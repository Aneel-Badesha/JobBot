from scrapers.ats import scrape_ashby


def scrape_shield_ai() -> list[dict]:
    return scrape_ashby("Shield AI", slug="shieldai")
