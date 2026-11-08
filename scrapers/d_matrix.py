from scrapers.ats import scrape_ashby


def scrape_d_matrix() -> list[dict]:
    return scrape_ashby("d-Matrix", slug="d-matrix")
