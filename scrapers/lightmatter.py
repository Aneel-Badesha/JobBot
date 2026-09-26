from scrapers.ats import scrape_greenhouse


def scrape_lightmatter() -> list[dict]:
    return scrape_greenhouse("Lightmatter", slug="lightmatter")
