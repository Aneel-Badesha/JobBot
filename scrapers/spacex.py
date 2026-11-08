from scrapers.ats import scrape_greenhouse


def scrape_spacex() -> list[dict]:
    return scrape_greenhouse("SpaceX", slug="spacex")
