"""Active internships from the community-maintained SimplifyJobs list, which covers
companies we have no working scraper for. Duplicates of our company-board rows
are merged in storage.merge_jobs.
"""
import logging
import re
from datetime import date, datetime, timedelta, timezone

import requests

from scrapers.filters import is_target_role, is_target_location, work_auth_flag

logger = logging.getLogger(__name__)

URL = "https://raw.githubusercontent.com/SimplifyJobs/Summer2027-Internships/dev/.github/scripts/listings.json"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)"}
TIMEOUT = 60
# Rows with no term ("N/A") are only trusted if someone touched them recently
NO_TERM_MAX_AGE = timedelta(days=90)

_TERM_START_MONTH = {"Winter": 1, "Spring": 3, "Summer": 5, "Fall": 9}
_SHORT_LOCATIONS = {"SF": "San Francisco, CA", "NYC": "New York, NY", "LA": "Los Angeles, CA"}
# Filters skip these state codes as they collide with country codes elsewhere,
# but this list only covers the US and Canada.
_AMBIGUOUS_STATE_RE = re.compile(r",\s*(?:IL|IN|DE)$")


def _is_upcoming(row: dict, today: date) -> bool:
    terms = [t.split() for t in row.get("terms", []) if re.fullmatch(r"\w+ \d{4}", t)]
    terms = [(s, int(y)) for s, y in terms if s in _TERM_START_MONTH]
    if terms:
        return any(date(y, _TERM_START_MONTH[s], 1) >= today.replace(day=1) for s, y in terms)
    updated = datetime.fromtimestamp(row.get("date_updated", 0), tz=timezone.utc).date()
    return today - updated <= NO_TERM_MAX_AGE


def _location(raw: str) -> str:
    raw = _SHORT_LOCATIONS.get(raw.strip(), raw.strip())
    return f"{raw}, USA" if _AMBIGUOUS_STATE_RE.search(raw) else raw


def scrape_simplify() -> list[dict]:
    resp = requests.get(URL, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()

    today = date.today()
    jobs = []
    for row in resp.json():
        if not row.get("active") or not row.get("is_visible") or row.get("category") != "Hardware":
            continue
        title = row.get("title", "")
        location = "; ".join(_location(l) for l in row.get("locations", []) if l)
        if not is_target_role(title) or not is_target_location(location) or not _is_upcoming(row, today):
            continue
        degrees = row.get("degrees") or []
        jobs.append({
            "id": f"simplify-{row.get('id')}",
            "company": row.get("company_name", ""),
            "title": title,
            "location": location,
            "link": row.get("url", ""),
            "posted": datetime.fromtimestamp(row.get("date_posted", 0), tz=timezone.utc).date().isoformat(),
            "terms": [t for t in row.get("terms", []) if re.fullmatch(r"(?:Winter|Spring|Summer|Fall) \d{4}", t)],
            "work_auth": work_auth_flag(row.get("sponsorship", "").replace("U.S. Citizenship is Required", "U.S. citizen")
                                        .replace("Does Not Offer Sponsorship", "no sponsorship")),
            "grad_only": bool(degrees) and "Bachelor's" not in degrees,
        })
    return jobs
