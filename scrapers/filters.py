import re

# Role keywords — a title must hit at least one of these (word-boundary match).
ROLE_KEYWORDS = [
    # Firmware
    "firmware", "embedded", "bootloader",
    # Hardware / silicon
    "hardware", "silicon", "asic", "fpga", "vlsi", "soc", "rtl", "verification",
    "dft", "physical design", "digital design", "analog design", "mixed-signal",
    "mixed signal", "ic design", "chip", "electrical",
    # Systems / low-level
    "systems", "system software", "kernel", "driver", "drivers", "platform",
    "low-level", "low level", "linux", "bsp",
]

# Level markers — informational only; they do not qualify a title on their own
# (otherwise "Marketing Intern" would pass). Exposed for scrapers that want them.
LEVEL_KEYWORDS = [
    "intern", "co-op", "coop", "internship", "new grad", "new graduate",
    "graduate", "entry", "campus", "early career", "university", "student",
]

SENIORITY_EXCLUSIONS = [
    "senior", "manager", "director",
    "principal", "vp ", "vice president", "head of", "partner",
    "managing", "experienced", "staff", "architect", " ii", " iii", " iv",
]

# Matches "Sr"/"Sr." and "Lead" as standalone words anywhere in the title
_SR_PATTERN = re.compile(r'\bsr\.?\b', re.IGNORECASE)
_LEAD_PATTERN = re.compile(r'\blead\b', re.IGNORECASE)

ROLE_EXCLUSIONS = [
    "sales", "marketing", "hr ", "human resources", "recruit", "account executive",
    "customer success", "technician", "truck", "delivery driver",
]

TARGET_LOCATIONS = [
    # Toronto + suburbs
    "toronto", "north york", "scarborough", "etobicoke", "mississauga",
    "markham", "richmond hill", "vaughan", "brampton", "gta",
    # Montreal + suburbs
    "montreal", "montréal", "laval", "longueuil",
    # Ottawa + suburbs
    "ottawa", "kanata", "nepean", "gatineau",
    # Vancouver + suburbs
    "vancouver", "burnaby", "richmond, bc", "richmond, british columbia",
    "surrey", "coquitlam", "north vancouver",
]


def _kw_pattern(words: list[str]) -> re.Pattern:
    return re.compile(r'\b(?:' + '|'.join(re.escape(w) for w in words) + r')\b', re.IGNORECASE)


_ROLE_RE = _kw_pattern(ROLE_KEYWORDS)
_LOCATION_RE = _kw_pattern(TARGET_LOCATIONS)

# Workday postedOn strings within 48 hours
_RECENT_WORKDAY = {"posted today", "posted yesterday", "posted 1 day ago", "posted 2 days ago"}


def is_target_role(title: str) -> bool:
    t = f" {title.lower()} "
    if any(excl in t for excl in SENIORITY_EXCLUSIONS):
        return False
    if _SR_PATTERN.search(title) or _LEAD_PATTERN.search(title):
        return False
    if any(excl in t for excl in ROLE_EXCLUSIONS):
        return False
    return bool(_ROLE_RE.search(title))


def is_target_location(text: str) -> bool:
    return bool(_LOCATION_RE.search(text or ""))


def is_recent(posted_on: str) -> bool:
    return posted_on.lower().strip() in _RECENT_WORKDAY
