from scrapers.ats import scrape_lever


def scrape_shield_ai() -> list[dict]:
    return scrape_lever("Shield AI", slug="shieldai")
