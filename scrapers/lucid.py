from scrapers.ats import scrape_greenhouse


def scrape_lucid() -> list[dict]:
    return scrape_greenhouse("Lucid Motors", slug="lucidmotors")
