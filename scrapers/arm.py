"""Arm's careers.arm.com runs on Bullhorn TalentBrew, which server-renders job
listings as plain HTML (no API, no JS execution required). The search-jobs/canada
path returns Arm's Canada roles (all based in Toronto, ~15 total) on a single
page, plus a handful of "related" postings from other countries/locales, which
is_target_location filters out.

Note: TalentBrew's "next page" is driven by an AJAX POST to a facet-search
endpoint (data-ajax-post-url), not a simple query/path page number — appending
a page number to the URL path breaks the location scoping entirely (it's
reinterpreted as a keyword search). Since Arm's whole Canada result set fits on
one page (15/page, ~15 results), we don't attempt further pagination here.
"""
import logging

import requests
from bs4 import BeautifulSoup

from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

BASE_URL = "https://careers.arm.com"
SEARCH_PATH = "/search-jobs/canada"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}
TIMEOUT = 20


def scrape_arm() -> list[dict]:
    jobs = []
    resp = requests.get(f"{BASE_URL}{SEARCH_PATH}", headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    total_pages = None
    section = soup.select_one("#search-results[data-total-pages]")
    if section:
        total_pages = section.get("data-total-pages")
        if total_pages and int(total_pages) > 1:
            logger.warning(f"Arm: results span {total_pages} pages; only fetching the first")

    for card in soup.select("li.job-card"):
        a = card.select_one("a.job-card__title")
        if not a:
            continue
        title = a.get_text(strip=True)
        loc_el = card.select_one("span.location")
        location = loc_el.get_text(strip=True) if loc_el else ""
        if not is_target_role(title) or not is_target_location(location):
            continue

        job_id = a.get("data-job-id", "")
        href = a.get("href", "")
        link = href if href.startswith("http") else f"{BASE_URL}{href}"
        jobs.append({
            "id": f"arm-{job_id}",
            "company": "Arm",
            "title": title,
            "location": location,
            "link": link,
            "posted": "",
        })

    return jobs
