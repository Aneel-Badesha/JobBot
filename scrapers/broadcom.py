from scrapers.ats import scrape_workday


def scrape_broadcom() -> list[dict]:
    return scrape_workday("Broadcom", tenant="broadcom", wd_instance="wd1", site="External_Career")
