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
    # Robotics / electronics
    "robotics", "electronics",
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

# Canadian cities: any target role (intern, co-op, new grad).
TARGET_LOCATIONS = [
    # Toronto + suburbs
    "toronto", "north york", "scarborough", "etobicoke", "mississauga",
    "markham", "richmond hill", "vaughan", "brampton", "gta",
    # Montreal + suburbs
    "montreal", "montréal", "laval", "longueuil", "sainte-anne-de-bellevue",
    # Ottawa + suburbs
    "ottawa", "kanata", "nepean", "gatineau",
    # Vancouver + suburbs
    "vancouver", "burnaby", "richmond, bc", "richmond, british columbia",
    "surrey", "coquitlam", "north vancouver",
]


def _kw_pattern(words: list[str]) -> re.Pattern:
    return re.compile(r'\b(?:' + '|'.join(re.escape(w) for w in words) + r')\b', re.IGNORECASE)


# United States: anywhere, but internships/co-ops only (see is_target_job).
US_STATES = [
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
    "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
    "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine",
    "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
    "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey",
    "new mexico", "new york", "north carolina", "north dakota", "ohio",
    "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina",
    "south dakota", "tennessee", "texas", "utah", "vermont", "virginia",
    "washington", "west virginia", "wisconsin", "wyoming", "district of columbia",
]
# Startup boards often list a bare city ("Austin", "San Francisco Office").
US_CITIES = [
    "san francisco", "san jose", "santa clara", "sunnyvale", "mountain view",
    "palo alto", "menlo park", "foster city", "san mateo", "san carlos",
    "redwood city", "fremont", "milpitas", "cupertino", "los angeles",
    "long beach", "hawthorne", "torrance", "el segundo", "irvine", "san diego",
    "seattle", "redmond", "bellevue, wa", "austin", "dallas", "houston",
    "boston", "new york", "pittsburgh", "detroit", "ann arbor", "chicago",
    "denver", "boulder", "atlanta", "phoenix", "salt lake city", "portland",
]
# Two-letter codes, matched case-sensitively as "City, ST". IL/IN/DE are left
# out — they collide with Israel/India/Germany country codes on many boards.
US_STATE_CODES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "FL", "GA", "HI", "ID", "IA",
    "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",
    "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
    "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC",
]

_ROLE_RE = _kw_pattern(ROLE_KEYWORDS)
_LOCATION_RE = _kw_pattern(TARGET_LOCATIONS)
_US_NAME_RE = re.compile(
    r'\b(?:united states|usa|u\.s\.a?\.?|' + '|'.join(US_STATES + US_CITIES) + r')\b', re.IGNORECASE)
_US_MARKER_RE = re.compile(r'\bUS\b')
_US_CODE_RE = re.compile(r',\s*(?:' + '|'.join(US_STATE_CODES) + r')\b')
_NOT_US_RE = re.compile(r'\bcanada\b', re.IGNORECASE)

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


def is_canada_location(text: str) -> bool:
    return bool(_LOCATION_RE.search(text or ""))


def is_us_location(text: str) -> bool:
    for seg in re.split(r'[;|]', text or ""):
        if _NOT_US_RE.search(seg):
            continue
        if _US_NAME_RE.search(seg) or _US_MARKER_RE.search(seg) or _US_CODE_RE.search(seg):
            return True
    return False


def is_target_location(text: str) -> bool:
    """Coarse location gate used inside scrapers; is_target_job applies the
    US interns-only rule once the title is known."""
    return is_canada_location(text) or is_us_location(text)


def is_recent(posted_on: str) -> bool:
    return posted_on.lower().strip() in _RECENT_WORKDAY


_INTERN_RE = _kw_pattern(["intern", "interns", "internship", "co-op", "coop", "student", "stage", "stagiaire"])


def is_intern(title: str) -> bool:
    """Intern/co-op postings (vs. full-time) — used to split the README tables."""
    return bool(_INTERN_RE.search(title))


def is_target_job(title: str, location: str) -> bool:
    """Target role in a Canadian target city, or a target internship in the US."""
    if not is_target_role(title):
        return False
    if is_canada_location(location):
        return True
    return is_us_location(location) and is_intern(title)


_TERM_RE = re.compile(r'\b(spring|summer|fall|autumn|winter)[\s\-/]*(20\d\d)\b|\b(20\d\d)[\s\-/]*(spring|summer|fall|autumn|winter)\b',
                      re.IGNORECASE)
_GRAD_RE = re.compile(r"\b(?:ph\.?\s?d|doctoral|master'?s?|ms)\b", re.IGNORECASE)
_BACHELOR_RE = re.compile(r"\b(?:bachelor'?s?|undergrad(?:uate)?|bs)\b", re.IGNORECASE)
_CITIZEN_RE = re.compile(r"\b(?:u\.?s\.? citizen|united states citizen|u\.?s\.? person|security clearance|itar)\b",
                         re.IGNORECASE)
_NO_SPONSOR_RE = re.compile(r"\b(?:not|unable to|cannot|can't|won't|no)\s+(?:\w+\s+){0,3}sponsor|"
                            r"\bwithout\s+(?:\w+\s+){0,2}sponsorship", re.IGNORECASE)


def title_terms(title: str) -> list[str]:
    """Terms named in a title, e.g. "Summer 2027"."""
    out = []
    for season, year, year2, season2 in _TERM_RE.findall(title or ""):
        season = (season or season2).capitalize().replace("Autumn", "Fall")
        term = f"{season} {year or year2}"
        if term not in out:
            out.append(term)
    return out


def is_grad_title(title: str) -> bool:
    """Title asks for a graduate degree and doesn't also accept undergrads."""
    return bool(_GRAD_RE.search(title or "")) and not _BACHELOR_RE.search(title or "")


def work_auth_flag(text: str) -> str:
    """Scan posting text: "citizen", "no_sponsorship", or "" if nothing is stated."""
    if _CITIZEN_RE.search(text or ""):
        return "citizen"
    if _NO_SPONSOR_RE.search(text or ""):
        return "no_sponsorship"
    return ""
