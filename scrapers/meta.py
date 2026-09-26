import logging

logger = logging.getLogger(__name__)

# Best-effort / unresolved: metacareers.com renders jobs entirely client-side
# via a GraphQL endpoint that requires a rotating `doc_id` captured from
# browser devtools network traffic (confirmed via research: no stable public
# JSON endpoint exists, and the endpoint breaks silently whenever Meta
# redeploys the frontend). The server-rendered HTML (verified live) contains
# no embedded job data either, unlike Google's careers site. Scraping this
# reliably would require a headless browser, which is out of scope here.


def scrape_meta() -> list[dict]:
    logger.warning("scrape_meta: metacareers.com requires a rotating GraphQL doc_id "
                    "captured via browser devtools; no stable JSON API found. Skipping.")
    return []
