from scrapers.ats import scrape_greenhouse


def scrape_agility_robotics() -> list[dict]:
    return scrape_greenhouse("Agility Robotics", slug="agilityrobotics")
