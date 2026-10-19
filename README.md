# JobBot

A job scraper and Gmail digest bot for hardware/firmware/embedded systems roles. Scrapes ~47 hardware and semiconductor companies for firmware, embedded, hardware, and systems engineer internships, co-ops, and new-grad roles in Toronto, Montreal, Ottawa, and Vancouver. Emails a daily digest and keeps the table below up to date.

**Features:**
- Scrapes ~47 hardware/semiconductor companies
- Filters for firmware/embedded/hardware/systems roles in target cities (Toronto, Montreal, Ottawa, Vancouver)
- Sends daily Gmail digest with new postings
- Rewrites the jobs table at the bottom of this README on every run
- Runs daily on Raspberry Pi (no GitHub Actions)

**To run locally:**
```bash
pip install -r requirements.txt
python main.py
```

**Configuration:**
- Job filters live in `scrapers/filters.py`
- Shared ATS fetchers in `scrapers/ats.py`
- Each company has its own scraper in `scrapers/`

## Current jobs

<!-- JOBS:START -->
_Updated 2026-10-19 21:31 UTC — 21 jobs posted in the last 14 days_

### Internships & Co-ops (7)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-10-19 | Ciena | [Wavelogic Embedded Software Developer Intern (Winter 2027)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Wavelogic-Embedded-Software-Developer-Intern--Winter-2027-_R031890) | Ottawa |
| 2026-10-19 | NVIDIA | [ASIC Verification Intern - Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/Canada-Toronto/ASIC-Verification-Intern---Summer-2027_JR2027982) | Canada, Toronto |
| 2026-10-16 | Intel | [GPU & AI Accelerator Hardware Design Undergraduate Intern](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/GPU---AI-Accelerator-Hardware-Design-Undergraduate-Intern_JR0287539) | Canada, Toronto |
| 2026-10-15 | Altera | [FPGA IP Design Engineer -  Intern](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-IP-Design-Engineer----Intern_R03324) | Toronto, Ontario, Canada |
| 2026-10-15 | Nokia | [Embedded C/C++ SW Developer Co-op/Intern](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/41311) | Ottawa, Ontario |
| 2026-10-08 | Amazon | [Systems Development Engineer Intern, Canada 2027](https://www.amazon.jobs/en/jobs/10573999) | Vancouver, British Columbia, CAN |
| 2026-10-06 | Ciena | [Hardware Design Co-Op (Winter 2027 - 4 Months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Design-Co-Op--Winter-2027---4-Months-_R031782) | Ottawa |

### Full-time (14)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-10-19 | AMD | [Design Verification Engineer](https://careers.amd.com/jobs/93955?lang=en-us) | MARKHAM, Canada |
| 2026-10-19 | AMD | [Systems Design Engineer](https://careers.amd.com/jobs/93474?lang=en-us) | VANCOUVER, Canada |
| 2026-10-19 | Ericsson | [RAN System Verification Professional](https://jobs.ericsson.com/careers/job/563121777356246) | Ottawa, ON, CA |
| 2026-10-16 | AMD | [GPU Design Verification Engineer](https://careers.amd.com/jobs/93729?lang=en-us) | MARKHAM, Canada |
| 2026-10-16 | AMD | [SoC Data Path Engineer](https://careers.amd.com/jobs/88677?lang=en-us) | MARKHAM, Canada |
| 2026-10-14 | GM | [Test Engineering, Data Engineering - Systems QA](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Markham-Ontario-Canada/Test-Engineering--Data-Engineering---Systems-QA_JR-202622079) | Markham, Ontario, Canada; Oshawa, Ontario, Canada |
| 2026-10-13 | GM | [Embedded Simulation Developer - SIL and Virtualization](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Markham-Ontario-Canada/Embedded-Simulation-Developer---SIL-and-Virtualization_JR-202622345-1) | Markham, Ontario, Canada |
| 2026-10-13 | Google | [Customer Engineer, Platform, Google Cloud (English, French)](https://www.google.com/about/careers/applications/jobs/results/83138342891201222) | Montreal, QC, Canada |
| 2026-10-09 | AMD | [IOHUB Design Verification Engineer](https://careers.amd.com/jobs/92834?lang=en-us) | MARKHAM, Canada |
| 2026-10-08 | AMD | [Systems Design Engineer (New Grad)](https://careers.amd.com/jobs/92338?lang=en-us) | MARKHAM, Canada |
| 2026-10-07 | AMD | [Systems Validation Engineer - Data Center GPU](https://careers.amd.com/jobs/93052?lang=en-us) | MARKHAM, Canada |
| 2026-10-07 | Tenstorrent | [Low-Level Software Engineer, LLK](https://job-boards.greenhouse.io/tenstorrent/jobs/5260226007) | Toronto, Ontario, Canada |
| 2026-10-06 | Nokia | [DSP Firmware Engineer](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/40797) | Ottawa, Ontario |
| 2026-10-05 | Tenstorrent | [Systems Engineer, Data Center Debug](https://job-boards.greenhouse.io/tenstorrent/jobs/5143663007) | Toronto, Ontario, Canada |
<!-- JOBS:END -->
