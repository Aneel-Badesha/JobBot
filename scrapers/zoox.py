from scrapers.ats import scrape_lever


def scrape_zoox() -> list[dict]:
    return scrape_lever("Zoox", slug="zoox")
