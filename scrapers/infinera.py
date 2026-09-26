from scrapers.ats import scrape_workday


def scrape_infinera() -> list[dict]:
    return scrape_workday("Infinera", tenant="infinera", wd_instance="wd1", site="infinera_Careers")
