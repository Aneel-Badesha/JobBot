from scrapers.ats import scrape_greenhouse


def scrape_motional() -> list[dict]:
    return scrape_greenhouse("Motional", slug="motional")
