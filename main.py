import logging
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

# Load .env when running locally (no-op if file doesn't exist or python-dotenv not installed)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from scrapers import (
    scrape_alphawave,
    scrape_altera,
    scrape_amazon,
    scrape_amd,
    scrape_analog_devices,
    scrape_arm,
    scrape_astera_labs,
    scrape_broadcom,
    scrape_cadence,
    scrape_cerebras,
    scrape_ciena,
    scrape_cisco,
    scrape_ecobee,
    scrape_ericsson,
    scrape_ford,
    scrape_gm,
    scrape_google,
    scrape_huawei,
    scrape_ibm,
    scrape_infineon,
    scrape_infinera,
    scrape_intel,
    scrape_jetson_ai,
    scrape_l3harris,
    scrape_lightmatter,
    scrape_marvell,
    scrape_meta,
    scrape_microchip,
    scrape_microsoft,
    scrape_nokia,
    scrape_nvidia,
    scrape_nxp,
    scrape_onsemi,
    scrape_photonic,
    scrape_qnx,
    scrape_qualcomm,
    scrape_rambus,
    scrape_ranovus,
    scrape_rivian,
    scrape_samsung,
    scrape_siemens_eda,
    scrape_synopsys,
    scrape_tenstorrent,
    scrape_tesla,
    scrape_ti,
    scrape_untether,
    scrape_viavi,
)
from storage import load_seen_ids, save_seen_ids, filter_new_jobs, add_to_seen, save_jobs_for_site, save_jobs_to_readme, apply_posted_dates
from emailer import send_digest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

SCRAPERS = [
    ("Alphawave Semi", scrape_alphawave),
    ("Altera", scrape_altera),
    ("Amazon", scrape_amazon),
    ("AMD", scrape_amd),
    ("Analog Devices", scrape_analog_devices),
    ("Arm", scrape_arm),
    ("Astera Labs", scrape_astera_labs),
    ("BlackBerry QNX", scrape_qnx),
    ("Broadcom", scrape_broadcom),
    ("Cadence", scrape_cadence),
    ("Cerebras", scrape_cerebras),
    ("Ciena", scrape_ciena),
    ("Cisco", scrape_cisco),
    ("ecobee", scrape_ecobee),
    ("Ericsson", scrape_ericsson),
    ("Ford", scrape_ford),
    ("GM", scrape_gm),
    ("Google", scrape_google),
    ("Huawei", scrape_huawei),
    ("IBM", scrape_ibm),
    ("Infineon", scrape_infineon),
    ("Infinera", scrape_infinera),
    ("Intel", scrape_intel),
    ("Jetson AI", scrape_jetson_ai),
    ("L3Harris", scrape_l3harris),
    ("Lightmatter", scrape_lightmatter),
    ("Marvell", scrape_marvell),
    ("Meta", scrape_meta),
    ("Microchip", scrape_microchip),
    ("Microsoft", scrape_microsoft),
    ("Nokia", scrape_nokia),
    ("NVIDIA", scrape_nvidia),
    ("NXP", scrape_nxp),
    ("onsemi", scrape_onsemi),
    ("Photonic Inc.", scrape_photonic),
    ("Qualcomm", scrape_qualcomm),
    ("Rambus", scrape_rambus),
    ("Ranovus", scrape_ranovus),
    ("Rivian", scrape_rivian),
    ("Samsung", scrape_samsung),
    ("Siemens EDA", scrape_siemens_eda),
    ("Synopsys", scrape_synopsys),
    ("Tenstorrent", scrape_tenstorrent),
    ("Tesla", scrape_tesla),
    ("Texas Instruments", scrape_ti),
    ("Untether AI", scrape_untether),
    ("VIAVI Solutions", scrape_viavi),
]


def run_scraper(name: str, fn) -> list[dict]:
    try:
        results = fn()
        logger.info(f"{name}: {len(results)} relevant jobs found")
        return results
    except Exception as e:
        logger.error(f"{name} failed: {e}", exc_info=True)
        return []


def main():
    seen_ids = load_seen_ids()
    logger.info(f"Loaded {len(seen_ids)} previously seen job IDs")

    all_jobs = []
    for name, fn in SCRAPERS:
        all_jobs += run_scraper(name, fn)

    logger.info(f"Total jobs scraped (before dedup): {len(all_jobs)}")
    all_jobs = apply_posted_dates(all_jobs)

    new_jobs = filter_new_jobs(all_jobs, seen_ids)
    logger.info(f"New jobs (not previously seen): {len(new_jobs)}")

    if new_jobs:
        try:
            send_digest(new_jobs)
        except Exception as e:
            logger.error(f"Failed to send email digest: {e}")
    else:
        logger.info("No new jobs — skipping email")

    updated_seen = add_to_seen(all_jobs, seen_ids)
    save_seen_ids(updated_seen)
    save_jobs_for_site(all_jobs)
    save_jobs_to_readme(all_jobs)
    _push_site()


def _push_site():
    repo = Path(__file__).parent
    try:
        subprocess.run(["git", "add", "docs/jobs.json", "README.md"], cwd=repo, check=True)
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"], cwd=repo
        )
        if result.returncode == 0:
            logger.info("Job listings unchanged — skipping push")
            return
        subprocess.run(
            ["git", "commit", "-m", f"Update jobs.json [{date.today().isoformat()}]"],
            cwd=repo, check=True,
        )
        subprocess.run(["git", "push", "origin", "main"], cwd=repo, check=True)
        logger.info("Pushed job listings to GitHub")
    except Exception as e:
        logger.error(f"Failed to push site update: {e}")


if __name__ == "__main__":
    main()
