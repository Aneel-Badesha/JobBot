from scrapers.ats import scrape_greenhouse


def scrape_tenstorrent() -> list[dict]:
    return scrape_greenhouse("Tenstorrent", slug="tenstorrent")
