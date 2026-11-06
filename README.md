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
_Updated 2026-11-06 22:31 UTC — 40 jobs posted in the last 14 days_

### Internships & Co-ops (9)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-11-05 | Intel | [Graphics Hardware Validation Undergraduate Engineering Intern](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Graphics-Hardware-Validation-Undergraduate-Engineering-Intern_JR0287535) | Canada, Toronto |
| 2026-11-03 | Ciena | [Hardware Engineering Co-op (Winter 2027)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Engineering-Co-op--Winter-2027-_R032054) | Ottawa |
| 2026-11-02 | Intel | [GPU & AI Accelerator Hardware Design Undergraduate Intern](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/GPU---AI-Accelerator-Hardware-Design-Undergraduate-Intern_JR0287539) | Canada, Toronto |
| 2026-10-30 | Altera | [FPGA Development Tools - Intern](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools---Intern_R03394) | Toronto, Ontario, Canada |
| 2026-10-30 | Ciena | [ASIC Engineer Intern](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Engineer-Intern_R031750) | Ottawa |
| 2026-10-30 | NVIDIA | [ASIC Verification Intern - Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/Canada-Toronto/ASIC-Verification-Intern---Summer-2027_JR2027982) | Canada, Toronto |
| 2026-10-29 | Ciena | [Embedded Software Engineer – Co-op Winter 2027](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-Software-Engineer---Co-op-Winter-2027_R032005) | Ottawa |
| 2026-10-29 | Ciena | [Hardware Characterization Automation Co-op (Winter 2027)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Characterization-Automation-Co-op--Winter-2027-_R032014) | Ottawa |
| 2026-10-27 | Ciena | [Optical Performance Lab Verification and Testing Co-op](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Optical-Performance-Lab-Verification-and-Testing-Co-op_R031991) | Ottawa |

### Full-time (31)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-11-06 | AMD | [Mixed Signal Custom Layout  - Temporary/Seasonal](https://careers.amd.com/jobs/93711?lang=en-us) | MARKHAM, Canada |
| 2026-11-06 | Ciena | [Embedded Security Software Developer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-Security-Software-Developer---New-Grad_R032066) | Ottawa |
| 2026-11-06 | Ericsson | [RAN System Verification Professional](https://jobs.ericsson.com/careers/job/563121777519784) | Ottawa, ON, CA |
| 2026-11-05 | AMD | [IP-Post Silicon Validation Engineer](https://careers.amd.com/jobs/97341?lang=en-us) | VANCOUVER, Canada |
| 2026-11-05 | AMD | [IP-Post Silicon Validation Engineer](https://careers.amd.com/jobs/96261?lang=en-us) | MARKHAM, Canada |
| 2026-11-05 | Arm | [IP Verification Engineer](https://careers.arm.com/job/toronto/ip-verification-engineer/33099/102559123680) | Toronto, Canada |
| 2026-11-03 | AMD | [IP Silicon Validation Engineer](https://careers.amd.com/jobs/97103?lang=en-us) | VANCOUVER, Canada |
| 2026-11-02 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/87376?lang=en-us) | MARKHAM, Canada |
| 2026-11-02 | Ciena | [ASIC Front End Implementation Engineer](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Senior-Physical-Design-Engineer_R031691) | Ottawa |
| 2026-11-02 | Ciena | [Embedded Software Engineer](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-software-engineer_R031266) | Ottawa |
| 2026-11-02 | Ciena | [Hardware Engineer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Engineer---New-Grad_R031914) | Ottawa |
| 2026-11-02 | Ciena | [Mixed Signal Design Engineer](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Mixed-Signal-Design-Engineer_R030994) | Ottawa |
| 2026-11-02 | Huawei | [Engineer - Optical Communication Systems (Test, Modeling & Sensing)](https://huaweicanada.recruitee.com/o/engineer-optical-communication-systems-test-modeling-sensing) | Ottawa, Ontario, Canada |
| 2026-10-30 | AMD | [IP Silicon Validation Engineer](https://careers.amd.com/jobs/93586?lang=en-us) | MARKHAM, Canada |
| 2026-10-30 | AMD | [Systems Design Engineer](https://careers.amd.com/jobs/93526?lang=en-us) | MARKHAM, Canada |
| 2026-10-30 | Tenstorrent | [Software Engineer, Acceleration Kernel Development](https://job-boards.greenhouse.io/tenstorrent/jobs/4155609007) | Santa Clara, California, United States; Toronto, Ontario, Canada |
| 2026-10-29 | AMD | [DSP Systems Engineer](https://careers.amd.com/jobs/93754?lang=en-us) | OTTAWA, Canada |
| 2026-10-28 | BlackBerry QNX | [QNX Systems Software Developer](https://bb.wd3.myworkdayjobs.com/QNX/job/Ottawa-Ontario/QNX-Systems-Software-Developer_20260323-1) | Ottawa, Ontario |
| 2026-10-28 | Ford | [Embedded Software Developer](https://efds.fa.em5.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/72899) | Ottawa, ON, Canada |
| 2026-10-27 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588644) | Vancouver, British Columbia, CAN |
| 2026-10-27 | Huawei | [Hardware & Embedded Systems Engineer - AI-Edge Devices](https://huaweicanada.recruitee.com/o/hardware-embedded-systems-engineer-ai-edge-devices) | Markham, Ontario, Canada |
| 2026-10-27 | Microchip | [SoC Design Engineer](https://microchiphr.wd5.myworkdayjobs.com/External/job/Canada---Burnaby/SoC-Design-Engineer_R4486-26) | Canada - Burnaby |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588632) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588637) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588639) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588643) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588635) | Vancouver, British Columbia, CAN |
| 2026-10-26 | Amazon | [Software Dev Engineer, Pricing Shared Platform](https://www.amazon.jobs/en/jobs/10588630) | Vancouver, British Columbia, CAN |
| 2026-10-23 | AMD | [ASIC Verification Engineer, AI Networking IP](https://careers.amd.com/jobs/93714?lang=en-us) | OTTAWA, Canada |
| 2026-10-23 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/93922?lang=en-us) | MARKHAM, Canada |
| 2026-10-23 | Intel | [Verification Engineer – AI SoC Development](https://intel.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Verification-Engineer---AI-SoC-Development_JR0287994) | Canada, Toronto |
<!-- JOBS:END -->
