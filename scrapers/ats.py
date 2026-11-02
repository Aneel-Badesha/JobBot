"""Shared fetchers for common applicant-tracking systems.

Each per-company scraper is a thin wrapper that calls one of these with its
board identifiers. Every helper applies is_target_role + is_target_location and
returns the standard job dict: {id, company, title, location, link, posted}.
"""
import logging
import time

import requests
from scrapers.filters import is_target_role, is_target_location, is_us_location

logger = logging.getLogger(__name__)

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}
TIMEOUT = 20


def _job(job_id: str, company: str, title: str, location: str, link: str, posted: str = "") -> dict:
    return {
        "id": job_id,
        "company": company,
        "title": title,
        "location": location,
        "link": link,
        "posted": posted,
    }


# --- Workday -----------------------------------------------------------------

def scrape_workday(company: str, tenant: str, wd_instance: str, site: str,
                   search_text: str = "Canada", us_interns: bool = True) -> list[dict]:
    """Workday CXS API. search_text scopes results server-side (default "Canada"),
    which keeps big boards (NVIDIA ~2000 postings) to a handful of pages. A second
    pass searches "intern" filtered to the board's United States location facet."""
    base_url = f"https://{tenant}.{wd_instance}.myworkdayjobs.com"
    api_url = f"{base_url}/wday/cxs/{tenant}/{site}/jobs"
    headers = {**HEADERS, "Content-Type": "application/json"}

    jobs = _workday_pass(company, tenant, site, base_url, api_url, headers, search_text, {})
    # An empty search_text already covers the whole board
    if us_interns and search_text:
        us_facets = _workday_us_facets(api_url, headers)
        seen = {j["id"] for j in jobs}
        jobs += [j for j in _workday_pass(company, tenant, site, base_url, api_url, headers, "intern", us_facets)
                 if j["id"] not in seen]
    return jobs


def _workday_us_facets(api_url: str, headers: dict) -> dict:
    """Find the board's facet values for United States. Facet names and ids vary
    by tenant (locationCountry, Location_Country, locationHierarchy1, ...). Boards
    with only a per-city "locations" facet get every US-looking city instead, and
    boards with neither get no facet (the "intern" search is small enough)."""
    resp = requests.post(api_url, json={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": "intern"},
                         headers=headers, timeout=TIMEOUT)
    resp.raise_for_status()

    country, cities = {}, {}

    def walk(facets):
        for f in facets:
            param = f.get("facetParameter", "")
            for v in f.get("values", []) or []:
                if "values" in v:
                    walk([v])
                    continue
                desc = v.get("descriptor", "")
                if "country" in param.lower() or "hierarchy1" in param.lower():
                    if desc in ("United States", "United States of America", "USA"):
                        country.setdefault(param, []).append(v["id"])
                elif "location" in param.lower() and is_us_location(desc):
                    cities.setdefault(param, []).append(v["id"])

    walk(resp.json().get("facets", []))
    return country or cities


def _workday_pass(company: str, tenant: str, site: str, base_url: str, api_url: str,
                  headers: dict, search_text: str, facets: dict) -> list[dict]:
    jobs = []
    limit = 20
    offset = 0

    while True:
        payload = {"appliedFacets": facets, "limit": limit, "offset": offset, "searchText": search_text}
        resp = requests.post(api_url, json=payload, headers=headers, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()

        postings = data.get("jobPostings", [])
        # Workday only reports the total on the first page
        if offset == 0:
            total = data.get("total", 0)

        for posting in postings:
            title = posting.get("title", "")
            if not is_target_role(title):
                continue
            external_path = posting.get("externalPath", "")
            location = posting.get("locationsText", "")
            # Multi-location postings show "N Locations" — fetch detail for the real list
            if location.lower().endswith("locations"):
                location = _workday_locations(api_url.rsplit("/jobs", 1)[0], external_path, headers) or location
            if not is_target_location(location):
                continue

            jobs.append(_job(
                f"workday-{tenant}-{external_path.strip('/')}",
                company, title, location,
                f"{base_url}/{site}{external_path}",
                posting.get("postedOn", ""),
            ))

        offset += limit
        if offset >= total or not postings:
            break
        time.sleep(0.5)

    return jobs


def _workday_locations(site_api: str, external_path: str, headers: dict) -> str:
    try:
        resp = requests.get(f"{site_api}{external_path}", headers=headers, timeout=TIMEOUT)
        resp.raise_for_status()
        info = resp.json().get("jobPostingInfo", {})
        locs = [info.get("location", "")] + list(info.get("additionalLocations", []))
        return "; ".join(l for l in locs if l)
    except Exception as e:
        logger.warning(f"Workday detail fetch failed for {external_path}: {e}")
        return ""


# --- Greenhouse --------------------------------------------------------------

def scrape_greenhouse(company: str, slug: str) -> list[dict]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
    resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()

    jobs = []
    for p in resp.json().get("jobs", []):
        title = p.get("title", "")
        location = (p.get("location") or {}).get("name", "")
        offices = "; ".join(o.get("name", "") for o in p.get("offices", []) if o.get("name"))
        loc_text = f"{location}; {offices}" if offices else location
        if not is_target_role(title) or not is_target_location(loc_text):
            continue
        jobs.append(_job(
            f"greenhouse-{slug}-{p.get('id')}",
            company, title, location or offices,
            p.get("absolute_url", ""),
            p.get("updated_at", ""),
        ))
    return jobs


# --- Ashby -------------------------------------------------------------------

def scrape_ashby(company: str, slug: str) -> list[dict]:
    url = f"https://api.ashbyhq.com/posting-api/job-board/{slug}"
    resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()

    jobs = []
    for p in resp.json().get("jobs", []):
        title = p.get("title", "")
        locs = [p.get("location", "")] + [
            s.get("location", "") for s in p.get("secondaryLocations", []) or []
        ]
        loc_text = "; ".join(l for l in locs if l)
        if not is_target_role(title) or not is_target_location(loc_text):
            continue
        jobs.append(_job(
            f"ashby-{slug}-{p.get('id')}",
            company, title, loc_text,
            p.get("jobUrl", ""),
            p.get("publishedAt", ""),
        ))
    return jobs


# --- Lever -------------------------------------------------------------------

def scrape_lever(company: str, slug: str) -> list[dict]:
    url = f"https://api.lever.co/v0/postings/{slug}?mode=json"
    resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()

    jobs = []
    for p in resp.json():
        title = p.get("text", "")
        cats = p.get("categories", {}) or {}
        loc_text = "; ".join([cats.get("location", "")] + list(cats.get("allLocations", []) or []))
        if not is_target_role(title) or not is_target_location(loc_text):
            continue
        jobs.append(_job(
            f"lever-{slug}-{p.get('id')}",
            company, title, cats.get("location", ""),
            p.get("hostedUrl", ""),
            str(p.get("createdAt", "")),
        ))
    return jobs


# --- Workable ----------------------------------------------------------------

def scrape_workable(company: str, slug: str) -> list[dict]:
    url = f"https://apply.workable.com/api/v1/widget/accounts/{slug}"
    resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()

    jobs = []
    for p in resp.json().get("jobs", []):
        title = p.get("title", "")
        loc_text = ", ".join(x for x in (p.get("city"), p.get("state"), p.get("country")) if x)
        if not is_target_role(title) or not is_target_location(loc_text):
            continue
        jobs.append(_job(
            f"workable-{slug}-{p.get('shortcode')}",
            company, title, loc_text,
            p.get("url") or p.get("shortlink", ""),
            p.get("published_on", ""),
        ))
    return jobs


# --- SmartRecruiters ---------------------------------------------------------

def scrape_smartrecruiters(company: str, slug: str, countries: tuple = ("ca", "us")) -> list[dict]:
    jobs = []
    for country in countries:
        jobs += _smartrecruiters_country(company, slug, country)
    return jobs


def _smartrecruiters_country(company: str, slug: str, country: str) -> list[dict]:
    url = f"https://api.smartrecruiters.com/v1/companies/{slug}/postings"
    jobs = []
    offset = 0
    while True:
        resp = requests.get(url, params={"country": country, "limit": 100, "offset": offset},
                            headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        content = data.get("content", [])
        for p in content:
            title = p.get("name", "")
            loc = p.get("location", {}) or {}
            loc_text = ", ".join(x for x in (loc.get("city"), loc.get("region"), loc.get("country")) if x)
            if not is_target_role(title) or not is_target_location(loc_text):
                continue
            jobs.append(_job(
                f"smartrecruiters-{slug}-{p.get('id')}",
                company, title, loc_text,
                f"https://jobs.smartrecruiters.com/{slug}/{p.get('id')}",
                p.get("releasedDate", ""),
            ))
        offset += len(content)
        if not content or offset >= data.get("totalFound", 0):
            break
        time.sleep(0.5)
    return jobs


# --- UltiPro (UKG Pro Recruiting) --------------------------------------------

def scrape_ultipro(company: str, host: str, tenant: str, boards: list[str]) -> list[dict]:
    """UKG job boards POST their search to JobBoardView/LoadSearchResults; no auth."""
    headers = {**HEADERS, "Content-Type": "application/json"}
    jobs, seen = [], set()
    for board in boards:
        board_url = f"https://{host}/{tenant}/JobBoard/{board}"
        skip = 0
        while True:
            payload = {"opportunitySearch": {
                "Top": 50, "Skip": skip, "QueryString": "", "Filters": [],
                "OrderBy": [{"Value": "postedDateDesc", "PropertyName": "PostedDate", "Ascending": False}],
            }}
            resp = requests.post(f"{board_url}/JobBoardView/LoadSearchResults", json=payload,
                                 headers=headers, timeout=TIMEOUT)
            resp.raise_for_status()
            data = resp.json()
            ops = data.get("opportunities", [])
            for o in ops:
                title = o.get("Title", "")
                locs = []
                for l in o.get("Locations", []) or []:
                    a = l.get("Address") or {}
                    locs.append(", ".join(x for x in (a.get("City"), (a.get("State") or {}).get("Name"),
                                                      (a.get("Country") or {}).get("Name")) if x))
                loc_text = "; ".join(l for l in locs if l)
                if o.get("Id") in seen or not is_target_role(title) or not is_target_location(loc_text):
                    continue
                seen.add(o.get("Id"))
                jobs.append(_job(
                    f"ultipro-{tenant}-{o.get('Id')}",
                    company, title, loc_text,
                    f"{board_url}/OpportunityDetail?opportunityId={o.get('Id')}",
                    o.get("PostedDate", ""),
                ))
            skip += len(ops)
            if not ops or skip >= data.get("totalCount", 0):
                break
            time.sleep(0.5)
    return jobs
