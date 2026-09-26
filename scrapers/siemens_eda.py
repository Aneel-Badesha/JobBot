"""Siemens EDA (Siemens Digital Industries Software) postings live on Siemens'
company-wide careers board, jobs.siemens.com, which runs on Avature and
server-renders results as plain HTML (no API/JS required). The /Canada path
segment scopes results server-side; is_target_role/is_target_location further
narrow out the many non-EDA Siemens business units also posted on this board.

Note: jobOffset/jobRecordsPerPage appear to be ignored by this Avature instance
without an established browsing session — every request (regardless of offset)
returns the same first batch (~6 postings) that a session-less client sees.
The pagination loop below is kept (capped at MAX_PAGES) in case that changes,
but in practice only the first batch is currently reachable this way.
"""
import logging
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

BASE_URL = "https://jobs.siemens.com"
SEARCH_PATH = "/en_US/externaljobs/SearchJobs/Canada"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}
TIMEOUT = 20
PER_PAGE = 50
MAX_PAGES = 20


def scrape_siemens_eda() -> list[dict]:
    jobs = []
    offset = 0
    page = 0
    while page < MAX_PAGES:
        resp = requests.get(f"{BASE_URL}{SEARCH_PATH}",
                             params={"jobRecordsPerPage": PER_PAGE, "jobOffset": offset},
                             headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        articles = soup.select("article.article--result")
        if not articles:
            break

        for article in articles:
            a = article.select_one("h3.article__header__text__title a.link")
            if not a:
                continue
            title = a.get_text(strip=True)
            if not is_target_role(title):
                continue

            city_el = article.select_one("span.list-item-jobCity")
            state_el = article.select_one("span.list-item-jobState")
            location = ", ".join(
                el.get_text(strip=True) for el in (city_el, state_el) if el
            )
            if not is_target_location(location):
                continue

            href = a.get("href", "")
            link = urljoin(BASE_URL, href)
            job_id = link.rstrip("/").rsplit("/", 1)[-1]
            jobs.append({
                "id": f"siemens-eda-{job_id}",
                "company": "Siemens EDA",
                "title": title,
                "location": location,
                "link": link,
                "posted": "",
            })

        offset += PER_PAGE
        page += 1
        if len(articles) < PER_PAGE:
            break
        time.sleep(0.5)

    return jobs
