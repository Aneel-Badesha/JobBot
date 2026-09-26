from scrapers.ats import scrape_greenhouse


def scrape_astera_labs() -> list[dict]:
    return scrape_greenhouse("Astera Labs", slug="asteralabs")
