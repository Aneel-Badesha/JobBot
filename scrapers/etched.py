from scrapers.ats import scrape_ashby


def scrape_etched() -> list[dict]:
    return scrape_ashby("Etched", slug="etched")
