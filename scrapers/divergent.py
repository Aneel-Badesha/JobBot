from scrapers.ats import scrape_greenhouse


def scrape_divergent() -> list[dict]:
    return scrape_greenhouse("Divergent", slug="divergent")
