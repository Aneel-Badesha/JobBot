from scrapers.ats import scrape_workday


def scrape_ecobee() -> list[dict]:
    # ecobee is owned by Generac and posts on Generac's Workday board
    return scrape_workday("ecobee", tenant="generac", wd_instance="wd5", site="External", search_text="ecobee")
