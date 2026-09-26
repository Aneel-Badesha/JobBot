from scrapers.ats import scrape_workday


def scrape_samsung() -> list[dict]:
    return scrape_workday("Samsung", tenant="sec", wd_instance="wd3", site="Samsung_Careers")
