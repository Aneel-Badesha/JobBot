import logging

logger = logging.getLogger(__name__)

# Best-effort / unresolved: careers.cisco.com / jobs.cisco.com run on the
# Phenom People platform (confirmed via response branding and CDN assets).
# Its public-facing career site does not expose an unauthenticated JSON
# search endpoint the way Eightfold-based sites do (Microsoft, Ericsson,
# Infineon) — probed patterns like /api/apply/v2/jobs and /api/career-site/jobs
# both return {"errorMsg": "Tenant not identified"}, and Phenom's documented
# developer API requires an OAuth token issued by Phenom support. Scraping
# this reliably would require a headless browser to replay the real frontend
# requests (with whatever tenant headers it sends), which is out of scope here.


def scrape_cisco() -> list[dict]:
    logger.warning("scrape_cisco: Cisco's Phenom-People-based career site has no "
                    "unauthenticated JSON API (tenant not identified without OAuth). Skipping.")
    return []
