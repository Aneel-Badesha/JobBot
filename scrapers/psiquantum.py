from scrapers.ats import scrape_greenhouse


def scrape_psiquantum() -> list[dict]:
    return scrape_greenhouse("PsiQuantum", slug="psiquantum")
