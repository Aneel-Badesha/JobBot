from scrapers.ats import scrape_ashby


def scrape_saronic() -> list[dict]:
    return scrape_ashby("Saronic", slug="saronic")
