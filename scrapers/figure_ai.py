from scrapers.ats import scrape_greenhouse


def scrape_figure_ai() -> list[dict]:
    return scrape_greenhouse("Figure AI", slug="figureai")
