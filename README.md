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
_Updated 2026-10-28 21:32 UTC — 31 jobs posted in the last 14 days_

### Internships & Co-ops (5)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-10-27 | Ciena | [Optical Performance Lab Verification and Testing Co-op](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Optical-Performance-Lab-Verification-and-Testing-Co-op_R031991) | Ottawa |
| 2026-10-27 | Intel | [GPU & AI Accelerator Hardware Design Undergraduate Intern](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/GPU---AI-Accelerator-Hardware-Design-Undergraduate-Intern_JR0287539) | Canada, Toronto |
| 2026-10-19 | Ciena | [Wavelogic Embedded Software Developer Intern (Winter 2027)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Wavelogic-Embedded-Software-Developer-Intern--Winter-2027-_R031890) | Ottawa |
| 2026-10-19 | NVIDIA | [ASIC Verification Intern - Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/Canada-Toronto/ASIC-Verification-Intern---Summer-2027_JR2027982) | Canada, Toronto |
| 2026-10-15 | Nokia | [Embedded C/C++ SW Developer Co-op/Intern](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/41311) | Ottawa, Ontario |

### Full-time (26)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-10-28 | BlackBerry QNX | [QNX Systems Software Developer](https://bb.wd3.myworkdayjobs.com/QNX/job/Ottawa-Ontario/QNX-Systems-Software-Developer_20260323-1) | Ottawa, Ontario |
| 2026-10-28 | Ford | [Embedded Software Developer](https://efds.fa.em5.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/72899) | Ottawa, ON, Canada |
| 2026-10-27 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588644) | Vancouver, British Columbia, CAN |
| 2026-10-27 | Ericsson | [RAN System Verification Professional](https://jobs.ericsson.com/careers/job/563121777356246) | Ottawa, ON, CA |
| 2026-10-27 | Huawei | [Hardware & Embedded Systems Engineer - AI-Edge Devices](https://huaweicanada.recruitee.com/o/hardware-embedded-systems-engineer-ai-edge-devices) | Markham, Ontario, Canada |
| 2026-10-27 | Microchip | [SoC Design Engineer](https://microchiphr.wd5.myworkdayjobs.com/External/job/Canada---Burnaby/SoC-Design-Engineer_R4486-26) | Canada - Burnaby |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588632) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588637) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588639) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588640) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588643) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588635) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588630) | Vancouver, British Columbia, CAN |
| 2026-10-23 | AMD | [ASIC Verification Engineer, AI Networking IP](https://careers.amd.com/jobs/93714?lang=en-us) | OTTAWA, Canada |
| 2026-10-23 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/93922?lang=en-us) | MARKHAM, Canada |
| 2026-10-23 | Ciena | [Hardware Engineer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Engineer---New-Grad_R031914) | Ottawa |
| 2026-10-23 | Intel | [Verification Engineer – AI SoC Development](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Verification-Engineer---AI-SoC-Development_JR0287994) | Canada, Toronto |
| 2026-10-21 | AMD | [ASIC Design Engineer, PCIe IP Enablement](https://careers.amd.com/jobs/93547?lang=en-us) | MARKHAM, Canada |
| 2026-10-21 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/93791?lang=en-us) | MARKHAM, Canada |
| 2026-10-21 | Huawei | [Research Engineer - Agentic Software Systems Engineering](https://huaweicanada.recruitee.com/o/research-engineer-agentic-software-systems-engineering) | Markham, Ontario, Canada |
| 2026-10-19 | AMD | [Design Verification Engineer](https://careers.amd.com/jobs/93955?lang=en-us) | MARKHAM, Canada |
| 2026-10-19 | AMD | [Silicon Design Engineer (1 year contract)](https://careers.amd.com/jobs/93231?lang=en-us) | MARKHAM, Canada |
| 2026-10-19 | AMD | [Systems Design Engineer](https://careers.amd.com/jobs/93474?lang=en-us) | VANCOUVER, Canada |
| 2026-10-16 | AMD | [GPU Design Verification Engineer](https://careers.amd.com/jobs/93729?lang=en-us) | MARKHAM, Canada |
| 2026-10-16 | AMD | [SoC Data Path Engineer](https://careers.amd.com/jobs/88677?lang=en-us) | MARKHAM, Canada |
| 2026-10-14 | GM | [Test Engineering, Data Engineering - Systems QA](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Markham-Ontario-Canada/Test-Engineering--Data-Engineering---Systems-QA_JR-202622079) | Markham, Ontario, Canada; Oshawa, Ontario, Canada |
<!-- JOBS:END -->
