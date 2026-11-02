from scrapers.ats import scrape_greenhouse


def scrape_scout_motors() -> list[dict]:
    return scrape_greenhouse("Scout Motors", slug="scoutmotors")
