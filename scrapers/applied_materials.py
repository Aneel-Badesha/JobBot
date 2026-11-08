from scrapers.ats import scrape_workday


def scrape_applied_materials() -> list[dict]:
    return scrape_workday("Applied Materials", tenant="amat", wd_instance="wd1", site="External")
