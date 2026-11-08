from scrapers.ats import scrape_greenhouse


def scrape_torc() -> list[dict]:
    return scrape_greenhouse("Torc Robotics", slug="torcrobotics")
