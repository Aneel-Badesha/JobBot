import logging

logger = logging.getLogger(__name__)


def scrape_jetson_ai() -> list[dict]:
    """Jetson AI (Toronto startup) uses an unknown ATS platform.

    Careers page (https://jetsonaicorp.com) is unreachable (connection error).
    Tested: Greenhouse, Ashby, Lever, Workable, SmartRecruiters, Workday — none found.
    Best-effort: Cannot reliably scrape.
    """
    logger.warning("Jetson AI: Careers page unreachable; no supported ATS endpoint found")
    return []
