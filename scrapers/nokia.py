"""Nokia uses Oracle Recruiting Cloud (jobs.nokia.com -> Oracle-hosted Candidate
Experience site). Public REST API, no auth required.

Unlike TI/Ford, Nokia's list view only reports "Canada" as PrimaryLocation (no
city), which isn't enough for our location filter (Ottawa/Toronto/etc). So for
each Canada-scoped, role-matching candidate we fetch the requisition detail
endpoint once to get the real city (workLocation.TownOrCity).
"""
import logging
import time

import requests

from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

HOST = "https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com"
SITE_NUMBER = "CX_1"
LIST_URL = f"{HOST}/hcmRestApi/resources/latest/recruitingCEJobRequisitions"
DETAIL_URL = f"{HOST}/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}
TIMEOUT = 20
LIMIT = 25
MAX_PAGES = 20


def _detail_location(job_id: str) -> str:
    try:
        finder = f'ById;Id="{job_id}",siteNumber={SITE_NUMBER}'
        resp = requests.get(DETAIL_URL, params={"onlyData": "true", "expand": "all", "finder": finder},
                             headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        items = resp.json().get("items") or []
        if not items:
            return ""
        work_locations = items[0].get("workLocation") or []
        parts = []
        for loc in work_locations:
            city = loc.get("TownOrCity", "")
            region = loc.get("Region2", "")
            if city:
                parts.append(f"{city}, {region}".strip(", "))
        return "; ".join(parts)
    except Exception as e:
        logger.warning(f"Nokia detail fetch failed for {job_id}: {e}")
        return ""


def scrape_nokia() -> list[dict]:
    jobs = []
    offset = 0
    page = 0
    while page < MAX_PAGES:
        finder = (f"findReqs;siteNumber={SITE_NUMBER},limit={LIMIT},offset={offset},"
                  f"keyword=Canada")
        resp = requests.get(LIST_URL, params={"onlyData": "true", "expand": "requisitionList.secondaryLocations", "finder": finder},
                             headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        items = data.get("items") or []
        if not items:
            break
        item = items[0]
        reqs = item.get("requisitionList", [])
        if not reqs:
            break

        for r in reqs:
            title = r.get("Title", "")
            if not is_target_role(title):
                continue
            job_id = r.get("Id")
            location = _detail_location(job_id) or r.get("PrimaryLocation", "")
            time.sleep(0.5)
            if not is_target_location(location):
                continue
            jobs.append({
                "id": f"nokia-{job_id}",
                "company": "Nokia",
                "title": title,
                "location": location,
                "link": f"{HOST}/hcmUI/CandidateExperience/en/sites/{SITE_NUMBER}/job/{job_id}",
                "posted": r.get("PostedDate", ""),
            })

        total = item.get("TotalJobsCount", 0)
        offset += LIMIT
        page += 1
        if offset >= total:
            break
        time.sleep(0.5)

    return jobs
