from scrapers.ats import scrape_workday


def scrape_nvidia() -> list[dict]:
    return scrape_workday("NVIDIA", tenant="nvidia", wd_instance="wd5", site="NVIDIAExternalCareerSite")
