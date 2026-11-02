from scrapers.ats import scrape_ultipro


def scrape_mda_space() -> list[dict]:
    return scrape_ultipro("MDA Space", host="recruiting.ultipro.ca", tenant="MAC5000MCDW",
                          boards=["664818ff-3594-4bec-9f30-3394e59e19f3",   # main (Canada)
                                  "832d1816-e4c1-444e-9dc4-ef655be91245"])  # US
