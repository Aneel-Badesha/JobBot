from scrapers.ats import scrape_workday


def scrape_marvell() -> list[dict]:
    return scrape_workday("Marvell", tenant="marvell", wd_instance="wd1", site="MarvellCareers2")
