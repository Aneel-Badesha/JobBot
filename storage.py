import json
import logging
import os
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from scrapers.filters import is_intern

logger = logging.getLogger(__name__)
SEEN_JOBS_FILE = Path(__file__).parent / "seen_jobs.json"


def load_seen_ids() -> set[str]:
    if not SEEN_JOBS_FILE.exists():
        return set()
    try:
        with SEEN_JOBS_FILE.open() as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        logger.warning(f"Could not read {SEEN_JOBS_FILE} ({e}); treating as empty")
        return set()
    return set(data.get("seen_ids", []))


def save_seen_ids(seen_ids: set[str]) -> None:
    tmp = SEEN_JOBS_FILE.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump({"seen_ids": sorted(seen_ids)}, f, indent=2)
        f.flush()
        os.fsync(f.fileno())
    tmp.replace(SEEN_JOBS_FILE)
    logger.info(f"Saved {len(seen_ids)} seen job IDs")


def filter_new_jobs(jobs: list[dict], seen_ids: set[str]) -> list[dict]:
    return [j for j in jobs if j["id"] not in seen_ids]


def add_to_seen(jobs: list[dict], seen_ids: set[str]) -> set[str]:
    return seen_ids | {j["id"] for j in jobs}


JOBS_SITE_FILE = Path(__file__).parent / "docs" / "jobs.json"


def save_jobs_for_site(jobs: list[dict]) -> None:
    JOBS_SITE_FILE.parent.mkdir(exist_ok=True)
    with JOBS_SITE_FILE.open("w") as f:
        json.dump({
            "updated": datetime.now(timezone.utc).isoformat(),
            "jobs": jobs,
        }, f, indent=2)
    logger.info(f"Saved {len(jobs)} jobs to {JOBS_SITE_FILE}")


README_FILE = Path(__file__).parent / "README.md"
_TABLE_START = "<!-- JOBS:START -->"
_TABLE_END = "<!-- JOBS:END -->"


def split_jobs(jobs: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split into (interns/co-ops, full-time), each sorted newest first then by company/title.
    Shared by the README tables and the email digest so both look the same."""
    def ordered(rows: list[dict]) -> list[dict]:
        rows = sorted(rows, key=lambda j: (j["company"].lower(), j["title"].lower()))
        return sorted(rows, key=lambda j: j.get("posted", ""), reverse=True)

    return (ordered([j for j in jobs if is_intern(j["title"])]),
            ordered([j for j in jobs if not is_intern(j["title"])]))


def save_jobs_to_readme(jobs: list[dict]) -> None:
    """Rewrite the jobs tables between the JOBS markers in README.md (appended if missing)."""
    def cell(text: str) -> str:
        return str(text).replace("|", r"\|").replace("\n", " ").strip()

    def table(rows: list[dict]) -> list[str]:
        if not rows:
            return ["_None right now._"]
        out = ["| Posted | Company | Role | Location |", "|--------|---------|------|----------|"]
        out += [f"| {cell(j.get('posted', ''))} | {cell(j['company'])} | [{cell(j['title'])}]({j['link']}) | {cell(j['location'])} |"
                for j in rows]
        return out

    interns, full_time = split_jobs(jobs)
    lines = [
        _TABLE_START,
        f"_Updated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} — {len(jobs)} jobs posted in the last {MAX_AGE_DAYS} days_",
        "",
        f"### Internships & Co-ops ({len(interns)})",
        "",
        *table(interns),
        "",
        f"### Full-time ({len(full_time)})",
        "",
        *table(full_time),
        _TABLE_END,
    ]
    block = "\n".join(lines)

    text = README_FILE.read_text(encoding="utf-8") if README_FILE.exists() else ""
    if _TABLE_START in text and _TABLE_END in text:
        before = text.split(_TABLE_START, 1)[0]
        after = text.split(_TABLE_END, 1)[1]
        text = before + block + after
    else:
        text = text.rstrip() + "\n\n## Current jobs\n\n" + block + "\n"
    README_FILE.write_text(text, encoding="utf-8")
    logger.info(f"Wrote {len(interns)} intern + {len(full_time)} full-time jobs to {README_FILE.name}")


# --- Posted dates ------------------------------------------------------------

MAX_AGE_DAYS = 14
FIRST_SEEN_FILE = Path(__file__).parent / "first_seen.json"

_RELATIVE_RE = re.compile(r"posted\s+(\d+)\+?\s+days?\s+ago", re.IGNORECASE)


def parse_posted(raw, today: date) -> date | None:
    """Normalize the many ATS 'posted' formats to a date. Returns None if unknown."""
    if raw in (None, ""):
        return None
    if isinstance(raw, (int, float)) or (isinstance(raw, str) and raw.isdigit() and len(raw) >= 12):
        return datetime.fromtimestamp(int(raw) / 1000, tz=timezone.utc).date()  # epoch ms (Lever)
    text = str(raw).strip()
    low = text.lower()
    if low in ("posted today", "today", "just posted"):
        return today
    if low in ("posted yesterday", "yesterday"):
        return today - timedelta(days=1)
    m = _RELATIVE_RE.search(text)
    if m:
        return today - timedelta(days=int(m.group(1)))
    m = re.match(r"(\d{4}-\d{2}-\d{2})", text)  # ISO date / datetime prefix
    if m:
        return date.fromisoformat(m.group(1))
    try:
        return datetime.strptime(" ".join(text.split()), "%B %d, %Y").date()  # "September 2, 2026"
    except ValueError:
        return None


def apply_posted_dates(jobs: list[dict], today: date | None = None) -> list[dict]:
    """Set each job's 'posted' to an ISO date and drop jobs older than MAX_AGE_DAYS.

    Jobs whose ATS gives no usable date fall back to the date we first saw them,
    tracked in first_seen.json (kept separately so an aged-out job doesn't come back).
    """
    today = today or date.today()
    first_seen = {}
    if FIRST_SEEN_FILE.exists():
        try:
            first_seen = json.loads(FIRST_SEEN_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            logger.warning(f"Could not read {FIRST_SEEN_FILE} ({e}); treating as empty")

    cutoff = today - timedelta(days=MAX_AGE_DAYS)
    kept = []
    current_first_seen = {}
    for job in jobs:
        posted = parse_posted(job.get("posted"), today)
        if posted is None:
            seen_on = first_seen.get(job["id"], today.isoformat())
            current_first_seen[job["id"]] = seen_on
            posted = date.fromisoformat(seen_on)
        if posted < cutoff:
            continue
        kept.append({**job, "posted": posted.isoformat()})

    # Only keep entries for jobs still listed, so the file doesn't grow forever
    FIRST_SEEN_FILE.write_text(json.dumps(current_first_seen, indent=2, sort_keys=True), encoding="utf-8")
    logger.info(f"Dropped {len(jobs) - len(kept)} jobs posted more than {MAX_AGE_DAYS} days ago")
    return kept
