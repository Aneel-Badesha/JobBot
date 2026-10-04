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
_Updated 2026-10-04 21:31 UTC — 40 jobs posted in the last 14 days_

### Internships & Co-ops (6)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-10-02 | Intel | [GPU & AI Accelerator Hardware Design Undergraduate Intern](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/GPU---AI-Accelerator-Hardware-Design-Undergraduate-Intern_JR0287539) | Canada, Toronto |
| 2026-10-01 | Intel | [Graphics Hardware Validation Undergraduate Engineering Intern](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Graphics-Hardware-Validation-Undergraduate-Engineering-Intern_JR0287535) | Canada, Toronto |
| 2026-09-29 | Ciena | [Hardware (PCBA) Design and Verification Intern (Winter 2027 - 4 Months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware--PCBA--Design-and-Verification-Intern--Winter-2027---4-Months-_R031787) | Ottawa |
| 2026-09-25 | Ciena | [Hardware (PCBA) Design and Verification Intern (Winter 2027 - 4 months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Canada--Ottawa--383-Terry-Fox--Bldg-C/Hardware--PCBA--Design-and-Verification-Intern--Winter-2027---4-months-_R031752) | Canada- Ottawa- 383 Terry Fox- Bldg C |
| 2026-09-23 | Analog Devices | [Analog Design Engineering Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Analog-Design-Engineering-Intern_R266614) | Canada, Toronto |
| 2026-09-22 | Ciena | [ASIC Engineer Intern](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Engineer-Intern_R031750) | Ottawa |

### Full-time (34)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-10-02 | AMD | [Analog/Mixed-Signal SerDes Design Engineer](https://careers.amd.com/jobs/92938?lang=en-us) | MARKHAM, Canada |
| 2026-10-02 | Cerebras | [AI Fleet Platform Software Engineer](https://jobs.ashbyhq.com/cerebras/89ed36d3-d7e4-4c41-b466-2e39a30a84f4) | Sunnyvale, CA; Toronto, CAN |
| 2026-10-01 | AMD | [AI Platform Engineer, Silicon Design Infrastructure](https://careers.amd.com/jobs/92369?lang=en-us) | MARKHAM, Canada |
| 2026-10-01 | AMD | [Silicon Design Engineer (1 year contract starting asap)](https://careers.amd.com/jobs/92764?lang=en-us) | MARKHAM, Canada |
| 2026-10-01 | AMD | [Silicon Design Engineer 2 (1-Year Contract)](https://careers.amd.com/jobs/93114?lang=en-us) | OTTAWA, Canada |
| 2026-09-30 | AMD | [Silicon Design Engineer](https://careers.amd.com/jobs/91986?lang=en-us) | MARKHAM, Canada |
| 2026-09-30 | Cadence | [Distributed Systems Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/BURNABY-01/Distributed-Systems-Engineer_R53233-1) | BURNABY 01 |
| 2026-09-30 | Cadence | [Distributed Systems Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/BURNABY-01/Distributed-Systems-Engineer_R53232) | BURNABY 01 |
| 2026-09-28 | AMD | [Firmware Engineer](https://careers.amd.com/jobs/90012?lang=en-us) | MARKHAM, Canada |
| 2026-09-28 | AMD | [Firmware Engineer](https://careers.amd.com/jobs/90462?lang=en-us) | VANCOUVER, Canada |
| 2026-09-28 | AMD | [RTL/Firmware Design Engineer](https://careers.amd.com/jobs/90713?lang=en-us) | MARKHAM, Canada |
| 2026-09-28 | AMD | [Silicon Design Engineer](https://careers.amd.com/jobs/90603?lang=en-us) | MARKHAM, Canada |
| 2026-09-28 | AMD | [Silicon Design Engineer](https://careers.amd.com/jobs/90108?lang=en-us) | VANCOUVER, Canada |
| 2026-09-28 | AMD | [Silicon Design Engineer](https://careers.amd.com/jobs/90826?lang=en-us) | MARKHAM, Canada |
| 2026-09-28 | AMD | [Silicon Design Engineer](https://careers.amd.com/jobs/91098?lang=en-us) | MARKHAM, Canada |
| 2026-09-28 | AMD | [Silicon Design Engineer](https://careers.amd.com/jobs/90373?lang=en-us) | VANCOUVER, Canada |
| 2026-09-28 | AMD | [Silicon Design Infrastructure Hardware/Software Engineer](https://careers.amd.com/jobs/87268?lang=en-us) | MARKHAM, Canada |
| 2026-09-28 | Cerebras | [ML Runtime and Kernel Engineer - Core ML](https://jobs.ashbyhq.com/cerebras/d6df4a44-a05f-4fac-b012-6d2e8bb981f6) | Sunnyvale, CA; Toronto, CAN |
| 2026-09-28 | Ciena | [Hardware Engineer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Engineer---New-Grad_R031783) | Ottawa |
| 2026-09-28 | Tenstorrent | [Systems & Infrastructure Administrator, IT - Contractor](https://job-boards.greenhouse.io/tenstorrent/jobs/5230724007) | Toronto, Ontario, Canada |
| 2026-09-26 | Arm | [CAD-DFT Engineer](https://careers.arm.com/job/toronto/cad-dft-engineer/33099/98723949120) | Toronto, Canada |
| 2026-09-25 | AMD | [Physical Design Engineer](https://careers.amd.com/jobs/92896?lang=en-us) | MARKHAM, Canada |
| 2026-09-25 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/92182?lang=en-us) | MARKHAM, Canada |
| 2026-09-24 | Amazon | [Builder - Mobile (Platform), Ring](https://www.amazon.jobs/en/jobs/10559417) | Toronto, Ontario, CAN |
| 2026-09-24 | AMD | [Static Timing Analysis / Full Chip Timing Engineer](https://careers.amd.com/jobs/92583?lang=en-us) | MARKHAM, Canada |
| 2026-09-24 | AMD | [Systems Design Engineer - dGPU / CPU Software Feature Enablement](https://careers.amd.com/jobs/92195?lang=en-us) | MARKHAM, Canada |
| 2026-09-24 | Huawei | [Researcher – Agent Platform R&D](https://huaweicanada.recruitee.com/o/researcher-agent-platform-rd) | Markham, Ontario, Canada |
| 2026-09-24 | Tenstorrent | [Electrical Engineer, PCB Design](https://job-boards.greenhouse.io/tenstorrent/jobs/5178453007) | Belgrade, Serbia; Toronto, Ontario, Canada |
| 2026-09-24 | Tenstorrent | [Physical Design Engineer, AI Accelerator IP](https://job-boards.greenhouse.io/tenstorrent/jobs/5198590007) | Austin, Texas, United States; Belgrade, Serbia; Toronto, Ontario, Canada |
| 2026-09-24 | Tenstorrent | [Physical Design Methodology Engineer, AI HW IP](https://job-boards.greenhouse.io/tenstorrent/jobs/5198608007) | Austin, Texas, United States; Belgrade, Serbia; Toronto, Ontario, Canada |
| 2026-09-23 | Altera | [FPGA Designer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Designer_R02835) | Toronto, Ontario, Canada |
| 2026-09-23 | Analog Devices | [Embedded Software Engineer](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Embedded-Software-Engineer_R266615) | Canada, Toronto; Canada, Vancouver |
| 2026-09-22 | AMD | [Software Development Engineer (Chip Product Security)](https://careers.amd.com/jobs/92300?lang=en-us) | MARKHAM, Canada |
| 2026-09-21 | Ciena | [Mixed Signal IP Integration Engineer – New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Mixed-Signal-IP-Integration-Engineer---New-Grad_R031688) | Ottawa |
<!-- JOBS:END -->
