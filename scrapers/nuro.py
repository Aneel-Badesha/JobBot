from scrapers.ats import scrape_greenhouse


def scrape_nuro() -> list[dict]:
    return scrape_greenhouse("Nuro", slug="nuro")
