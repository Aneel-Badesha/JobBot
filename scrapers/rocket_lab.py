from scrapers.ats import scrape_greenhouse


def scrape_rocket_lab() -> list[dict]:
    return scrape_greenhouse("Rocket Lab", slug="rocketlab")
