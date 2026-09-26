import logging

logger = logging.getLogger(__name__)

# Best-effort / unresolved: IBM's careers site (www.ibm.com/careers/search)
# is a JS-rendered SPA with no embedded job data in the server-rendered HTML
# and no discoverable JSON API endpoint (probed common patterns: SmartRecruiters
# "careers.smartrecruiters.com/IBM" returns 0 real postings for Canada — it's
# an unrelated/inactive board, not IBM's live careers site; Avature
# "ibmglobal.avature.net" appears to be a different regional/legacy portal;
# several guessed REST paths under ibm.com/careers/api/* all 404 to the same
# SPA shell). Scraping this reliably would require a headless browser to
# observe the real XHR calls, which is out of scope here.


def scrape_ibm() -> list[dict]:
    logger.warning("scrape_ibm: no working public JSON endpoint found for IBM careers "
                    "(SPA with no embedded data); would need a headless browser. Skipping.")
    return []
