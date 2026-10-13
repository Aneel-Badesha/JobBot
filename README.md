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
_Updated 2026-10-13 21:31 UTC — 24 jobs posted in the last 14 days_

### Internships & Co-ops (5)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-10-08 | Amazon | [Systems Development Engineer Intern, Canada 2027](https://www.amazon.jobs/en/jobs/10573999) | Vancouver, British Columbia, CAN |
| 2026-10-06 | Ciena | [Hardware Design Co-Op (Winter 2027 - 4 Months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Design-Co-Op--Winter-2027---4-Months-_R031782) | Ottawa |
| 2026-10-02 | Intel | [GPU & AI Accelerator Hardware Design Undergraduate Intern](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/GPU---AI-Accelerator-Hardware-Design-Undergraduate-Intern_JR0287539) | Canada, Toronto |
| 2026-10-01 | Intel | [Graphics Hardware Validation Undergraduate Engineering Intern](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Graphics-Hardware-Validation-Undergraduate-Engineering-Intern_JR0287535) | Canada, Toronto |
| 2026-09-29 | Ciena | [Hardware (PCBA) Design and Verification Intern (Winter 2027 - 4 Months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware--PCBA--Design-and-Verification-Intern--Winter-2027---4-Months-_R031787) | Ottawa |

### Full-time (19)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-10-13 | GM | [Embedded Simulation Developer - SIL and Virtualization](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Markham-Ontario-Canada/Embedded-Simulation-Developer---SIL-and-Virtualization_JR-202622345-1) | Markham, Ontario, Canada |
| 2026-10-13 | Google | [Customer Engineer, Platform, Google Cloud (English, French)](https://www.google.com/about/careers/applications/jobs/results/83138342891201222) | Montreal, QC, Canada |
| 2026-10-13 | Synopsys | [Silicon Validation Engineer](https://synopsys.avature.net/careers/JobDetail/Silicon-Validation-Engineer-Sr-Staff-Engineer-18768/18768?businessTitle=Silicon+Validation+Engineer) | Mississauga |
| 2026-10-13 | Synopsys | [Silicon Validation/Characterization Engineer](https://synopsys.avature.net/careers/JobDetail/Silicon-Validation-Characterization-Eng-Staff-Engineer-18757/18757?businessTitle=Silicon+Validation%2FCharacterization+Engineer+-+18757) | Nepean |
| 2026-10-09 | AMD | [IOHUB Design Verification Engineer](https://careers.amd.com/jobs/92834?lang=en-us) | MARKHAM, Canada |
| 2026-10-09 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/93349?lang=en-us) | MARKHAM, Canada |
| 2026-10-09 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/91483?lang=en-us) | MARKHAM, Canada |
| 2026-10-08 | AMD | [Systems Design Engineer (New Grad)](https://careers.amd.com/jobs/92338?lang=en-us) | MARKHAM, Canada |
| 2026-10-07 | AMD | [Systems Validation Engineer - Data Center GPU](https://careers.amd.com/jobs/93052?lang=en-us) | MARKHAM, Canada |
| 2026-10-07 | Cadence | [Distributed Systems Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/BURNABY-01/Distributed-Systems-Engineer_R53233-1) | BURNABY 01 |
| 2026-10-07 | Cadence | [Distributed Systems Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/BURNABY-01/Distributed-Systems-Engineer_R53232) | BURNABY 01 |
| 2026-10-07 | Tenstorrent | [Low-Level Software Engineer, LLK](https://job-boards.greenhouse.io/tenstorrent/jobs/5260226007) | Toronto, Ontario, Canada |
| 2026-10-06 | Nokia | [DSP Firmware Engineer](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/40797) | Ottawa, Ontario |
| 2026-10-05 | L3Harris | [Systems Engineer](https://careers.l3harris.com/en/job/montreal/systems-engineer/4832/100077248416) | Montreal, Quebec |
| 2026-10-05 | Tenstorrent | [Systems Engineer, Data Center Debug](https://job-boards.greenhouse.io/tenstorrent/jobs/5143663007) | Toronto, Ontario, Canada |
| 2026-10-02 | AMD | [Analog/Mixed-Signal SerDes Design Engineer](https://careers.amd.com/jobs/92938?lang=en-us) | MARKHAM, Canada |
| 2026-10-02 | Cerebras | [AI Fleet Platform Software Engineer](https://jobs.ashbyhq.com/cerebras/89ed36d3-d7e4-4c41-b466-2e39a30a84f4) | Sunnyvale, CA; Toronto, CAN |
| 2026-10-01 | AMD | [AI Platform Engineer, Silicon Design Infrastructure](https://careers.amd.com/jobs/92369?lang=en-us) | MARKHAM, Canada |
| 2026-09-30 | AMD | [Silicon Design Engineer](https://careers.amd.com/jobs/91986?lang=en-us) | MARKHAM, Canada |
<!-- JOBS:END -->
