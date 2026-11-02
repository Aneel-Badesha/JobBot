from scrapers.ats import scrape_greenhouse


def scrape_astranis() -> list[dict]:
    return scrape_greenhouse("Astranis", slug="astranis")
