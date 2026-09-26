import logging

logger = logging.getLogger(__name__)


def scrape_photonic() -> list[dict]:
    """Photonic Inc. uses an unknown ATS platform.

    Careers page (https://www.photonic.com/careers) returns 403 Forbidden.
    Tested: Greenhouse, Ashby, Lever, Workable, SmartRecruiters, Workday — none found.
    """
    logger.warning("Photonic Inc.: Careers page is protected (403 Forbidden); no supported ATS endpoint found")
    return []
