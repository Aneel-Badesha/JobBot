from scrapers.ats import scrape_ashby


def scrape_cerebras() -> list[dict]:
    return scrape_ashby("Cerebras", slug="cerebras")
