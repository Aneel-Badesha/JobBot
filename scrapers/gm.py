from scrapers.ats import scrape_workday


def scrape_gm() -> list[dict]:
    return scrape_workday("GM", tenant="generalmotors", wd_instance="wd5", site="Careers_GM")
