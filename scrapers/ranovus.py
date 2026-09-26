import logging

logger = logging.getLogger(__name__)


def scrape_ranovus() -> list[dict]:
    """Ranovus (Ottawa-based semi startup) uses LinkedIn for careers.

    Careers page (https://ranovus.com/careers/) redirects to LinkedIn.
    No supported ATS endpoint found (Greenhouse, Ashby, Lever, Workable, SmartRecruiters).
    Best-effort: LinkedIn scraping would require Selenium or fragile HTML parsing.
    """
    logger.warning("Ranovus: Uses LinkedIn for careers; no supported ATS endpoint found")
    return []
