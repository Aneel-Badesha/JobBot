import logging

logger = logging.getLogger(__name__)


def scrape_alphawave() -> list[dict]:
    """Alphawave Semi uses an unknown ATS platform.

    Careers page (https://alphawaveipexcess.com/careers) is unreachable (connection error).
    Tested: Greenhouse, Ashby, Lever, Workable, SmartRecruiters, Workday — none found.
    Best-effort: Cannot reliably scrape.
    """
    logger.warning("Alphawave Semi: Careers page unreachable; no supported ATS endpoint found")
    return []
