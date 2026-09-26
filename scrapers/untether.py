import logging

logger = logging.getLogger(__name__)


def scrape_untether() -> list[dict]:
    """Untether AI (small Toronto startup) uses an unknown ATS platform.

    Careers page (https://untether.ai/careers) is unreachable (SSL/DNS error).
    Tested: Greenhouse, Ashby, Lever, Workable, SmartRecruiters, Workday — none found.
    Best-effort: Cannot reliably scrape.
    """
    logger.warning("Untether AI: Careers page unreachable; no supported ATS endpoint found")
    return []
