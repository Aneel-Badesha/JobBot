from scrapers.ats import scrape_workday


def scrape_nxp() -> list[dict]:
    return scrape_workday("NXP", tenant="nxp", wd_instance="wd3", site="careers")
