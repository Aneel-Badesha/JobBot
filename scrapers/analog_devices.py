from scrapers.ats import scrape_workday


def scrape_analog_devices() -> list[dict]:
    return scrape_workday("Analog Devices", tenant="analogdevices", wd_instance="wd1", site="External")
