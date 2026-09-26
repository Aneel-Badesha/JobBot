from scrapers.ats import scrape_workday


def scrape_ciena() -> list[dict]:
    return scrape_workday("Ciena", tenant="ciena", wd_instance="wd5", site="Careers")
