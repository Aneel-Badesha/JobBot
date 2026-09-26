import logging
import time

import requests
from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

# onsemi's careers.onsemi.com site is powered by Oracle Recruiting Cloud
# (Oracle HCM), not iCIMS as guessed in the plan. Verified live at
# hctz.fa.us2.oraclecloud.com with siteNumber=CX_1001.
API_URL = "https://hctz.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions"
SITE_NUMBER = "CX_1001"
PAGE_SIZE = 25
MAX_PAGES = 20

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}


def scrape_onsemi() -> list[dict]:
    jobs = []
    offset = 0

    for _ in range(MAX_PAGES):
        finder = (
            f"findReqs;siteNumber={SITE_NUMBER},facetsList=LOCATIONS,"
            f"limit={PAGE_SIZE},offset={offset},sortBy=POSTING_DATES_DESC,keyword=Canada"
        )
        params = {
            "onlyData": "true",
            "expand": "requisitionList.secondaryLocations,flexFieldsFacet.values",
            "finder": finder,
        }
        resp = requests.get(API_URL, params=params, headers=HEADERS, timeout=20)
        resp.raise_for_status()
        items = resp.json().get("items", [])
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

            locs = [r.get("PrimaryLocation", "")] + [
                s.get("Location", "") for s in r.get("secondaryLocations", []) or []
            ]
            loc_text = "; ".join(l for l in locs if l)
            if not is_target_location(loc_text):
                continue

            job_id = r.get("Id")
            jobs.append({
                "id": f"onsemi-{job_id}",
                "company": "onsemi",
                "title": title,
                "location": loc_text,
                "link": f"https://hctz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/{SITE_NUMBER}/job/{job_id}",
                "posted": r.get("PostedDate", ""),
            })

        total = item.get("TotalJobsCount", 0)
        offset += PAGE_SIZE
        if offset >= total or len(reqs) < PAGE_SIZE:
            break
        time.sleep(0.5)

    return jobs
