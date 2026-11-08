from scrapers.ats import scrape_greenhouse


def scrape_sambanova() -> list[dict]:
    return scrape_greenhouse("SambaNova", slug="sambanovasystems")
