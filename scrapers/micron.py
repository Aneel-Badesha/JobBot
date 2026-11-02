from scrapers.ats import scrape_workday


def scrape_micron() -> list[dict]:
    return scrape_workday("Micron", tenant="micron", wd_instance="wd1", site="External")
