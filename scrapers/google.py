import json
import logging
import re
import time

import requests
from scrapers.filters import is_target_role, is_target_location

logger = logging.getLogger(__name__)

# The old careers.google.com/api/v3/search/ JSON API is dead (404s). Google's
# current careers site is a server-rendered SPA at
# www.google.com/about/careers/applications/jobs/results that embeds its job
# data as an AF_initDataCallback({key: 'ds:1', ..., data: [...]}) blob in the
# HTML. The "data:" array's inner payload is valid JSON, so we extract it with
# a bracket-balance scan and json.loads it directly, rather than trying to hit
# a JSON endpoint that no longer exists. `page` and `location` are honoured as
# query params server-side.
RESULTS_URL = "https://www.google.com/about/careers/applications/jobs/results"
PAGE_SIZE = 20
MAX_PAGES = 20

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; job-scraper/1.0)",
}

_DATA_CALLBACK_RE = re.compile(r"AF_initDataCallback\((\{.*?\})\);</script>", re.S)


def _extract_ds1(html: str):
    """Pull the ds:1 AF_initDataCallback payload (job results) out of the page."""
    for blob in _DATA_CALLBACK_RE.findall(html):
        if "'ds:1'" not in blob and '"ds:1"' not in blob:
            continue
        marker = "data:"
        start = blob.index(marker) + len(marker)
        s = blob[start:]
        depth = 0
        end = None
        for i, ch in enumerate(s):
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            continue
        try:
            return json.loads(s[:end])
        except json.JSONDecodeError:
            continue
    return None


def scrape_google() -> list[dict]:
    jobs = []
    page = 1

    while page <= MAX_PAGES:
        params = {"location": "Canada", "page": page}
        resp = requests.get(RESULTS_URL, params=params, headers=HEADERS, timeout=20)
        if resp.status_code != 200:
            logger.warning(f"Google careers page fetch failed: {resp.status_code}")
            break

        arr = _extract_ds1(resp.text)
        if not arr:
            logger.warning("Google careers page: could not find/parse ds:1 job data")
            break

        postings = arr[0] or []
        total = arr[2] if len(arr) > 2 and isinstance(arr[2], int) else 0
        if not postings:
            break

        for p in postings:
            title = p[1] if len(p) > 1 else ""
            if not title or not is_target_role(title):
                continue

            locs = p[9] if len(p) > 9 and p[9] else []
            loc_names = [l[0] for l in locs if l]
            loc_text = "; ".join(loc_names)
            # Check every location on the posting, not just the first.
            if not any(is_target_location(name) for name in loc_names):
                continue

            job_id = p[0] if len(p) > 0 else ""
            link = p[2] if len(p) > 2 else "https://www.google.com/about/careers/applications/jobs/results"

            jobs.append({
                "id": f"google-{job_id}",
                "company": "Google",
                "title": title,
                "location": loc_text,
                "link": link,
                "posted": "",
            })

        if page * PAGE_SIZE >= total or len(postings) < PAGE_SIZE:
            break
        page += 1
        time.sleep(0.5)

    return jobs
