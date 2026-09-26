"""L3Harris's careers.l3harris.com runs on Bullhorn TalentBrew (same platform as
Arm's careers site), server-rendered HTML — no API/JS required. The
/en/search-jobs/canada path scopes results to Canada.

L3Harris's TalentBrew skin differs from Arm's: job entries are plain <li>
elements (no "job-card" class) with an <a data-job-id> wrapping an <h2> title
and a "*location*"-classed span, rather than Arm's job-card__title/location
spans — so parsing here is more defensive about markup shape.

Note: as with Arm, TalentBrew's "next page" is an AJAX call, not a simple URL
page number, so we only fetch the first page here.
"""
import logging

import requests
from bs4 import BeautifulSoup

from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

BASE_URL = "https://careers.l3harris.com"
SEARCH_PATH = "/en/search-jobs/canada"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}
TIMEOUT = 20


def scrape_l3harris() -> list[dict]:
    jobs = []
    resp = requests.get(f"{BASE_URL}{SEARCH_PATH}", headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    section = soup.select_one("[data-total-pages]")
    if section:
        total_pages = section.get("data-total-pages")
        if total_pages and int(total_pages) > 1:
            logger.warning(f"L3Harris: results span {total_pages} pages; only fetching the first")

    seen_ids = set()
    for li in soup.select("li"):
        a = li.select_one("a[data-job-id]")
        if not a:
            continue
        job_id = a.get("data-job-id", "")
        if not job_id or job_id in seen_ids:
            continue
        seen_ids.add(job_id)

        h2 = a.select_one("h2")
        if h2:
            title = h2.get_text(strip=True)
        else:
            job_title_el = li.select_one(".job-title")
            title = job_title_el.get_text(strip=True) if job_title_el else a.get_text(strip=True)

        loc_el = li.select_one("[class*='location']")
        location = loc_el.get_text(strip=True) if loc_el else ""
        if not is_target_role(title) or not is_target_location(location):
            continue

        href = a.get("href", "")
        link = href if href.startswith("http") else f"{BASE_URL}{href}"
        jobs.append({
            "id": f"l3harris-{job_id}",
            "company": "L3Harris",
            "title": title,
            "location": location,
            "link": link,
            "posted": "",
        })

    return jobs
