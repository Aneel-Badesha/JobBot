from scrapers.ats import scrape_workday


def scrape_kla() -> list[dict]:
    return scrape_workday("KLA", tenant="kla", wd_instance="wd1", site="Search")
