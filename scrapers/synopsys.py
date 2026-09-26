"""Synopsys careers (synopsys.avature.net) runs on Avature, which server-renders
the job search results as plain HTML — no API/JS required. The /Canada path
segment scopes the list to Canada, but the list view doesn't show a city — so
for each role-matching candidate we fetch the job detail page, which embeds a
small JSON blob (`legacyViewCopilotData`) with a real City field.
"""
import logging
import re
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

BASE_URL = "https://synopsys.avature.net"
SEARCH_PATH = "/careers/SearchJobs/Canada"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}
TIMEOUT = 20
PER_PAGE = 25
MAX_PAGES = 20

_CITY_RE = re.compile(r'"City":"([^"]*)"')
_STATE_RE = re.compile(r'"State\\?/Province":"([^"]*)"')
_TITLE_SUFFIX_RE = re.compile(r'\s*-\s*\d+$')


def scrape_synopsys() -> list[dict]:
    jobs = []
    offset = 0
    page = 0
    while page < MAX_PAGES:
        resp = requests.get(f"{BASE_URL}{SEARCH_PATH}",
                             params={"jobRecordsPerPage": PER_PAGE, "jobOffset": offset},
                             headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        links = soup.select('a[href*="/careers/JobDetail/"]')
        seen_on_page = {}
        for a in links:
            href = a.get("href", "")
            title = a.get_text(strip=True)
            if not href or not title:
                continue
            seen_on_page.setdefault(href, title)

        if not seen_on_page:
            break

        for href, raw_title in seen_on_page.items():
            title = _TITLE_SUFFIX_RE.sub("", raw_title)
            if not is_target_role(title):
                continue

            link = urljoin(BASE_URL, href)
            location = _detail_location(link)
            time.sleep(0.5)
            if not is_target_location(location):
                continue

            job_id = urlparse(link).path.rstrip("/").rsplit("/", 1)[-1]
            jobs.append({
                "id": f"synopsys-{job_id}",
                "company": "Synopsys",
                "title": title,
                "location": location,
                "link": link,
                "posted": "",
            })

        offset += PER_PAGE
        page += 1
        if len(seen_on_page) < PER_PAGE:
            break
        time.sleep(0.5)

    return jobs


def _detail_location(link: str) -> str:
    try:
        resp = requests.get(link, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        city_m = _CITY_RE.search(resp.text)
        state_m = _STATE_RE.search(resp.text)
        city = city_m.group(1) if city_m else ""
        state = state_m.group(1) if state_m else ""
        return ", ".join(p for p in (city, state) if p and p != city) or city
    except Exception as e:
        logger.warning(f"Synopsys detail fetch failed for {link}: {e}")
        return ""
