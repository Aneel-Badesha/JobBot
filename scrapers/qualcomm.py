import logging
import time

import requests
from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

# Qualcomm moved off Workday (the wd12 board now reports 0 postings) to
# Eightfold PCSX at careers.qualcomm.com — same API as Microsoft/Ericsson.
API_URL = "https://careers.qualcomm.com/api/pcsx/search"
HOST = "https://careers.qualcomm.com"
DOMAIN = "qualcomm.com"
PAGE_SIZE = 10
MAX_PAGES = 40

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}


def _scrape_qualcomm(query: str, location: str) -> list[dict]:
    jobs = []
    start = 0

    for _ in range(MAX_PAGES):
        params = {"domain": DOMAIN, "query": query, "location": location, "start": start, "num": PAGE_SIZE}
        resp = requests.get(API_URL, params=params, headers=HEADERS, timeout=20)
        resp.raise_for_status()
        data = resp.json().get("data", {})

        positions = data.get("positions", [])
        if not positions:
            break

        for p in positions:
            title = p.get("name", "").lstrip("#")
            if not is_target_role(title):
                continue
            locs = p.get("standardizedLocations") or p.get("locations") or []
            loc_text = "; ".join(locs)
            if not is_target_location(loc_text):
                continue

            job_id = p.get("displayJobId") or p.get("id")
            jobs.append({
                "id": f"qualcomm-{job_id}",
                "company": "Qualcomm",
                "title": title,
                "location": loc_text,
                "link": HOST + p.get("positionUrl", ""),
                "posted": "",
            })

        total = data.get("count", 0)
        start += len(positions)
        if start >= total:
            break
        time.sleep(0.5)

    return jobs


def scrape_qualcomm() -> list[dict]:
    jobs, seen = [], set()
    for scope in [("", "Canada"), ("intern", "United States")]:
        for job in _scrape_qualcomm(*scope):
            if job["id"] not in seen:
                seen.add(job["id"])
                jobs.append(job)
    return jobs
