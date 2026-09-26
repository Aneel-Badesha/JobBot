# Shift FinancialBot → Hardware/Embedded/Systems Jobs Bot

## Context

This project currently scrapes ~25 Canadian finance/consulting companies (RBC, TD, Deloitte, McKinsey, etc.) for entry-level roles and emails a daily digest. You want to repurpose it for **firmware / embedded / systems** roles at ~46 hardware companies, filtered to **Toronto, Montreal, Ottawa, Vancouver** only, targeting **Fall 2027 4-month co-op** interns AND **2027-start** full-time new grad roles.

### Critical findings from exploring the repo

1. **Local repo is 116 commits behind `origin/main`.** The local checkout is from May 2026 — an old version of the code. The remote has evolved significantly (new `filters.py`, `docs/` job board, Gmail API emailer, `wealthsimple` and `bank_of_america` scrapers, several old scrapers commented out with `# dead URL` / `# blocks scrapers`).

2. **The Raspberry Pi is running the daily job, NOT GitHub Actions.** Daily commits titled `Update jobs.json [YYYY-MM-DD]` are authored by `Aneel-Badesha <abadesha@outlook.com>` (your personal git identity) at 14:34 Pacific time. The origin `main.py` has a `_push_site()` function that commits `docs/jobs.json` and pushes to `origin/main` at the end of each run — that's what your Pi is doing.

3. **GitHub Actions has been failing daily** (that's why you get failure emails). Two reasons: (a) the workflow tries to run `python main.py`, which now uses a Gmail OAuth token file at `~/.config/financialbot/token.json` — that file exists on your Pi but NOT on Ubuntu GitHub Actions runners; (b) `_push_site()` calls `git push` without runner auth configured. **The workflow is redundant and broken. Remove it.**

4. **`docs/index.html` is a public GitHub Pages job board** at `https://aneel-badesha.github.io/FinancialBot/`. It reads `docs/jobs.json` and renders company chips + jobs table. Currently branded "FinancialBot Job Board".

5. **`scrapers/filters.py` already exists** (on origin/main) with `is_target_role()` — a centralized filter. It currently *excludes* interns (via `INTERN_EXCLUSIONS`) which we need to reverse for this pivot.

### Your decisions (confirmed via questions)

- **Old scrapers:** Delete all 24 finance/consulting scrapers, keep only Amazon + Google (they appear in the new list too).
- **Locations:** Toronto, Montreal, Ottawa, Vancouver + common suburbs (Markham, Mississauga, Kanata, Laval, Burnaby, Richmond, etc.). No remote-only, no Waterloo unless it's a suburb of the four.
- **Term filter:** Loose — role keywords + intern/co-op/new grad/graduate. You'll skim the digest.
- **Branding:** Rebrand in-place. Keep folder name `FinancialBot` (git history, GH Pages URL) but change email subject, HTML template, README, and the job-board title.
- **Layout:** One file per company (46 files), even where multiple companies share Workday. Matches the existing convention.
- **Jetson** = Jetson AI (Toronto startup).
- **GitHub Actions:** Remove entirely — RPi handles the automation.

---

## Execution strategy — delegate to cheaper models

The orchestrator (Opus) does only the work that needs judgment or touches shared contracts. The bulk implementation, meaning 44 thin per-company scrapers plus endpoint verification and branding edits, goes to cheaper subagents running in parallel.

### Orchestrator (Opus) — shared foundation, integration, review
1. Rewrite `scrapers/filters.py` (step 2). The role keywords are word-boundary regexes, so `soc` doesn't match "associate" and `chip` doesn't match "chipotle". A level marker alone (intern/new grad) does **not** qualify a title, so "Marketing Intern" is rejected.
2. Create `scrapers/ats.py` with shared fetchers: `scrape_workday`, `scrape_greenhouse`, `scrape_ashby`, `scrape_lever`, `scrape_workable`, `scrape_smartrecruiters`. Each one applies both filters and returns the standard job dict.
   - Workday uses `searchText="Canada"` server-side. NVIDIA drops from 2000 postings to about 8, so a Pi run takes seconds instead of many minutes.
   - Workday resolves "N Locations" postings through the job-detail endpoint.
   - The 48h `is_recent` filter is dropped. `seen_ids` already dedups emails, and interns posted weeks ago still show up on the board.
3. Write the reference wrapper `scrapers/nvidia.py`, which every Workday agent copies.
4. Delete the workflow and the 25 old scrapers (steps 1 and 3).
5. After the agents finish: rebuild `scrapers/__init__.py` and `main.py` (steps 6–7), run the verification steps, and review the diffs.

### Subagents (each gets a disjoint set of files, so there are no conflicts)
| Agent | Model | Scope |
|-------|-------|-------|
| A — Workday | Haiku | 19 Workday wrappers (all except nvidia). Probe each tenant/instance/site with a live POST and fix wrong guesses. Anything that can't be found moves to a custom scraper or is reported as unresolved. |
| B — Simple ATS | Haiku | Greenhouse/Ashby/Lever/Workable/SmartRecruiters companies: cerebras, lightmatter, rambus, rivian, ecobee, photonic, tenstorrent, untether, alphawave, ranovus, jetson_ai. Find which ATS each company actually uses and wrap the matching `ats.py` helper. Best-effort ones log a warning and return `[]`. |
| C — Custom APIs | Sonnet | meta, microsoft, ibm, intel, cisco, tesla, ericsson, huawei, onsemi, microchip, infineon, samsung, ciena. Custom endpoints that need real investigation. Update `amazon.py`/`google.py` to use the shared filters. |
| D — Branding | Haiku | `emailer.py`, `docs/index.html` (title, h1, `COMPANIES` list of 46), `README.md` (steps 8–10). |

Agent rules: use `.venv/Scripts/python` and run every scraper live once. Don't edit `filters.py`, `ats.py`, `__init__.py` or `main.py`, and don't commit. Report each file's endpoint and live job count, plus anything unresolved.

`seen_jobs.json` is gitignored and lives only on the Pi, so step 11 is a Pi-side action.

---

## Prerequisite (you run this first, not part of the code changes)

```
cd C:\Users\Aneel\Documents\Files\Personal\Projects\FinancialBot
git pull origin main
```

Bring local up to date with the 116 remote commits before we edit anything. Otherwise every edit will conflict.

---

## Changes

### 1. Delete GitHub Actions workflow

**File:** `.github/workflows/scrape.yml` — delete.

This stops the daily failure emails. Your Pi already does the work.

### 2. Rewrite `scrapers/filters.py`

Replace the finance-oriented filter with a hardware/embedded/systems-oriented one.

- **New `INCLUDE_KEYWORDS`** (title matching):
  - Firmware: `firmware`, `embedded`, `bootloader`
  - Hardware/silicon: `hardware`, `silicon`, `asic`, `fpga`, `vlsi`, `soc`, `rtl`, `verification`, `dft`, `physical design`, `digital design`, `analog design`, `mixed-signal`, `ic design`, `chip`
  - Systems/low-level: `systems`, `kernel`, `driver`, `platform`, `low-level`, `linux`
  - Level markers: `intern`, `co-op`, `coop`, `internship`, `new grad`, `new graduate`, `graduate`, `entry`, `campus`, `early career`
- **Remove `INTERN_EXCLUSIONS`** entirely (we WANT interns).
- **Keep `SENIORITY_EXCLUSIONS`** (senior/lead/principal/etc.) — still relevant.
- **Adjust `ROLE_EXCLUSIONS`** — drop finance-specific ones (teller, cashier, mortgage advisor). Add hardware-adjacent noise if any (e.g., `sales`, `marketing`, `hr `).
- **Add `TARGET_LOCATIONS`** module-level constant + `is_target_location(text) -> bool`:
  ```
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
  ```
  Note: `richmond` alone is ambiguous (Richmond Hill ON vs Richmond BC) so match on the qualified form.
- **`is_target_role(title)`** logic: pass if any INCLUDE keyword hits AND no seniority/role exclusion. Interns and co-ops are now allowed through.
- Every new scraper imports `is_target_role` and `is_target_location` from this module. This is the one place to tune filters going forward.

### 3. Delete finance-only scrapers

Delete from `scrapers/`:
```
atb.py, bain.py, bank_of_america.py, bcg.py, bell.py, bnpparibas.py,
canada_life.py, deloitte.py, ey.py, fairfax.py, grant_thornton.py,
hsbc.py, jpmorgan.py, kpmg.py, mckinsey.py, mnp.py, national_bank.py,
oliver_wyman.py, pwc.py, rogers.py, scotiabank.py, shopify.py,
sobeys.py, wealthsimple.py, workday.py
```

That's 25 files. Keep `amazon.py`, `google.py`, `filters.py`, `__init__.py`.

### 4. Update `amazon.py` and `google.py`

Both currently filter Canada-wide. Update:
- Import `is_target_role` and `is_target_location` from `scrapers.filters`.
- Replace inline `_is_entry_level` / location-inference with the shared filters.
- Amazon: change query param `loc_query` from `"Canada"` to a broader term or leave as Canada then filter by `is_target_location` on the returned `normalized_location`. Same idea for Google.

### 5. Add 44 new scrapers — one file per company

Convention for every new scraper:
```python
from scrapers.filters import is_target_role, is_target_location

def scrape_<company>() -> list[dict]:
    # returns list of {id, company, title, location, link, posted}
```

Group by ATS platform (all files are still one-per-company, but they follow the same platform pattern). **ATS URLs listed below are best-guess starting points — verify each during implementation by opening the company's careers page.**

#### Workday ATS (pattern: `https://{tenant}.{wd_instance}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs`)

Reuse the POST-JSON pagination pattern from the old `workday.py`. Each file only needs `tenant`, `wd_instance`, `site` constants.

| Company | Tenant guess | Instance guess | Site guess |
|---------|--------------|----------------|------------|
| AMD | `amd` | `wd1` | `External` |
| NVIDIA | `nvidia` | `wd5` | `NVIDIAExternalCareerSite` |
| Qualcomm | `qualcomm` | `wd5` | `External` |
| Broadcom | `broadcom` | `wd1` | `External_Career_Site` |
| Marvell | `marvell` | `wd1` | `MarvellCareers2` |
| NXP | `nxp` | `wd3` | `careers` |
| Texas Instruments | `ti` | `wd1` | (verify) |
| Analog Devices | `analog` | `wd1` | (verify) |
| Arm | `arm` | `wd3` | `Arm_RM` |
| GM | `gm` | `wd5` | `Careers_GM` |
| Ford | `ford` | `wd5` | `FordCareers` |
| Nokia | `nokia` | `wd3` | `careers` |
| Infinera | `infinera` | `wd1` | (verify) |
| VIAVI Solutions | `viavi` | `wd1` | (verify) |
| L3Harris | `l3harris` | `wd1` | `L3Harris_Careers` |
| Cadence | `cadence` | `wd1` | `External_Careers` |
| Synopsys | `synopsys` | `wd1` | `Synopsys_Careers` |
| Siemens EDA | `siemens` | `wd3` | `siemens` (parent Siemens) |
| BlackBerry (QNX) | `blackberry` | `wd3` | `BlackBerry` |
| Altera | (verify — post-spinoff) | | |

Files: `amd.py`, `nvidia.py`, `qualcomm.py`, `broadcom.py`, `marvell.py`, `nxp.py`, `ti.py`, `analog_devices.py`, `arm.py`, `gm.py`, `ford.py`, `nokia.py`, `infinera.py`, `viavi.py`, `l3harris.py`, `cadence.py`, `synopsys.py`, `siemens_eda.py`, `qnx.py`, `altera.py`.

#### Greenhouse ATS (pattern: `https://boards-api.greenhouse.io/v1/boards/{slug}/jobs`)

Standard GET, no pagination for most boards. Each file: `slug` constant + fetch + filter.

| Company | Board slug guess |
|---------|------------------|
| Cerebras | `cerebras` |
| Lightmatter | `lightmatter` |
| Rambus | `rambus` |
| Rivian | `rivian` |
| ecobee | `ecobee` |
| Photonic Inc. | `photonic` (verify) |

Files: `cerebras.py`, `lightmatter.py`, `rambus.py`, `rivian.py`, `ecobee.py`, `photonic.py`.

#### iCIMS / SuccessFactors / other named ATS

| Company | Likely ATS | Notes |
|---------|-----------|-------|
| onsemi | iCIMS | `careers.onsemi.com` |
| Microchip | iCIMS | `careers.microchip.com` |
| Infineon | SAP SuccessFactors | `jobs.infineon.com` |
| Samsung | SuccessFactors | `sec.wd3.myworkdayjobs.com` (verify — some Samsung units on Workday) |
| Ciena | iCIMS/custom | `www.ciena.com/about/careers` |

Files: `onsemi.py`, `microchip.py`, `infineon.py`, `samsung.py`, `ciena.py`.

#### Ashby ATS

| Company | Board slug guess |
|---------|------------------|
| Tenstorrent | `tenstorrent` on `jobs.ashbyhq.com` |

File: `tenstorrent.py`.

#### Big-tech / custom career-site APIs

| Company | Endpoint |
|---------|----------|
| Meta | `metacareers.com` GraphQL |
| Microsoft | `careers.microsoft.com/professionals/us/en/search-results` JSON |
| IBM | `careers.ibm.com` JSON search |
| Intel | `jobs.intel.com` JSON search |
| Cisco | `jobs.cisco.com` JSON search |
| Tesla | `www.tesla.com/en_CA/careers/search` JSON |
| Ericsson | `jobs.ericsson.com` custom |
| Huawei Canada | `career.huawei.com` custom |

Files: `meta.py`, `microsoft.py`, `ibm.py`, `intel.py`, `cisco.py`, `tesla.py`, `ericsson.py`, `huawei.py`. Each is a custom scraper — investigate the site's Network tab or existing scraping references.

#### Small companies (LinkedIn / Workable / custom)

Small firms often use LinkedIn or a small ATS. Options: LinkedIn scraping (fragile — may need selenium), Workable public API (`apply.workable.com/api/v3/accounts/{slug}/jobs`), or a light HTML scraper.

| Company | Suggested approach |
|---------|-------------------|
| Untether AI | LinkedIn or Workable |
| Alphawave Semi | Custom (`alphawaveipexcess.com/careers`) |
| Ranovus | LinkedIn or custom (Ottawa-based; small) |
| Jetson AI | LinkedIn — Toronto startup, small |

Files: `untether.py`, `alphawave.py`, `ranovus.py`, `jetson_ai.py`. Mark these as "best-effort" — if they can't be scraped reliably, log a warning and continue.

### 6. Update `scrapers/__init__.py`

Rebuild the imports and `__all__` list to match the new scraper files. Alphabetical or ATS-grouped, whichever you prefer.

### 7. Update `main.py`

- Replace the `SCRAPERS` list with the new 46 companies (labels + functions).
- Remove all commented-out old scrapers.
- Keep the `_push_site()` function — it's what the RPi uses.
- Keep the log line format.

### 8. Update `emailer.py`

- Line 68: change `msg["Subject"] = f"Finance Jobs Digest — ..."` → `f"Hardware Jobs Digest — ..."` (or your preferred name).
- Line 84 (`_build_plain`): change `"New finance jobs in Canada"` → `"New hardware/embedded jobs"`.
- Line 108 (`_build_html`): change `"New Finance Jobs in Canada"` heading → `"New Hardware Jobs"`.
- Line 126 (footer): update text `"Jobs filtered for Canada + entry-level keywords"` → `"Jobs filtered for Toronto/Montreal/Ottawa/Vancouver + firmware/embedded/systems keywords"`.
- Line 127: leave the `https://aneel-badesha.github.io/FinancialBot` link (URL doesn't change).
- Optional: swap accent color `#c8102e` (RBC red) to something less finance-y. Not required.

### 9. Update `docs/index.html`

- Line 6: `<title>FinancialBot Job Board</title>` → `<title>Hardware Jobs Board</title>` (or your name).
- Line 160: `<h1>Financial<span>Bot</span> Job Board</h1>` → new heading.
- Lines 182–ish: `COMPANIES` array — replace the current 30 finance companies with the 46 new hardware companies + their careers-page URLs.

### 10. Update `README.md`

Current content:
```
# FinancialBot
Bot that sends finance jobs to me via email
```
Replace with a short blurb about hardware/embedded jobs and a note about the Pi automation.

### 11. Delete `seen_jobs.json` contents

Optional but recommended — clear the seen-ids file so the first run of the new scrapers emails you everything it finds fresh:
```json
{"seen_ids": []}
```

### 12. RPi — you handle after the code lands

On the Raspberry Pi:
1. `git pull origin main` to pick up the new code.
2. `pip install -r requirements.txt` (no new deps expected).
3. Test manually: `python main.py`.
4. The daily cron/systemd unit stays as-is.

---

## Critical files touched (summary)

- `.github/workflows/scrape.yml` — **delete**
- `scrapers/filters.py` — rewrite keywords, add `is_target_location`
- `scrapers/__init__.py` — rebuild imports
- `scrapers/{25 old files}` — **delete**
- `scrapers/amazon.py`, `scrapers/google.py` — update to use shared filters
- `scrapers/{44 new files}` — **create**
- `main.py` — new `SCRAPERS` list
- `emailer.py` — subject + HTML branding
- `docs/index.html` — title + `COMPANIES` list
- `README.md` — new blurb
- `seen_jobs.json` — reset to empty (optional)

## Reused code / utilities

- `scrapers/filters.py::is_target_role` — extend it, don't duplicate keyword logic per scraper.
- The Workday POST-JSON pagination pattern from the old `scrapers/workday.py` — each new Workday-based scraper is a thin wrapper.
- The Greenhouse GET pattern — one function template covers all Greenhouse boards.
- `storage.py::save_jobs_for_site` — unchanged, still writes `docs/jobs.json`.
- `main.py::_push_site` — unchanged, still commits `docs/jobs.json` and pushes.

## Verification

1. **Filter unit sanity check**: In a Python shell:
   ```
   from scrapers.filters import is_target_role, is_target_location
   assert is_target_role("Firmware Engineer, New Grad")
   assert is_target_role("Embedded Software Co-op (Fall 2027)")
   assert not is_target_role("Senior Firmware Engineer")
   assert not is_target_role("Financial Analyst")
   assert is_target_location("Markham, ON, Canada")
   assert is_target_location("Montréal, QC")
   assert not is_target_location("Waterloo, ON")
   ```
2. **Run one scraper in isolation**: e.g. `python -c "from scrapers.nvidia import scrape_nvidia; print(scrape_nvidia())"` and inspect the output.
3. **Full local dry-run**: `python main.py` from the project root. Should log per-scraper counts, write `docs/jobs.json`, and either send an email or log "No new jobs — skipping email".
4. **Verify each ATS URL** before shipping a scraper — many of the tenant/site guesses above are educated guesses. If a company's page 404s the API, open the careers page in a browser and inspect the Network tab to find the correct endpoint.
5. **Post-deploy on Pi**: `git pull` on the Pi, run `python main.py` manually once, confirm the digest arrives and `docs/jobs.json` updates the GitHub Pages board within a minute of push.
6. **Confirm GitHub Actions failure emails stop** after the workflow file is deleted (next scheduled run at 13:00 UTC won't happen).

---

## Implementation status (2026-09-26)

Built as planned: the orchestrator wrote the shared pieces, and subagents wrote the scrapers (Haiku for Workday, simple job boards and branding; Sonnet for custom APIs). The Haiku Workday agent resolved only 6 of 19, so a Sonnet follow-up agent redid the other 13 plus Rambus and Rivian.

The dry run found **120 matching jobs across 46 scrapers in about 110s**, with no exceptions except a transient Microsoft 429.

Many guesses in the plan were wrong; these are the real endpoints:
- **Oracle Recruiting Cloud:** TI, Ford, Nokia, onsemi.
- **Jibe:** AMD and Rivian (`/api/jobs?country=Canada`).
- **Eightfold:** Microsoft, Ericsson, Infineon.
- **TalentBrew HTML:** Arm, L3Harris (first page only).
- **Avature:** Synopsys, Siemens EDA.
- **Recruitee:** Huawei Canada.
- **Workday on a different tenant:** ecobee (on Generac's board), GM (`generalmotors`), QNX (`bb`/`QNX`), Microchip (`microchiphr`), Analog Devices (`analogdevices`), VIAVI (`viavisolutions`).
- **Greenhouse instead of Ashby:** Tenstorrent. Cerebras is on Ashby.

**Best-effort (these log a warning and return `[]`):**
- Meta: needs a rotating GraphQL `doc_id`.
- IBM: no JSON API found.
- Cisco: Phenom API needs an OAuth token.
- Tesla, Rambus, Photonic: blocked by Akamai/Cloudflare.
- Ranovus: LinkedIn only.
- Untether AI: team acquired by AMD in 2025.
- Alphawave Semi: acquired by Qualcomm.
- Jetson AI: no ATS found.
