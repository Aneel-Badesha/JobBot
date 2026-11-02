from scrapers.ats import scrape_greenhouse


def scrape_neuralink() -> list[dict]:
    return scrape_greenhouse("Neuralink", slug="neuralink")
