from scrapers.ats import scrape_greenhouse


def scrape_ionq() -> list[dict]:
    return scrape_greenhouse("IonQ", slug="ionq")
