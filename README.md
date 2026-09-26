# FinancialBot

A job scraper and Gmail digest bot for hardware/firmware/embedded systems roles. Scrapes ~46 hardware and semiconductor companies for firmware, embedded, hardware, and systems engineer internships, co-ops, and new-grad roles in Toronto, Montreal, Ottawa, and Vancouver. Emails a daily digest and keeps the table below up to date.

**Features:**
- Scrapes ~46 hardware/semiconductor companies
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
_Updated 2026-09-26 23:01 UTC — 118 jobs_

| Company | Role | Location |
|---------|------|----------|
| Altera | [FPGA Compiler (Placer) Engineer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Compiler--Placer--Engineer_R02895) | Toronto, Ontario, Canada |
| Altera | [FPGA Designer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Designer_R02835) | Toronto, Ontario, Canada |
| Altera | [FPGA Development Tools Engineer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools-Engineer_R03026-1) | Toronto, Ontario, Canada |
| Altera | [FPGA Development Tools Engineer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools-Engineer_R03049) | Toronto, Ontario, Canada |
| Altera | [FPGA Development Tools Engineer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools-Engineer_R02854) | Toronto, Ontario, Canada |
| Altera | [FPGA Development Tools Engineer – Synthesis](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools-Engineer---Synthesis_R02600) | Toronto, Ontario, Canada |
| Altera | [IP Firmware Design Engineer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/IP-Firmware-Design-Engineer_R02871) | Toronto, Ontario, Canada |
| Amazon | [Builder - Mobile (Platform), Ring](https://www.amazon.jobs/en/jobs/10559417) | Toronto, Ontario, CAN |
| Amazon | [Design Verification Engineer, Annapurna Labs](https://www.amazon.jobs/en/jobs/10515427) | Toronto, Ontario, CAN |
| Amazon | [ML Kernel Performance Engineer, AWS Neuron, Annapurna Labs](https://www.amazon.jobs/en/jobs/10526702) | Toronto, Ontario, CAN |
| Amazon | [ML Systems Software Development Engineer Intern, Annapurna Labs - 2027](https://www.amazon.jobs/en/jobs/10538066) | Toronto, Ontario, CAN |
| Amazon | [Software Development Engineer - Supply Chain Optimization Tech, Inbound Systems](https://www.amazon.jobs/en/jobs/10482782) | Toronto, Ontario, CAN |
| Amazon | [Software Development Engineer - Supply Chain Optimization Tech, Inbound Systems](https://www.amazon.jobs/en/jobs/10482781) | Toronto, Ontario, CAN |
| Amazon | [Software Development Engineer, RDS Platform](https://www.amazon.jobs/en/jobs/10424755) | Vancouver, British Columbia, CAN |
| AMD | [AI Systems Engineer – AI Model (Training & Inference)](https://canadacareers-amd.icims.com/jobs/90266/login) | MARKHAM, Canada |
| AMD | [Analog/Mixed-Signal SerDes Design Engineer](https://canadacareers-amd.icims.com/jobs/86868/login) | Markham, Canada |
| AMD | [ASIC Design Verification Engineer](https://canadacareers-amd.icims.com/jobs/90287/login) | OTTAWA, Canada |
| AMD | [ASIC Verification Engineer](https://canadacareers-amd.icims.com/jobs/87378/login) | MARKHAM, Canada |
| AMD | [Design Verification Engineer](https://canadacareers-amd.icims.com/jobs/91740/login) | VANCOUVER, Canada |
| AMD | [Design Verification Engineer](https://canadacareers-amd.icims.com/jobs/90564/login) | MARKHAM, Canada |
| AMD | [Design Verification Engineer](https://canadacareers-amd.icims.com/jobs/88877/login) | MARKHAM, Canada |
| AMD | [Design Verification Engineer (1-Year Contract)](https://canadacareers-amd.icims.com/jobs/85833/login) | OTTAWA, Canada |
| AMD | [DFT Design Engineer](https://canadacareers-amd.icims.com/jobs/88718/login) | MARKHAM, Canada |
| AMD | [Digital Design Verification Engineer](https://canadacareers-amd.icims.com/jobs/89215/login) | MARKHAM, Canada |
| AMD | [Fullchip Floorplan Physical Design Engineer](https://canadacareers-amd.icims.com/jobs/91541/login) | MARKHAM, Canada |
| AMD | [IOMMU Verification Engineer](https://canadacareers-amd.icims.com/jobs/91643/login) | VANCOUVER, Canada |
| AMD | [IP Silicon Firmware Engineer](https://canadacareers-amd.icims.com/jobs/92333/login) | VANCOUVER, Canada |
| AMD | [IP Silicon Firmware Engineer](https://canadacareers-amd.icims.com/jobs/92064/login) | MARKHAM, Canada |
| AMD | [Mixed Signal Circuit Design Analysis & CAD Engineer ( Temporary Contract)](https://canadacareers-amd.icims.com/jobs/91052/login) | MARKHAM, Canada |
| AMD | [Physical Design Engineer](https://canadacareers-amd.icims.com/jobs/92896/login) | MARKHAM, Canada |
| AMD | [Physical Design Engineer](https://canadacareers-amd.icims.com/jobs/84595/login) | VANCOUVER, Canada |
| AMD | [RTL Design Engineer](https://canadacareers-amd.icims.com/jobs/92182/login) | MARKHAM, Canada |
| AMD | [RTL Design Engineer](https://canadacareers-amd.icims.com/jobs/92178/login) | MARKHAM, Canada |
| AMD | [RTL Design Engineer](https://canadacareers-amd.icims.com/jobs/87376/login) | MARKHAM, Canada |
| AMD | [RTL Digital Design Engineer](https://canadacareers-amd.icims.com/jobs/88603/login) | VANCOUVER, Canada |
| AMD | [Ryzen/Radeon Systems Design Engineer](https://canadacareers-amd.icims.com/jobs/92299/login) | MARKHAM, Canada |
| AMD | [Server Systems Assembly Manufacturing Engineer](https://careers-amd.icims.com/jobs/88983/login) | MARKHAM, Canada |
| AMD | [Short Term 2027 Firmware Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/91320/login) | MARKHAM, Canada |
| AMD | [Short Term 2027 Firmware Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/91313/login) | VANCOUVER, Canada |
| AMD | [Short Term 2027 Hardware Design Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/91360/login) | MARKHAM, Canada |
| AMD | [Short Term 2027 Hardware Design Verification Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/91361/login) | MARKHAM, Canada |
| AMD | [Short Term 2027 Hardware Design Verification Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/91362/login) | VANCOUVER, Canada |
| AMD | [Silicon Design Engineer (1 year contract)](https://canadacareers-amd.icims.com/jobs/88719/login) | MARKHAM, Canada |
| AMD | [Silicon Design Verification Engineer](https://canadacareers-amd.icims.com/jobs/91979/login) | MARKHAM, Canada |
| AMD | [SOC CAD Engineer](https://canadacareers-amd.icims.com/jobs/87520/login) | MARKHAM, Canada |
| AMD | [SoC Data Path Engineer](https://canadacareers-amd.icims.com/jobs/88677/login) | MARKHAM, Canada |
| AMD | [SoC DFX Scan / ATPG Engineer](https://canadacareers-amd.icims.com/jobs/89475/login) | OTTAWA, Canada |
| AMD | [SoC DFX Scan / ATPG Engineer](https://canadacareers-amd.icims.com/jobs/81103/login) | MARKHAM, Canada |
| AMD | [SOC Engineer](https://canadacareers-amd.icims.com/jobs/89711/login) | MARKHAM, Canada |
| AMD | [Software Development Engineer (Chip Product Security)](https://careers-amd.icims.com/jobs/92300/login) | MARKHAM, Canada |
| AMD | [Static Timing Analysis / Full Chip Timing Engineer](https://canadacareers-amd.icims.com/jobs/92583/login) | MARKHAM, Canada |
| AMD | [Summer 2027 Long Term Analog and Mixed Signal Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/91369/login) | MARKHAM, Canada |
| AMD | [Summer 2027 Long Term ASIC Verification Engineering Intern/ Co-Op](https://campuscanada-amd.icims.com/jobs/91207/login) | OTTAWA, Canada |
| AMD | [Summer 2027 Long Term Firmware Engineering Intern/Co-op](https://campuscanada-amd.icims.com/jobs/90301/login) | VANCOUVER, Canada |
| AMD | [Summer 2027 Long Term Firmware Engineering Intern/Co-op](https://campuscanada-amd.icims.com/jobs/90297/login) | MARKHAM, Canada |
| AMD | [Summer 2027 Long Term Hardware Design Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/90372/login) | VANCOUVER, Canada |
| AMD | [Summer 2027 Long Term Hardware Design Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/90367/login) | MARKHAM, Canada |
| AMD | [Summer 2027 Long Term Hardware Design Verification Engineering Intern/Co-Op](https://campuscanada-amd.icims.com/jobs/90379/login) | MARKHAM, Canada |
| AMD | [System Firmware Technical Engineer (1 yr contract)](https://canadacareers-amd.icims.com/jobs/87355/login) | MARKHAM, Canada |
| AMD | [Systems Design Engineer - dGPU / CPU Software Feature Enablement](https://canadacareers-amd.icims.com/jobs/92195/login) | MARKHAM, Canada |
| AMD | [Verification Engineer](https://canadacareers-amd.icims.com/jobs/91540/login) | MARKHAM, Canada |
| Analog Devices | [Analog Design Engineering Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Analog-Design-Engineering-Intern_R266614) | Canada, Toronto |
| Analog Devices | [Associate Analog Design Engineer](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Associate-Analog-Design-Engineer_R266122) | Canada, Toronto |
| Analog Devices | [Embedded Software Engineer](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Toronto/Embedded-Software-Engineer_R266615) | Canada, Toronto; Canada, Vancouver |
| Analog Devices | [Mixed-Signal Design Engineer](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-MA-Wilmington/Mixed-Signal-Design-Engineer_R262378) | US, MA, Wilmington; Canada, Toronto; US, TX, Austin, Plaza on the Lake; US, CA, San Diego, Avenue of Science; US, NC, Durham |
| Arm | [CAD-DFT Engineer](https://careers.arm.com/job/toronto/cad-dft-engineer/33099/98723949120) | Toronto, Canada |
| Cadence | [Analog/Mixed-Signal IC Design Co-Op/Intern  (Summer 2026) / Stage/Co-Op en Conception de CI Analogiques/Signal Mixte (Été  2026)](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/MOUNT-ROYAL-Montreal/Analog-Mixed-Signal-IC-Design-Co-Op-Intern---Summer-2026----Stage-Co-Op-en-Conception-de-CI-Analogiques-Signal-Mixte--t--2026-_R53993-2) | MOUNT-ROYAL (Montreal) |
| Cadence | [Distributed Systems Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/BURNABY-01/Distributed-Systems-Engineer_R53233-1) | BURNABY 01 |
| Cadence | [Distributed Systems Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/BURNABY-01/Distributed-Systems-Engineer_R53232) | BURNABY 01 |
| Cadence | [Firmware Design Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/MOUNT-ROYAL-Montreal/Ingnieur-en-conception-de-micrologiciel---Firmware-Design-Engineer_R55507) | MOUNT-ROYAL (Montreal); MOUNT-ROYAL 01 (MONTREAL) |
| Cadence | [Ingénieur en conception de micrologiciel - Firmware Design Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/MOUNT-ROYAL-Montreal/Ingnieur-en-conception-de-micrologiciel---Firmware-Design-Engineer_R55932) | MOUNT-ROYAL (Montreal); MOUNT-ROYAL 01 (MONTREAL) |
| Cadence | [Ingénieur en conception de micrologiciel - Firmware Design Engineer](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/MOUNT-ROYAL-Montreal/Ingnieur-en-conception-de-micrologiciel---Firmware-Design-Engineer_R55931) | MOUNT-ROYAL (Montreal); MOUNT-ROYAL 01 (MONTREAL) |
| Cerebras | [FPGA Engineer](https://jobs.ashbyhq.com/cerebras/3f85f614-264f-4987-9fb5-320ee2798e97) | Sunnyvale, CA; Toronto, CAN |
| Cerebras | [ML Systems Integration Engineer](https://jobs.ashbyhq.com/cerebras/c35a389c-807e-45fb-bfda-03f6b1361871) | Sunnyvale, CA; Toronto, CAN |
| Cerebras | [Software Engineer, Inference Platform](https://jobs.ashbyhq.com/cerebras/80775253-7fba-4a3b-87ee-0e70ce8e995c) | Sunnyvale, CA; Toronto, CAN |
| Ciena | [ASIC Engineer Intern](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Engineer-Intern_R031750) | Ottawa |
| Ciena | [ASIC Processor Complex Engineering Co-op (January 2027 - 4 months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Processor-Complex-Engineering-Co-op--January-2027---4-months-_R031744) | Ottawa |
| Ciena | [ASIC Synthesis and STA Engineer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Synthesis-and-STA-Engineer---New-Grad_R030893) | Ottawa |
| Ciena | [Embedded Software Developer (New Grad)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-Software-Developer--New-Grad-_R031481) | Ottawa |
| Ciena | [Embedded software engineer](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-software-engineer_R031266) | Ottawa |
| Ciena | [Embedded Software Engineer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-Software-Engineer---New-Grad_R031571) | Ottawa |
| Ciena | [Hardware (PCBA) Design and Verification Intern (Winter 2027 - 4 months)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Canada--Ottawa--383-Terry-Fox--Bldg-C/Hardware--PCBA--Design-and-Verification-Intern--Winter-2027---4-months-_R031752) | Canada- Ottawa- 383 Terry Fox- Bldg C |
| Ciena | [Hardware Engineer, Power Design, onsite Kanata](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Engineer--Power-Design--onsite-Kanata_R031227) | Ottawa |
| Ciena | [Hardware Power Engineer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Power-Engineer---New-Grad_R030580) | Ottawa |
| Ciena | [Mixed Signal Design Engineer](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Mixed-Signal-Design-Engineer_R030994) | Ottawa |
| Ciena | [Mixed Signal IP Integration Engineer – New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Mixed-Signal-IP-Integration-Engineer---New-Grad_R031688) | Ottawa |
| Ciena | [NPI Hardware Co-op (8 month - January 2027)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/NPI-Hardware-Co-op--8-month---January-2027-_R031642) | Ottawa |
| Ciena | [Product Verification Technologist](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Product-Verification-Technologist_R031555) | Ottawa |
| ecobee | [Associate Verification Engineer](https://generac.wd5.myworkdayjobs.com/External/job/Canada---Toronto/Associate-Verification-Engineer_JR16559-1) | Canada - Toronto |
| Ford | [Embedded Software Developer - BSP/Bootloader](https://efds.fa.em5.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/69725) | Ottawa, ON, Canada |
| Ford | [Software Development (Embedded) Engineer](https://efds.fa.em5.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/68556) | Ottawa, ON, Canada |
| GM | [2027 Winter Co-op Mechatronic Infrastructure Diagnostic Systems](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Markham-Ontario-Canada/XMLNAME-2027-Winter-Co-op-Mechatronic-Infrastructure-Diagnostic-Systems_JR-202618915) | Markham, Ontario, Canada |
| GM | [Embedded Simulation Developer - SIL and Virtualization](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Markham-Ontario-Canada/Software-Developer----Virtualization-and-SIL-Integration_JR-202602900) | Markham, Ontario, Canada |
| Huawei | [Co-op Engineer - openJiuwen AI Agent Platform](https://huaweicanada.recruitee.com/o/co-op-engineer-openjiuwen-ai-agent-platform) | Markham, Ontario, Canada |
| Huawei | [Database Research Expert - Big Data Platform](https://huaweicanada.recruitee.com/o/database-research-expert) | Markham, Ontario, Canada |
| Huawei | [Engineer - Optical Communication Systems (Test, Modeling & Sensing)](https://huaweicanada.recruitee.com/o/engineer-optical-communication-systems-test-modeling-sensing) | Ottawa, Ontario, Canada |
| Huawei | [Engineer - Optical Systems](https://huaweicanada.recruitee.com/o/engineer-optical-systems-1) | Ottawa, Ontario, Canada |
| Huawei | [Research Engineer - Agentic Software Systems Engineering](https://huaweicanada.recruitee.com/o/research-engineer-agentic-software-systems-engineering) | Markham, Ontario, Canada |
| Huawei | [Research Engineer - AI Workload & Systems](https://huaweicanada.recruitee.com/o/research-engineer-ai-workload-systems) | Markham, Ontario, Canada |
| Huawei | [Researcher - Real-Time Embedded OS](https://huaweicanada.recruitee.com/o/researcher-realtime-embedded-os) | Ottawa, Ontario, Canada |
| Huawei | [Researcher – Agent Platform R&D](https://huaweicanada.recruitee.com/o/researcher-agent-platform-rd) | Markham, Ontario, Canada |
| Huawei | [Researcher – AI/ML Real-Time Embedded OS](https://huaweicanada.recruitee.com/o/researcher-real-time-embedded-os-2) | Ottawa, Ontario, Canada |
| Lightmatter | [Analog IC Design Engineer, High-Speed](https://boards.greenhouse.io/lightmatter/jobs/4418733008?gh_jid=4418733008) | Toronto, ON |
| Marvell | [Data Center Silicon Hardware Engineering Intern - BS - 2027 Co-Op](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Ottawa-Canada/Data-Center-Silicon-Hardware-Engineering-Intern---Winter-2027_2604525) | Ottawa, Canada; Toronto, Canada |
| Marvell | [Firmware Engineer Intern](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Ottawa-Canada/Firmware-Engineer-Intern_2604738-1) | Ottawa, Canada |
| Marvell | [Silicon Photonics Intern - PhD (Fall 2026 Start Date)](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Ottawa-Canada/Silicon-Photonics-Intern---PhD_2502469) | Ottawa, Canada |
| Microchip | [ASIC Development Engineer](https://microchiphr.wd5.myworkdayjobs.com/External/job/Canada---Burnaby/ASIC-Development-Engineer_R3761-26) | Canada - Burnaby |
| Nokia | [DSP Firmware Engineer](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/40197) | Ottawa, Ontario |
| Nokia | [DSP Firmware Engineering Co-op/Intern](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/39237) | Ottawa, Ontario |
| Nokia | [Firmware DSP Engineer](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/40264) | Ottawa, Ontario |
| Nokia | [Hardware Developer Eng Co-op/Intern](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/39600) | Ottawa, Ontario |
| NXP | [IC Design Verification Engineer](https://nxp.wd3.myworkdayjobs.com/careers/job/Kanata/IC-Design-Verification-Engineer_R-10063155) | Kanata |
| NXP | [Software Engineer - Hardware Design Verification](https://nxp.wd3.myworkdayjobs.com/careers/job/Kanata/Digital-Verification-Engineer_R-10063157) | Kanata |
| Tenstorrent | [Electrical Engineer, PCB Design](https://job-boards.greenhouse.io/tenstorrent/jobs/5178453007) | Belgrade, Serbia; Toronto, Ontario, Canada |
| Tenstorrent | [Physical Design Engineer, AI Accelerator IP](https://job-boards.greenhouse.io/tenstorrent/jobs/5198590007) | Austin, Texas, United States; Belgrade, Serbia; Toronto, Ontario, Canada |
| Tenstorrent | [Physical Design Methodology Engineer, AI HW IP](https://job-boards.greenhouse.io/tenstorrent/jobs/5198608007) | Austin, Texas, United States; Belgrade, Serbia; Toronto, Ontario, Canada |
| Tenstorrent | [Software Engineer, Acceleration Kernel Development](https://job-boards.greenhouse.io/tenstorrent/jobs/4155609007) | Toronto, Ontario, Canada |
| Tenstorrent | [Systems Engineer, Data Center Debug](https://job-boards.greenhouse.io/tenstorrent/jobs/5143663007) | Toronto, Ontario, Canada |
<!-- JOBS:END -->
