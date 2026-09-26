import logging

import requests
from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

# Huawei Canada's careers site runs on Recruitee (huaweicanada.recruitee.com),
# not the "career.huawei.com" custom portal guessed in the plan. Recruitee's
# public offers API returns the whole board in one call (no pagination
# needed; ~178 offers as of verification).
API_URL = "https://huaweicanada.recruitee.com/api/offers/"

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}


def scrape_huawei() -> list[dict]:
    jobs = []
    resp = requests.get(API_URL, headers=HEADERS, timeout=20)
    resp.raise_for_status()
    offers = resp.json().get("offers", [])

    for o in offers:
        title = o.get("title", "")
        if not is_target_role(title):
            continue

        loc_text = ", ".join(x for x in (o.get("city"), o.get("state_name"), o.get("country")) if x)
        if not is_target_location(loc_text):
            continue

        jobs.append({
            "id": f"huawei-{o.get('id')}",
            "company": "Huawei",
            "title": title,
            "location": loc_text,
            "link": o.get("careers_url", ""),
            "posted": o.get("updated_at", ""),
        })

    return jobs
