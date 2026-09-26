"""Texas Instruments uses Oracle Recruiting Cloud (careers.ti.com -> Oracle-hosted
Candidate Experience site). The public REST API doesn't require auth. We scope the
search server-side with keyword="Canada" (TI has few Canadian postings, so this
keeps the request count tiny while still matching on PrimaryLocation text).
"""
import logging
import time

import requests

from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

HOST = "https://edbz.fa.us2.oraclecloud.com"
SITE_NUMBER = "CX"
API_URL = f"{HOST}/hcmRestApi/resources/latest/recruitingCEJobRequisitions"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}
TIMEOUT = 20
LIMIT = 25
MAX_PAGES = 20


def scrape_ti() -> list[dict]:
    jobs = []
    offset = 0
    page = 0
    while page < MAX_PAGES:
        finder = (f"findReqs;siteNumber={SITE_NUMBER},limit={LIMIT},offset={offset},"
                  f"keyword=Canada")
        resp = requests.get(API_URL, params={"onlyData": "true", "expand": "requisitionList.secondaryLocations", "finder": finder},
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
            location = r.get("PrimaryLocation", "")
            if not is_target_role(title) or not is_target_location(location):
                continue
            job_id = r.get("Id")
            jobs.append({
                "id": f"ti-{job_id}",
                "company": "Texas Instruments",
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
