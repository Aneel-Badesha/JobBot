import logging

logger = logging.getLogger(__name__)

# Best-effort / unresolved: www.tesla.com/careers is behind Akamai bot
# protection — every request (even the plain HTML search page, let alone any
# API path) returns a 403 "Access Denied" Akamai block page when fetched with
# plain requests. This matches the heavy-bot-protection case called out
# up front as not worth deep investigation; scraping it would require a
# real browser (and likely still get flagged).


def scrape_tesla() -> list[dict]:
    logger.warning("scrape_tesla: tesla.com is behind Akamai bot protection "
                    "(403 on all plain-requests fetches). Skipping.")
    return []
