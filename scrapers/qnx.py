from scrapers.ats import scrape_workday


def scrape_qnx() -> list[dict]:
    # BlackBerry QNX posts on BlackBerry's Workday tenant, dedicated "QNX" site.
    return scrape_workday("BlackBerry QNX", tenant="bb", wd_instance="wd3", site="QNX", search_text="")
