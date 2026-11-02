from scrapers.ats import scrape_workday


def scrape_boeing() -> list[dict]:
    return scrape_workday("Boeing", tenant="boeing", wd_instance="wd1", site="External_Careers")
