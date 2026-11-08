from scrapers.ats import scrape_greenhouse


def scrape_anduril() -> list[dict]:
    return scrape_greenhouse("Anduril", slug="andurilindustries")
