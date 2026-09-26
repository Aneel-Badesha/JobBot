from scrapers.ats import scrape_workday


def scrape_viavi() -> list[dict]:
    return scrape_workday("VIAVI Solutions", tenant="viavisolutions", wd_instance="wd1", site="careers")
