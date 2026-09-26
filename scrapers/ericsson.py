import logging
import time

import requests
from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

# Ericsson careers runs on Eightfold's "PCSX" platform (same underlying
# platform as Microsoft's careers site), verified live at
# jobs.ericsson.com/api/pcsx/search with domain=ericsson.com.
API_URL = "https://jobs.ericsson.com/api/pcsx/search"
HOST = "https://jobs.ericsson.com"
DOMAIN = "ericsson.com"
PAGE_SIZE = 20
MAX_PAGES = 20

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}


def scrape_ericsson() -> list[dict]:
    jobs = []
    start = 0

    for _ in range(MAX_PAGES):
        params = {
            "domain": DOMAIN,
            "query": "",
            "location": "Canada",
            "start": start,
            "num": PAGE_SIZE,
        }
        resp = requests.get(API_URL, params=params, headers=HEADERS, timeout=20)
        resp.raise_for_status()
        data = resp.json().get("data", {})

        positions = data.get("positions", [])
        if not positions:
            break

        for p in positions:
            title = p.get("name", "")
            if not is_target_role(title):
                continue
            locs = p.get("standardizedLocations") or p.get("locations") or []
            loc_text = "; ".join(locs)
            if not any(is_target_location(l) for l in locs) and not is_target_location(loc_text):
                continue

            job_id = p.get("displayJobId") or p.get("id")
            link = HOST + p.get("positionUrl", "")

            jobs.append({
                "id": f"ericsson-{job_id}",
                "company": "Ericsson",
                "title": title,
                "location": loc_text,
                "link": link,
                "posted": "",
            })

        total = data.get("count", 0)
        start += PAGE_SIZE
        if start >= total or len(positions) < PAGE_SIZE:
            break
        time.sleep(0.5)

    return jobs
