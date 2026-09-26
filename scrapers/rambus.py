import logging

logger = logging.getLogger(__name__)


def scrape_rambus() -> list[dict]:
    """Rambus's careers site (careers.rambus.com, custom domain) is fronted by
    Cloudflare bot protection: every request (root, /jobs, and individual job
    detail pages) returns HTTP 403 with a Cloudflare "Attention Required"
    challenge page, even with a browser-like User-Agent. Job URLs found via
    search (e.g. careers.rambus.com/jobs/<slug>-<uuid>) look like a Lever-style
    posting id, but api.lever.co/v0/postings/rambus returns 404 — Rambus is not
    on Lever, Greenhouse, Ashby, Workable, SmartRecruiters, or Workday either.
    No scrapable endpoint without a browser (to pass the Cloudflare challenge).
    """
    logger.warning("Rambus: careers.rambus.com is behind Cloudflare bot protection (403); no scrapable endpoint found")
    return []
