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
    scrape_agility_robotics,
    scrape_alphawave,
    scrape_altera,
    scrape_amazon,
    scrape_amd,
    scrape_analog_devices,
    scrape_anduril,
    scrape_applied_materials,
    scrape_apptronik,
    scrape_arm,
    scrape_astera_labs,
    scrape_astranis,
    scrape_boeing,
    scrape_broadcom,
    scrape_cadence,
    scrape_cerebras,
    scrape_ciena,
    scrape_cisco,
    scrape_d_matrix,
    scrape_divergent,
    scrape_ecobee,
    scrape_ericsson,
    scrape_etched,
    scrape_fab2,
    scrape_figure_ai,
    scrape_ford,
    scrape_gm,
    scrape_google,
    scrape_hermeus,
    scrape_huawei,
    scrape_ibm,
    scrape_infineon,
    scrape_infinera,
    scrape_intel,
    scrape_ionq,
    scrape_jetson_ai,
    scrape_kla,
    scrape_kodiak,
    scrape_l3harris,
    scrape_lightmatter,
    scrape_lucid,
    scrape_marvell,
    scrape_mda_space,
    scrape_meta,
    scrape_microchip,
    scrape_micron,
    scrape_microsoft,
    scrape_motional,
    scrape_neuralink,
    scrape_nokia,
    scrape_nuro,
    scrape_nvidia,
    scrape_nxp,
    scrape_one_x,
    scrape_onsemi,
    scrape_photonic,
    scrape_psiquantum,
    scrape_qnx,
    scrape_qualcomm,
    scrape_rambus,
    scrape_ranovus,
    scrape_relativity_space,
    scrape_rivian,
    scrape_rocket_lab,
    scrape_sambanova,
    scrape_samsung,
    scrape_saronic,
    scrape_scout_motors,
    scrape_shield_ai,
    scrape_siemens_eda,
    scrape_skydio,
    scrape_spacex,
    scrape_synopsys,
    scrape_tenstorrent,
    scrape_tesla,
    scrape_ti,
    scrape_torc,
    scrape_untether,
    scrape_viavi,
    scrape_waabi,
    scrape_waymo,
    scrape_zoox,
)
from storage import load_seen_ids, save_seen_ids, filter_new_jobs, add_to_seen, save_jobs_for_site, save_jobs_to_readme, apply_posted_dates
from emailer import send_digest
from scrapers.filters import is_target_job

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

SCRAPERS = [
    ("1X", scrape_one_x),
    ("Agility Robotics", scrape_agility_robotics),
    ("Alphawave Semi", scrape_alphawave),
    ("Altera", scrape_altera),
    ("Amazon", scrape_amazon),
    ("AMD", scrape_amd),
    ("Analog Devices", scrape_analog_devices),
    ("Anduril", scrape_anduril),
    ("Applied Materials", scrape_applied_materials),
    ("Apptronik", scrape_apptronik),
    ("Arm", scrape_arm),
    ("Astera Labs", scrape_astera_labs),
    ("Astranis", scrape_astranis),
    ("BlackBerry QNX", scrape_qnx),
    ("Boeing", scrape_boeing),
    ("Broadcom", scrape_broadcom),
    ("Cadence", scrape_cadence),
    ("Cerebras", scrape_cerebras),
    ("Ciena", scrape_ciena),
    ("Cisco", scrape_cisco),
    ("d-Matrix", scrape_d_matrix),
    ("Divergent", scrape_divergent),
    ("ecobee", scrape_ecobee),
    ("Ericsson", scrape_ericsson),
    ("Etched", scrape_etched),
    ("Fab2", scrape_fab2),
    ("Figure AI", scrape_figure_ai),
    ("Ford", scrape_ford),
    ("GM", scrape_gm),
    ("Google", scrape_google),
    ("Hermeus", scrape_hermeus),
    ("Huawei", scrape_huawei),
    ("IBM", scrape_ibm),
    ("Infineon", scrape_infineon),
    ("Infinera", scrape_infinera),
    ("Intel", scrape_intel),
    ("IonQ", scrape_ionq),
    ("Jetson AI", scrape_jetson_ai),
    ("KLA", scrape_kla),
    ("Kodiak Robotics", scrape_kodiak),
    ("L3Harris", scrape_l3harris),
    ("Lightmatter", scrape_lightmatter),
    ("Lucid Motors", scrape_lucid),
    ("Marvell", scrape_marvell),
    ("MDA Space", scrape_mda_space),
    ("Meta", scrape_meta),
    ("Microchip", scrape_microchip),
    ("Micron", scrape_micron),
    ("Microsoft", scrape_microsoft),
    ("Motional", scrape_motional),
    ("Neuralink", scrape_neuralink),
    ("Nokia", scrape_nokia),
    ("Nuro", scrape_nuro),
    ("NVIDIA", scrape_nvidia),
    ("NXP", scrape_nxp),
    ("onsemi", scrape_onsemi),
    ("Photonic Inc.", scrape_photonic),
    ("PsiQuantum", scrape_psiquantum),
    ("Qualcomm", scrape_qualcomm),
    ("Rambus", scrape_rambus),
    ("Ranovus", scrape_ranovus),
    ("Relativity Space", scrape_relativity_space),
    ("Rivian", scrape_rivian),
    ("Rocket Lab", scrape_rocket_lab),
    ("SambaNova", scrape_sambanova),
    ("Samsung", scrape_samsung),
    ("Saronic", scrape_saronic),
    ("Scout Motors", scrape_scout_motors),
    ("Shield AI", scrape_shield_ai),
    ("Siemens EDA", scrape_siemens_eda),
    ("Skydio", scrape_skydio),
    ("SpaceX", scrape_spacex),
    ("Synopsys", scrape_synopsys),
    ("Tenstorrent", scrape_tenstorrent),
    ("Tesla", scrape_tesla),
    ("Texas Instruments", scrape_ti),
    ("Torc Robotics", scrape_torc),
    ("Untether AI", scrape_untether),
    ("VIAVI Solutions", scrape_viavi),
    ("Waabi", scrape_waabi),
    ("Waymo", scrape_waymo),
    ("Zoox", scrape_zoox),
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

    # Scrapers gate on role and location separately; the US interns-only rule
    # needs both, so it is applied once here.
    all_jobs = [j for j in all_jobs if is_target_job(j["title"], j["location"])]
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
