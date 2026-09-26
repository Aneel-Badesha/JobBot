from scrapers.ats import scrape_workday


def scrape_cadence() -> list[dict]:
    return scrape_workday("Cadence", tenant="cadence", wd_instance="wd1", site="External_Careers")
