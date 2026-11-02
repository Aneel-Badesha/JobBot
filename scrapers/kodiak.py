from scrapers.ats import scrape_greenhouse


def scrape_kodiak() -> list[dict]:
    return scrape_greenhouse("Kodiak Robotics", slug="kodiak")
