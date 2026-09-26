from scrapers.ats import scrape_workday


def scrape_microchip() -> list[dict]:
    return scrape_workday("Microchip", tenant="microchiphr", wd_instance="wd5", site="External")
