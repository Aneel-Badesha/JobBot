import logging
import time

import requests
from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

# Amazon has a public jobs JSON API. NOTE: `loc_query` (the old param this file
# used) no longer filters server-side — it silently returns the same unfiltered
# firehose regardless of value (verified: "Canada", "Toronto", "" all return
# identical results with hits stuck at 10000, the Elasticsearch result-window
# cap). `normalized_country_code[]=CAN` is the param that actually filters to
# Canada (hits ~421, real CAN-only postings), so we use that instead.
API_URL = "https://www.amazon.jobs/en/search.json"
PAGE_SIZE = 10
MAX_PAGES = 60  # sane cap; ~421 CAN postings / 10 per page ~= 43 pages today

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}


def scrape_amazon() -> list[dict]:
    jobs = []
    offset = 0
    pages = 0

    while pages < MAX_PAGES:
        params = {
            "base_query": "",
            "normalized_country_code[]": "CAN",
            "job_count": PAGE_SIZE,
            "result_limit": PAGE_SIZE,
            "sort": "recent",
            "offset": offset,
            "latitude": "",
            "longitude": "",
            "loc_group_id": "",
        }
        resp = requests.get(API_URL, params=params, headers=HEADERS, timeout=20)
        resp.raise_for_status()
        data = resp.json()

        postings = data.get("jobs", [])
        if not postings:
            break

        for p in postings:
            title = p.get("title", "")
            if not is_target_role(title):
                continue

            location = p.get("normalized_location", p.get("location", "Canada"))
            if not is_target_location(location):
                continue

            job_id = p.get("id_icims", p.get("job_id", ""))
            link = f"https://www.amazon.jobs/en/jobs/{job_id}" if job_id else "https://www.amazon.jobs"

            jobs.append({
                "id": f"amazon-{job_id}",
                "company": "Amazon",
                "title": title,
                "location": location,
                "link": link,
                "posted": p.get("posted_date", ""),
            })

        hits = data.get("hits", 0)
        offset += PAGE_SIZE
        pages += 1
        if offset >= hits or len(postings) < PAGE_SIZE:
            break
        time.sleep(0.5)

    return jobs
