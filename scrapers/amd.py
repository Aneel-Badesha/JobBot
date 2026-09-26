"""AMD careers site (careers.amd.com) runs on the Jibe/iCIMS "career-site" platform.

The rendered page is a client-side SPA, but it is backed by a plain JSON API at
/api/jobs that isn't gated — no auth, no JS execution required. `country=Canada`
scopes results server-side, and `page=N` paginates (10 jobs/page).
"""
import logging
import time

import requests

from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

API_URL = "https://careers.amd.com/api/jobs"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}
TIMEOUT = 20
MAX_PAGES = 20


def scrape_amd() -> list[dict]:
    jobs = []
    page = 1
    while page <= MAX_PAGES:
        resp = requests.get(API_URL, params={"country": "Canada", "page": page},
                             headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()

        postings = data.get("jobs", [])
        if not postings:
            break

        for posting in postings:
            d = posting.get("data", {})
            title = d.get("title", "")
            location = d.get("full_location") or d.get("location_name") or ""
            if not is_target_role(title) or not is_target_location(location):
                continue
            jobs.append({
                "id": f"amd-{d.get('req_id') or d.get('slug')}",
                "company": "AMD",
                "title": title,
                "location": location,
                "link": (d.get("meta_data") or {}).get("canonical_url")
                        or f"{API_URL.rsplit('/api/', 1)[0]}/jobs/{d.get('slug') or d.get('req_id')}",  # posting page, not iCIMS apply/login
                "posted": d.get("posted_date", ""),
            })

        total = data.get("totalCount", 0)
        if page * 10 >= total:
            break
        page += 1
        time.sleep(0.5)

    return jobs
