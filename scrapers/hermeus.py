from scrapers.ats import scrape_lever


def scrape_hermeus() -> list[dict]:
    return scrape_lever("Hermeus", slug="hermeus")
