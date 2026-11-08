from scrapers.ats import scrape_ashby


def scrape_skydio() -> list[dict]:
    return scrape_ashby("Skydio", slug="skydio")
