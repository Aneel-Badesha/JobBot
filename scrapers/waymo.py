from scrapers.ats import scrape_greenhouse


def scrape_waymo() -> list[dict]:
    return scrape_greenhouse("Waymo", slug="waymo")
