from scrapers.ats import scrape_lever


def scrape_waabi() -> list[dict]:
    return scrape_lever("Waabi", slug="waabi")
