from scrapers.ats import scrape_greenhouse


def scrape_apptronik() -> list[dict]:
    return scrape_greenhouse("Apptronik", slug="apptronik")
