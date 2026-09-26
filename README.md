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
_Updated 2026-09-26 23:35 UTC — 33 jobs posted in the last 14 days_

### Internships & Co-ops (8)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-09-25 | Ciena | [ASIC Processor Complex Engineering Co-op (January 2027 - 4 months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Processor-Complex-Engineering-Co-op--January-2027---4-months-_R031744) | Ottawa |
| 2026-09-25 | Ciena | [Hardware (PCBA) Design and Verification Intern (Winter 2027 - 4 months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Canada--Ottawa--383-Terry-Fox--Bldg-C/Hardware--PCBA--Design-and-Verification-Intern--Winter-2027---4-months-_R031752) | Canada- Ottawa- 383 Terry Fox- Bldg C |
| 2026-09-23 | Analog Devices | [Analog Design Engineering Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Analog-Design-Engineering-Intern_R266614) | Canada, Toronto |
| 2026-09-23 | GM | [2027 Winter Co-op Mechatronic Infrastructure Diagnostic Systems](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Markham-Ontario-Canada/XMLNAME-2027-Winter-Co-op-Mechatronic-Infrastructure-Diagnostic-Systems_JR-202618915) | Markham, Ontario, Canada |
| 2026-09-22 | Ciena | [ASIC Engineer Intern](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Engineer-Intern_R031750) | Ottawa |
| 2026-09-17 | Marvell | [Data Center Silicon Hardware Engineering Intern - BS - 2027 Co-Op](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Ottawa-Canada/Data-Center-Silicon-Hardware-Engineering-Intern---Winter-2027_2604525) | Ottawa, Canada; Toronto, Canada |
| 2026-09-15 | Nokia | [Hardware Developer Eng Co-op/Intern](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/39600) | Ottawa, Ontario |
| 2026-09-14 | Marvell | [Firmware Engineer Intern](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Ottawa-Canada/Firmware-Engineer-Intern_2604738-1) | Ottawa, Canada |

### Full-time (25)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
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
| 2026-09-24 | Tenstorrent | [Software Engineer, Acceleration Kernel Development](https://job-boards.greenhouse.io/tenstorrent/jobs/4155609007) | Toronto, Ontario, Canada |
| 2026-09-24 | Tenstorrent | [Systems Engineer, Data Center Debug](https://job-boards.greenhouse.io/tenstorrent/jobs/5143663007) | Toronto, Ontario, Canada |
| 2026-09-23 | Altera | [FPGA Designer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Designer_R02835) | Toronto, Ontario, Canada |
| 2026-09-23 | Analog Devices | [Embedded Software Engineer](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Embedded-Software-Engineer_R266615) | Canada, Toronto; Canada, Vancouver |
| 2026-09-22 | AMD | [Software Development Engineer (Chip Product Security)](https://careers.amd.com/jobs/92300?lang=en-us) | MARKHAM, Canada |
| 2026-09-21 | AMD | [Ryzen/Radeon Systems Design Engineer](https://careers.amd.com/jobs/92299?lang=en-us) | MARKHAM, Canada |
| 2026-09-21 | Ciena | [Mixed Signal IP Integration Engineer – New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Mixed-Signal-IP-Integration-Engineer---New-Grad_R031688) | Ottawa |
| 2026-09-17 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/92178?lang=en-us) | MARKHAM, Canada |
| 2026-09-17 | ecobee | [Associate Verification Engineer](https://generac.wd5.myworkdayjobs.com/External/job/Canada---Toronto/Associate-Verification-Engineer_JR16559-1) | Canada - Toronto |
| 2026-09-16 | Cadence | [Distributed Systems Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/BURNABY-01/Distributed-Systems-Engineer_R53233-1) | BURNABY 01 |
| 2026-09-16 | Cadence | [Distributed Systems Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/BURNABY-01/Distributed-Systems-Engineer_R53232) | BURNABY 01 |
| 2026-09-15 | Altera | [FPGA Development Tools Engineer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools-Engineer_R03026-1) | Toronto, Ontario, Canada |
| 2026-09-15 | Altera | [FPGA Development Tools Engineer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools-Engineer_R03049) | Toronto, Ontario, Canada |
| 2026-09-15 | Analog Devices | [Associate Analog Design Engineer](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Associate-Analog-Design-Engineer_R266122) | Canada, Toronto |
| 2026-09-14 | Nokia | [DSP Firmware Engineer](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/40197) | Ottawa, Ontario |
<!-- JOBS:END -->
