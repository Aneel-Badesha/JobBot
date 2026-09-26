from scrapers.ats import scrape_workday


def scrape_intel() -> list[dict]:
    return scrape_workday("Intel", tenant="intel", wd_instance="wd1", site="External")
