from scrapers.ats import scrape_workday


def scrape_altera() -> list[dict]:
    return scrape_workday("Altera", tenant="altera", wd_instance="wd1", site="altera")
