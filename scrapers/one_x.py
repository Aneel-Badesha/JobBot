from scrapers.ats import scrape_ashby


def scrape_one_x() -> list[dict]:
    return scrape_ashby("1X", slug="1x")
