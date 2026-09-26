from scrapers.ats import scrape_workday


def scrape_qualcomm() -> list[dict]:
    return scrape_workday("Qualcomm", tenant="qualcomm", wd_instance="wd12", site="External")
