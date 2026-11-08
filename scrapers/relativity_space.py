from scrapers.ats import scrape_greenhouse


def scrape_relativity_space() -> list[dict]:
    return scrape_greenhouse("Relativity Space", slug="relativity")
