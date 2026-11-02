from scrapers.ats import scrape_ashby


def scrape_fab2() -> list[dict]:
    return scrape_ashby("Fab2", slug="fab2")
