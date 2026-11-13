# JobBot

A job scraper and Gmail digest bot for hardware/firmware/embedded systems roles. Scrapes ~80 hardware, semiconductor, robotics, space, and automotive companies for firmware, embedded, hardware, and systems engineer roles: internships, co-ops, and new-grad roles in Toronto, Montreal, Ottawa, and Vancouver, plus internships anywhere in the US. Emails a daily digest and keeps the table below up to date.

**Features:**
- Scrapes ~80 hardware/semiconductor/robotics/space/automotive companies
- Filters for firmware/embedded/hardware/systems roles in target Canadian cities (Toronto, Montreal, Ottawa, Vancouver), and internships/co-ops anywhere in the US
- Adds active hardware internships from the [Simplify list](https://github.com/SimplifyJobs/Summer2027-Internships)
- Shows each role's term and flags citizenship, sponsorship, and graduate-degree requirements where known
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
_Updated 2026-11-13 22:38 UTC — 515 roles. Internships stay until they leave the board; full-time roles for 14 days_

_🇺🇸 U.S. citizens / clearance only · 🛂 no sponsorship · 🎓 graduate degree_

### Canada (75)

| Posted | Company | Role | Location | Term | Flags |
|--------|---------|------|----------|------|-------|
| 2026-11-13 | AMD | [Silicon Design Engineer](https://careers.amd.com/jobs/96257?lang=en-us) | MARKHAM, Canada |  |  |
| 2026-11-12 | Analog Devices | [Analog Design Engineering Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Ottawa/Analog-Design-Engineering-Intern_R267446) | Canada, Ottawa; Canada, Toronto |  |  |
| 2026-11-12 | Analog Devices | [Analog Design Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/Canada-Ottawa/Analog-Design-Engineering-Intern_R267446) | Ottawa, ON, Canada |  |  |
| 2026-11-09 | Altera | [FPGA Design Verification Intern](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Design-Verification-Intern_R03440) | Toronto, Ontario, Canada; Toronto, ON, Canada |  |  |
| 2026-11-09 | Altera | [FPGA Development Tools Engineer](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools-Engineer_R03413) | Toronto, Ontario, Canada |  |  |
| 2026-11-09 | Qualcomm | [Firmware Engineering Intern](https://qualcomm.eightfold.ai/careers/job/446722038614) | Toronto, ON, Canada | Summer 2027 |  |
| 2026-11-06 | AMD | [Mixed Signal Custom Layout  - Temporary/Seasonal](https://careers.amd.com/jobs/93711?lang=en-us) | MARKHAM, Canada |  |  |
| 2026-11-06 | Qualcomm | [Digital Design Engineer Intern - Interim Engineering Intern - Systems](https://qualcomm.eightfold.ai/careers/job/446722005254) | Toronto, ON, Canada | Summer 2027 |  |
| 2026-11-06 | Qualcomm | [RF/Analog Verification Engineer Intern](https://qualcomm.eightfold.ai/careers/job/446722001120) | Markham, ON, Canada | Summer 2027 |  |
| 2026-11-05 | AMD | [IP-Post Silicon Validation Engineer](https://careers.amd.com/jobs/96261?lang=en-us) | MARKHAM, Canada; VANCOUVER, Canada |  |  |
| 2026-11-05 | Arm | [IP Verification Engineer](https://careers.arm.com/job/toronto/ip-verification-engineer/33099/102559123680) | Toronto, Canada |  |  |
| 2026-11-05 | MDA Space | [Systems Engineer, Missions](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=2d5d7a56-04bd-45b8-b057-814b59fd3b61) | Richmond, British Columbia, Canada |  |  |
| 2026-11-05 | Qualcomm | [Display IP FPGA Emulation Intern](https://qualcomm.eightfold.ai/careers/job/446721972361) | Markham, ON, Canada | Summer 2027 |  |
| 2026-11-05 | Qualcomm | [Driver and Tools Developer Intern - Telemetry Firmware](https://qualcomm.eightfold.ai/careers/job/446721989047) | Markham, ON, Canada | Summer 2027 |  |
| 2026-11-03 | AMD | [IP Silicon Validation Engineer](https://careers.amd.com/jobs/93586?lang=en-us) | MARKHAM, Canada; VANCOUVER, Canada |  |  |
| 2026-11-03 | Arlo Technologies | [Firmware Developer Co-op](https://arlo.wd12.myworkdayjobs.com/External_Careers/job/Richmond-BC-Canada/Firmware-Developer-Co-op_JR100445) | Richmond, BC, Canada |  |  |
| 2026-11-03 | Arlo Technologies | [Hardware Engineer Co-op](https://arlo.wd12.myworkdayjobs.com/External_Careers/job/Richmond-BC-Canada/Hardware-Engineer-Co-op_JR100446) | Richmond, BC, Canada |  |  |
| 2026-11-03 | Ciena | [Hardware Engineering Co-op](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Engineering-Co-op--Winter-2027-_R032054) | Ottawa, ON, Canada | Winter 2027 |  |
| 2026-11-02 | Huawei | [Engineer - Optical Communication Systems (Test, Modeling & Sensing)](https://huaweicanada.recruitee.com/o/engineer-optical-communication-systems-test-modeling-sensing) | Ottawa, Ontario, Canada |  |  |
| 2026-11-02 | MDA Space | [Satellite Bus Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=e9f6a21e-c486-4ebf-9a82-7fb787af7f51) | Sainte-Anne-de-Bellevue, Quebec, Canada |  |  |
| 2026-11-02 | MDA Space | [Satellite Electrical Propulsion Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=13713581-7e6f-4ed1-8a9b-7a9be4e13a78) | Sainte-Anne-de-Bellevue, Quebec, Canada |  |  |
| 2026-11-02 | MDA Space | [Satellite Flight Software (FSW) Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=540fc56c-c323-46d2-8999-8ecc0a2cf271) | Sainte-Anne-de-Bellevue, Quebec, Canada |  |  |
| 2026-11-02 | MDA Space | [Satellite TT&C/PDT Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=465bf57b-6fac-47dc-9e26-25109058ab70) | Sainte-Anne-de-Bellevue, Quebec, Canada |  |  |
| 2026-11-02 | Qualcomm | [Digital Design Engineer Intern](https://qualcomm.eightfold.ai/careers/job/446721913672) | Toronto, ON, Canada | Summer 2027 |  |
| 2026-11-02 | Qualcomm | [SoC Engineering Intern](https://qualcomm.eightfold.ai/careers/job/446721914045) | Markham, ON, Canada | Summer 2027 |  |
| 2026-11-02 | Qualcomm | [Verification Engineer Intern](https://qualcomm.eightfold.ai/careers/job/446721913769) | Toronto, ON, Canada | Summer 2027 |  |
| 2026-11-02 | Rocket Lab | [Electrical Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7990043003) | Toronto, CAN; Long Beach, CA; Pasadena, CA | Summer 2027 | 🇺🇸 |
| 2026-11-01 | Spaceium | [Electrical Intern](https://job-boards.greenhouse.io/spaceium/jobs/4368438009) | Ottawa, ON, Canada |  |  |
| 2026-10-30 | Altera | [FPGA Development Tools - Intern](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools---Intern_R03394) | Toronto, Ontario, Canada |  |  |
| 2026-10-30 | AMD | [Systems Design Engineer](https://careers.amd.com/jobs/93526?lang=en-us) | MARKHAM, Canada |  |  |
| 2026-10-30 | MDA Space | [Engineering Student - FPGA Designer - Winter 2027](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=216d347b-2abb-43e8-8fbc-268adecf0aa3) | Sainte-Anne-de-Bellevue, Quebec, Canada | Winter 2027 |  |
| 2026-10-30 | MDA Space | [Engineering Student - FPGA Verification - Winter 2027](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=e40bbead-0940-4adb-9ae8-2b3d4d3d6874) | Sainte-Anne-de-Bellevue, Quebec, Canada | Winter 2027 |  |
| 2026-10-30 | Qualcomm | [Camera HW ASIC Verification Intern](https://qualcomm.eightfold.ai/careers/job/446721829462) | Vancouver, BC, Canada | Summer 2027 |  |
| 2026-10-30 | Qualcomm | [Camera Systems Intern](https://qualcomm.eightfold.ai/careers/job/446721876037) | Vancouver, BC, Canada | Summer 2027 |  |
| 2026-10-30 | Qualcomm | [High-Speed Electrical and Optical Systems Validation Co-op Intern - Interim Engineering Intern - HW](https://qualcomm.eightfold.ai/careers/job/446721874877) | Ottawa, ON, Canada | Winter 2027 |  |
| 2026-10-30 | Tenstorrent | [Software Engineer, Acceleration Kernel Development](https://job-boards.greenhouse.io/tenstorrent/jobs/4155609007) | Santa Clara, California, United States; Toronto, Ontario, Canada |  |  |
| 2026-10-27 | Ciena | [Optical Performance Lab Verification and Testing Co-op](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Optical-Performance-Lab-Verification-and-Testing-Co-op_R031991) | Ottawa, ON, Canada | Winter 2027 |  |
| 2026-10-21 | Qualcomm | [Display Systems Engineer Intern](https://qualcomm.eightfold.ai/careers/job/446721661677) | Markham, ON, Canada | Summer 2027 |  |
| 2026-10-19 | NVIDIA | [ASIC Verification Intern](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/Canada-Toronto/ASIC-Verification-Intern---Summer-2027_JR2027982) | Toronto, ON, Canada | Summer 2027 |  |
| 2026-10-19 | Qualcomm | [QDSP Hardware Physical Design Intern](https://qualcomm.eightfold.ai/careers/job/446721636316) | Markham, ON, Canada | Summer 2027 |  |
| 2026-10-16 | MDA Space | [Engineering Student,  Systems Design (Project Engineering) - Winter 2027](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=ea57438a-cb1d-44e0-96a0-b9d680cf5e7b) | Brampton, Ontario, Canada | Winter 2027 |  |
| 2026-10-16 | SiTime | [ASIC Digital Verification Engineer Co-op](https://job-boards.greenhouse.io/sitimecorporation/jobs/4452852009) | Ottawa, ON, Canada | Winter 2027 |  |
| 2026-10-16 | SiTime | [ASIC Digital Verification Engineer Intern](https://job-boards.greenhouse.io/sitimecorporation/jobs/4451161009) | Ottawa, ON, Canada |  |  |
| 2026-10-15 | Nokia | [Embedded C/C++ Software Developer Co-op Intern](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/41311) | Ottawa, ON, Canada | Winter 2027 |  |
| 2026-10-15 | Nokia | [Embedded C/C++ SW Developer Co-op/Intern](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/41311) | Ottawa, Ontario |  |  |
| 2026-10-14 | Analog Devices | [Embedded Software Engineer Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-MA-Wilmington/Embedded-Software-Engineer-Intern_R266132) | US, MA, Wilmington; US, CA, San Jose, Rio Robles; US, NC, Durham; Toronto, ON, Canada; Vancouver, BC, Canada |  |  |
| 2026-10-14 | Astera Labs | [Firmware Engineer Co-op Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4739544005) | Vancouver, BC, Canada | Spring 2027 |  |
| 2026-10-14 | Cadence | [Analog/Mixed-Signal IC Design Co-Op/Intern  (Summer 2026) / Stage/Co-Op en Conception de CI Analogiques/Signal Mixte (Été  2026)](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/MOUNT-ROYAL-Montreal/Analog-Mixed-Signal-IC-Design-Co-Op-Intern---Summer-2026----Stage-Co-Op-en-Conception-de-CI-Analogiques-Signal-Mixte--t--2026-_R53993-2) | MOUNT-ROYAL (Montreal) | Summer 2026 |  |
| 2026-10-14 | Lumentum | [Electrical Engineer Intern Co-op](https://lumentum.wd5.myworkdayjobs.com/LITE/job/Canada---Ottawa-Bill-Leathem/Electrical-Engineer-Co-op-Intern_20261433) | Ottawa, ON, Canada | Winter 2027 |  |
| 2026-10-14 | MDA Space | [Engineering Student - Electronics Production and AI&T -  Winter 2027](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=4620a5ce-7260-4d2c-bb1a-d6beff72610e) | Sainte-Anne-de-Bellevue, Quebec, Canada | Winter 2027 |  |
| 2026-10-14 | Tenstorrent | [Systems Intern - Multiple Teams](https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/5264407007) | Toronto, ON, Canada; Vancouver, BC, Canada |  |  |
| 2026-10-13 | Astera Labs | [Analog/Mixed-Signal IC Design Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4739756005) | Toronto, ON, Canada |  | 🎓 |
| 2026-10-13 | Astera Labs | [Design Verification Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4743360005) | San Jose, CA; Toronto, ON, Canada |  |  |
| 2026-10-06 | Astera Labs | [Digital Design Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4731399005) | Toronto, ON, Canada |  |  |
| 2026-10-06 | Astera Labs | [Physical Design Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4729022005) | San Jose, CA; Toronto, ON, Canada |  |  |
| 2026-10-06 | Lumentum | [Embedded Software Engineer Co-op Intern](https://lumentum.wd5.myworkdayjobs.com/LITE/job/Canada---Ottawa-Bill-Leathem/Embedded-Software-Engineer-Co-op-Intern_20261370) | Ottawa, ON, Canada |  |  |
| 2026-10-06 | MDA Space | [Engineering Student - Digital Electronics Test Station Design - Winter 2027](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=080ac9a6-c9f4-4d51-bcf6-b4085e35e941) | Sainte-Anne-de-Bellevue, Quebec, Canada | Winter 2027 |  |
| 2026-10-06 | MDA Space | [Engineering Student - Systems - Winter 2027](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=f0e69c62-7bd2-48e9-b3d5-e419027d2712) | Sainte-Anne-de-Bellevue, Quebec, Canada | Winter 2027 |  |
| 2026-10-06 | Tenstorrent | [Hardware Intern - AI HW & System on a Chip](https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/5256568007) | Toronto, ON, Canada; Ottawa, ON, Canada |  |  |
| 2026-10-05 | Hitachi Energy | [Electrical Component Engineer Intern](https://hitachi.wd1.myworkdayjobs.com/hitachi/job/Toronto-Ontario-Canada/Electrical-Component-Engineering-Intern--Winter-2027--16months-_R0145359) | Toronto, ON, Canada | Summer 2027 |  |
| 2026-10-05 | Lumentum | [Embedded Software Developer Co-op - Optical Circuit Switch](https://lumentum.wd5.myworkdayjobs.com/LITE/job/Canada---Ottawa-Bill-Leathem/Embedded-Software-Developer-Co-op--Optical-Circuit-Switch-_20261320) | Ottawa, ON, Canada | Winter 2027 |  |
| 2026-10-02 | Hitachi Energy | [Hardware Test Engineering Intern](https://hitachi.wd1.myworkdayjobs.com/hitachi/job/Toronto-Ontario-Canada/Hardware-Test-Engineering-Intern--Summer-2027--16months-_R0142476) | Toronto, ON, Canada | Summer 2027 |  |
| 2026-10-02 | Marvell | [Firmware Engineer Intern](https://marvell.wd1.myworkdayjobs.com/MarvellCareers/job/Santa-Clara-CA/Firmware-Engineer-Intern--MS---Summer-2027_2604513) | Santa Clara, CA; Westlake Village, CA; Ottawa, ON, Canada | Winter 2027, Summer 2027, Fall 2027, Winter 2028, Spring 2028, Summer 2028 | 🎓 |
| 2026-09-24 | Marvell | [Analog Design Intern Co-op - Master’s](https://marvell.wd1.myworkdayjobs.com/MarvellCareers/job/Toronto-Canada/Analog-Design-Intern--Master-s---2027-Co-Op_2603862) | Toronto, ON, Canada | Summer 2027 | 🎓 |
| 2026-09-24 | Semtech | [Analog Design Intern](https://semtech.wd1.myworkdayjobs.com/SemtechCareers/job/CAN---Ottawa-ON/Analog-Design-Intern_REQ3625) | Ottawa, ON, Canada | Summer 2027 |  |
| 2026-09-24 | Semtech | [Digital IC Design Intern](https://semtech.wd1.myworkdayjobs.com/SemtechCareers/job/CAN---Ottawa-ON/Digital-IC-Design-Engineering-Intern_REQ3620) | Ottawa, ON, Canada | Summer 2027 |  |
| 2026-09-24 | Semtech | [Firmware Intern](https://semtech.wd1.myworkdayjobs.com/SemtechCareers/job/CAN---Ottawa-ON/Firmware-Design-Intern_REQ3617) | Ottawa, ON, Canada | Summer 2027 |  |
| 2026-09-23 | Qualcomm | [Firmware Development Intern - PAL](https://qualcomm.eightfold.ai/careers/job/446721229661) | Markham, ON, Canada | Summer 2027 |  |
| 2026-09-22 | Ciena | [ASIC Engineer Intern](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Engineer-Intern_R031750) | Ottawa, ON, Canada | Winter 2027 |  |
| 2026-09-17 | Qualcomm | [Firmware Engineer Intern - Embedded Software Engineering - Embedded Firmware and SDK Development](https://qualcomm.eightfold.ai/careers/job/446721141411) | Toronto, ON, Canada | Summer 2027 |  |
| 2026-09-11 | Amazon | [ML Systems Software Development Engineer Intern, Annapurna Labs - 2027](https://www.amazon.jobs/en/jobs/10538066) | Toronto, Ontario, CAN |  |  |
| 2026-09-09 | Amazon | [Software Development Engineer Intern, ROBOTICS - 2027](https://www.amazon.jobs/en/jobs/10535280) | Toronto, Ontario, CAN |  |  |
| 2026-09-02 | Huawei | [Co-op Engineer - openJiuwen AI Agent Platform](https://huaweicanada.recruitee.com/o/co-op-engineer-openjiuwen-ai-agent-platform) | Markham, Ontario, Canada |  |  |
| 2026-05-25 | Spaceium | [Electrical Engineer Intern](https://job-boards.greenhouse.io/spaceium/jobs/4258525009) | Ottawa, ON, Canada |  |  |
| 2025-12-03 | Amazon | [Robotics - Software Development Engineer Intern - 2026 - Toronto](https://www.amazon.jobs/en/jobs/3136815) | Toronto, Ontario, CAN |  |  |

### United States (440)

| Posted | Company | Role | Location | Term | Flags |
|--------|---------|------|----------|------|-------|
| 2026-11-13 | Amazon | [2027 Applied Science Internship - Robotics - United States](https://www.amazon.jobs/en/jobs/10604778) | North Reading, Massachusetts, USA |  |  |
| 2026-11-13 | Lightmatter | [Hardware Test Engineering, Intern (Summer 2027)](https://boards.greenhouse.io/lightmatter/jobs/5473869008?gh_jid=5473869008) | Mountain View, CA | Summer 2027 |  |
| 2026-11-13 | Lightmatter | [Physical Design, Intern (Summer 2027)](https://boards.greenhouse.io/lightmatter/jobs/5481668008?gh_jid=5481668008) | Boston, MA | Summer 2027 |  |
| 2026-11-13 | Micron | [Intern -  AI Engineer Platform](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---Main-Site/Intern----AI-Engineer-Platform_JR115934) | Boise, ID - Main Site |  |  |
| 2026-11-13 | SpaceX | [Propulsion Engineer, Stage Systems (Starship)](https://boards.greenhouse.io/spacex/jobs/8901004002?gh_jid=8901004002) | Starbase, TX |  | 🇺🇸 |
| 2026-11-13 | Texas Instruments | [Analog Design Eng Intern (GaN Device)](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25016345) | Santa Clara, CA, United States |  |  |
| 2026-11-13 | Texas Instruments | [Analog Design Eng Intern - High-Speed/RF](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25016352) | Santa Clara, CA, United States |  |  |
| 2026-11-13 | Texas Instruments | [Analog Design Eng Intern - High-speed/RF/mm-wave](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25016349) | Dallas, TX, United States |  |  |
| 2026-11-13 | Texas Instruments | [Analog Design Eng Intern - Power](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25019495) | Dallas, TX, United States |  |  |
| 2026-11-12 | Analog Devices | [Mechanical Engineer - Advanced Robotics Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-MA-Wilmington/Mechanical-Engineer---Advanced-Robotics-Intern_R268505) | US, MA, Wilmington |  |  |
| 2026-11-12 | Astranis | [Electrical Integration Intern - RF (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4715788006) | San Francisco | Summer 2027 | 🇺🇸 |
| 2026-11-12 | Astranis | [Electrical Reliability Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704784006) | San Francisco | Summer 2027 | 🇺🇸 |
| 2026-11-12 | Astranis | [Embedded Software Developer, Network/Payload Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704569006) | San Francisco, CA | Winter 2027, Summer 2027 | 🇺🇸 |
| 2026-11-12 | Astranis | [FPGA Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704803006) | San Francisco, CA | Winter 2027, Summer 2027 | 🇺🇸 |
| 2026-11-12 | Astranis | [Hardware Test Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4707012006) | San Francisco, CA | Winter 2027 | 🇺🇸 |
| 2026-11-12 | Astranis | [RF Hardware Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4708417006) | San Francisco | Winter 2027 | 🇺🇸 |
| 2026-11-12 | Astranis | [Software Defined Radio Hardware Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4716087006) | San Francisco, CA | Winter 2027 | 🇺🇸 |
| 2026-11-12 | Astranis | [Software Engineer - Enterprise Systems Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4705610006) | San Francisco, CA | Summer 2027 | 🇺🇸 |
| 2026-11-12 | CACI | [Embedded Software Development Intern](https://caci.wd1.myworkdayjobs.com/external/job/Denver-CO-US/Embedded-Software-Development-Intern---Summer-2027_333147) | Westminster, CO | Summer 2027 |  |
| 2026-11-12 | Entegris | [Embedded Software Engineer Intern](https://entegris.wd1.myworkdayjobs.com/entegriscareers/job/Bloomington-MN/Embedded-Software-Engineering-Intern_REQ-15870) | Bloomington, MN | Summer 2027 |  |
| 2026-11-12 | North Atlantic Industries | [Embedded Software Engineer Intern](https://recruiting.paylocity.com/Recruiting/Jobs/Details/4663112) | Bohemia, NY | Spring 2027 |  |
| 2026-11-12 | Shield AI | [Hardware Test Engineering Co-op](https://jobs.ashbyhq.com/f7d8749a-72d6-407c-bf98-292ea630c73a/ec8a822c-ccbf-4b4e-b41c-2f0db5c8342d/application?embed=true) | Dallas, TX | Summer 2027 |  |
| 2026-11-12 | SK hynix | [Embedded Software Engineer Intern](https://job-boards.greenhouse.io/skhynixmemorysolutionsamericainc/jobs/4504499009) | San Jose, CA | Winter 2027 |  |
| 2026-11-12 | Waymo | [2027 Summer Intern, MS/PhD, Machine Learning, Driver Refinement Foundations](https://careers.withwaymo.com/jobs?gh_jid=8243556) | Mountain View, CA, USA; San Francisco, CA, USA | Summer 2027 | 🎓 |
| 2026-11-12 | Waymo | [2027 Summer Intern, MS/PhD, ML Systems & Behavior Discovery](https://careers.withwaymo.com/jobs?gh_jid=8257159) | Mountain View, CA, USA | Summer 2027 | 🎓 |
| 2026-11-12 | Waymo | [2027 Summer Intern, MS/PhD, Perception Systems Engineering: Pedestrian Detection Precision](https://careers.withwaymo.com/jobs?gh_jid=8234670) | San Francisco, California | Summer 2027 | 🎓 |
| 2026-11-12 | Waymo | [2027 Summer Intern, MS/PhD, Perception, Robotics](https://careers.withwaymo.com/jobs?gh_jid=8227633) | Mountain View, CA, USA | Summer 2027 | 🎓 |
| 2026-11-12 | Waymo | [2027 Summer Intern, MS/PhD, Software Engineer, Onboard Developer Platform](https://careers.withwaymo.com/jobs?gh_jid=8240198) | Mountain View, CA, USA | Summer 2027 | 🎓 |
| 2026-11-12 | Waymo | [2027 Summer Intern, MS/PhD, Systems Engineer, Autonomous Vehicle Networks & Diagnostics](https://careers.withwaymo.com/jobs?gh_jid=8231711) | Mountain View, CA, USA | Summer 2027 | 🎓 |
| 2026-11-12 | Zoox | [Firmware Engineer Intern - FW Core System Services](https://jobs.lever.co/zoox/54be0f19-9a45-466d-89bc-bc72dd3f9d68/apply) | Seattle, WA; Foster City, CA; San Diego, CA |  |  |
| 2026-11-12 | Zoox | [Systems & Safety Engineering Intern [Summer 2027]](https://jobs.lever.co/zoox/442845d1-33b0-4801-a553-7fd9b806e46f) | Foster City, CA | Summer 2027 |  |
| 2026-11-11 | Entrust | [Electrical Engineer Co-op](https://entrust.wd1.myworkdayjobs.com/entrustcareers/job/United-States---Shakopee-MN-GHQ/Electrical-Engineer-Co-op_R004413) | Shakopee, MN |  |  |
| 2026-11-11 | GlobalFoundries | [AI Processor Hardware/Software Integration Engineer Intern](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---Texas---Richardson/AI-Processor-Hardware-Software-Integration-Engineer-Intern--Summer-2027-_JR-2604028) | Richardson, TX | Summer 2027 |  |
| 2026-11-11 | Infineon | [Internship - Analog Mixed Signal Design](https://jobs.infineon.com/careers/job/563808971905261) | El Segundo, CA, US |  |  |
| 2026-11-11 | KLA | [Electrical Engineering Intern](https://kla.wd1.myworkdayjobs.com/Search/job/Ann-Arbor-MI/Electrical-Engineering-Intern_2642897-2) | Ann Arbor, MI; Milpitas, CA |  |  |
| 2026-11-11 | Lightmatter | [Laser Firmware Intern - Summer 2027](https://boards.greenhouse.io/lightmatter/jobs/5479596008?gh_jid=5479596008) | Boston, MA | Summer 2027 |  |
| 2026-11-11 | Motorola Solutions | [Embedded Software Engineer Intern](https://motorolasolutions.wd5.myworkdayjobs.com/Careers/job/Schaumburg-IL/XMLNAME-2027-Summer-Embedded-SW-Engineering-Intern_R67741-1) | Schaumburg, IL, USA | Summer 2027 |  |
| 2026-11-11 | MSA Safety | [Electrical Engineering Technology Intern Co-op](https://careers.msasafety.com/jobs/10392?icims=1&lang=en-us) | Cranberry Township, PA | Summer 2027 |  |
| 2026-11-11 | RTX | [Electrical Components Engineer Intern](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-AZ-TUCSON-M10--3360-E-Hemisphere-Loop--BLDG-M10/Electrical-Components-Engineer-Intern--Summer-2027---Onsite-_01888885) | Tucson, AZ | Summer 2027 |  |
| 2026-11-11 | RTX | [Electrical Engineer Intern - FCS Hardware](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-193--1120-Collins-Rd-NE--BLDG193/Electrical--FCS-Hardware--Engineering-Intern--Summer-2027--Onsite-_01888815) | Cedar Rapids, IA | Summer 2027 |  |
| 2026-11-11 | RTX | [Electrical Engineer Intern - Firmware](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IN-FT-WAYNE-150A--1010-Production-Rd--BLDG-150A/Electrical--Firmware--Engineering-Intern--Summer-2027--Onsite-_01888316) | Fort Wayne, IN, USA | Summer 2027 |  |
| 2026-11-11 | RTX | [Electrical Engineer Intern - Test Solutions](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-MA-TEWKSBURY-TB2--50-Apple-Hill-Dr--SUDBURY-BLDG-Tewksbury-Tb2-200-Sudbury/Electrical-Engineering-Intern---Test-Solutions_01887669) | Tewksbury, MA |  |  |
| 2026-11-11 | Zoox | [Contract Student Worker  – Firmware Engineer (FW Core System Services)](https://jobs.lever.co/zoox/54be0f19-9a45-466d-89bc-bc72dd3f9d68) | Foster City, CA |  |  |
| 2026-11-10 | Etched | [Chip Simulation Software Intern](https://jobs.ashbyhq.com/Etched/27e5bd6b-9357-45f0-9e79-cfa2bf4eeba8) | San Jose |  |  |
| 2026-11-10 | GlobalFoundries | [CPU IP Design & Verification Intern - RISC-V Processor Development](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---Texas---Austin/CPU-IP-Design---Verification-Intern---RISC-V-Processor-Development--Summer-2027-_JR-2604040) | Austin, TX; Santa Clara, CA | Summer 2027 |  |
| 2026-11-10 | Lightmatter | [Silicon, Hardware, & Photonics Engineering Intern – Summer 2027](https://boards.greenhouse.io/lightmatter/jobs/5425407008?gh_jid=5425407008) | Boston, MA; Mountain View, CA | Summer 2027 |  |
| 2026-11-10 | Meta | [Research Scientist Intern - Audio Systems](https://www.metacareers.com/jobs/1100150399514897) | Sunnyvale, CA |  |  |
| 2026-11-10 | NVIDIA | [Performance Engineering Intern - Platform Performance and Power](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Performance-Engineering-Intern--Platform-Performance-and-Power----Spring-2027_JR2029541) | Canada; Santa Clara, CA; United States | Spring 2027 |  |
| 2026-11-10 | Skydio | [Hardware In Loop (HIL) Software Engineer Intern - Winter 2027](https://jobs.ashbyhq.com/skydio/add7fd86-78e6-483e-98cd-cdfc1029fded) | San Mateo, California, United States | Winter 2027 |  |
| 2026-11-09 | CesiumAstro | [Electrical Engineering Intern - FPGA](https://jobs.lever.co/CesiumAstro/fc86b32c-9320-4da0-80ae-18f02bc37316/apply) | Melbourne, FL | Summer 2027 |  |
| 2026-11-09 | CesiumAstro | [Electrical Engineering Intern - Hardware](https://jobs.lever.co/CesiumAstro/8f54cb68-5803-4fbe-93a9-da5873a67435/apply) | Melbourne, FL | Spring 2027, Summer 2027 |  |
| 2026-11-09 | CesiumAstro | [Embedded Software Engineer Intern](https://jobs.lever.co/CesiumAstro/96e97f22-a5b2-4e95-af84-b4f765343663/apply) | Westminster, CO; Melbourne, FL; Austin, TX | Summer 2027 |  |
| 2026-11-09 | Fresenius Medical Care | [Verification and Validation Systems Engineer Co-op](https://freseniusmedicalcare.wd3.myworkdayjobs.com/fme/job/Lawrence-MA-USA/V-V-Systems-Engineer-Co-op_R0277323) | Lawrence, MA |  |  |
| 2026-11-09 | General Dynamics Mission Systems | [FPGA Engineer Intern](https://careers-gdms.icims.com/jobs/78722/job?mobile=true&needsRedirect=false) | Scottsdale, AZ; Manassas, VA |  |  |
| 2026-11-09 | Hewlett Packard Enterprise | [Wireless Hardware Engineer Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/San-Jose-California-United-States-of-America/Wireless-Hardware-Engineering-Intern_1218701) | San Jose, CA |  |  |
| 2026-11-09 | Keysight Technologies | [Embedded Software Engineer Intern](https://jobs.keysight.com/jobs/55093?icims=1&lang=en-us) | Cambridge, MA |  |  |
| 2026-11-09 | Pivotal Aero | [Electrical Engineering Intern](https://jobs.lever.co/pivotal/442a0450-f911-4ac1-a112-03374217f7fb/apply) | Palo Alto, CA | Summer 2027 |  |
| 2026-11-09 | RTX | [Electronic Warfare Electrical Engineer Intern](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-CA-GOLETA-H01--6380-Hollister-Ave--BLDG-H01/Electronic-Warfare-Electrical-Engineer-Intern--Summer-2027--Onsite-_01886573) | Goleta, CA | Summer 2027 |  |
| 2026-11-09 | RTX | [Systems Engineer Intern](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-143--855-35Th-St-NE--BLDG-143/Systems-Engineering-Intern--Summer-2027---SAOC--Cedar-Rapids--IA--Onsite-_01886221) | Cedar Rapids, IA | Summer 2027 |  |
| 2026-11-09 | Schweitzer Engineering Laboratories | [Hardware Engineer Intern](https://selinc.wd1.myworkdayjobs.com/SEL/job/Washington---Pullman/Engineering-Intern_2026-24373-1) | Pullman, WA |  |  |
| 2026-11-09 | Skydio | [Systems Engineering Intern - Summer 2027](https://jobs.ashbyhq.com/skydio/33f1f123-8cec-4e6a-b125-e8831603a62a) | San Mateo, California, United States | Summer 2027 |  |
| 2026-11-09 | Viavi Solutions | [Digital Hardware Engineer Intern](https://viavisolutions.wd1.myworkdayjobs.com/careers/job/Lenexa-KS-USA/Digital-Hardware-Engineering-Intern_260005289-1) | Lenexa, KS |  |  |
| 2026-11-09 | VIAVI Solutions | [Digital Hardware Engineering Intern](https://viavisolutions.wd1.myworkdayjobs.com/careers/job/Lenexa-KS-USA/Digital-Hardware-Engineering-Intern_260005289-1) | Lenexa, KS, USA |  |  |
| 2026-11-08 | Hewlett Packard Enterprise | [Electrical Hardware Engineer Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Sunnyvale-California-United-States-of-America/Electrical-Hardware-Engineer-Intern_1214992) | Sunnyvale, CA; Spring, TX; Chippewa Falls, WI |  |  |
| 2026-11-08 | Infineon | [Intern - Data Center Power Systems](https://jobs.infineon.com/careers/job/563808971984423) | El Segundo, CA, US |  |  |
| 2026-11-08 | Infineon | [Intern- Analog Design](https://jobs.infineon.com/careers/job/563808972303150) | Austin, TX, US |  |  |
| 2026-11-08 | L3Harris | [Systems Engineering Intern](https://careers.l3harris.com/en/job/salt-lake-city/systems-engineering-intern/4832/100667887008) | Salt Lake City, UT; Forest, VA; Rochester, NY |  |  |
| 2026-11-06 | Astranis | [Embedded Software Developer – Network/Payload Software Intern](https://job-boards.greenhouse.io/astranis/jobs/4704571006) | San Francisco, CA | Winter 2027 |  |
| 2026-11-06 | Danaher | [Firmware Engineer Co-op](https://danaher.wd1.myworkdayjobs.com/DanaherJobs/job/Indianapolis-Indiana-United-States/Firmware-Engineer-Co-op_R1321509) | Indianapolis, IN, USA |  |  |
| 2026-11-06 | GlobalFoundries | [Device Engineer Intern - Silicon Photonics](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---New-York---Malta/Device-Engineering-Intern--Silicon-Photonics--Summer-2027-_JR-2604264) | Malta, NY | Summer 2027 |  |
| 2026-11-06 | L3Harris Technologies | [Electrical Engineering Intern](https://jobs.l3harris.com/job/Salt-Lake-City-Electrical-Engineering-Intern-(Salt-Lake-City,-UT)-UT-84116/1448712800/?ats=successfactors) | Salt Lake City, UT |  |  |
| 2026-11-06 | Zoox | [Hardware Engineer Intern, Vehicle Systems [Summer 2027]](https://jobs.lever.co/zoox/0c32245b-f51d-40d2-8e57-a0be1b744c5b) | Foster City, CA | Summer 2027 |  |
| 2026-11-05 | General Dynamics Mission Systems | [Electrical Engineer Intern](https://careers-gdms.icims.com/jobs/75142/job?mobile=true&needsRedirect=false) | Manassas, VA |  |  |
| 2026-11-05 | General Dynamics Mission Systems | [Engineer Intern - Infrastructure Hardware/Network](https://careers-gdms.icims.com/jobs/75025/job?mobile=true&needsRedirect=false) | Pittsfield, MA |  |  |
| 2026-11-05 | General Dynamics Mission Systems | [Systems Engineer Intern - FCS Auxiliary and Training Systems](https://careers-gdms.icims.com/jobs/74988/job?mobile=true&needsRedirect=false) | Pittsfield, MA |  |  |
| 2026-11-05 | KLA | [Optical Systems Student Engineer](https://kla.wd1.myworkdayjobs.com/Search/job/Milpitas-CA/Optical-Systems-Student-Engineer_2641844-1) | Milpitas, CA |  |  |
| 2026-11-05 | KLA | [Optical Systems Student Engineer Intern](https://kla.wd1.myworkdayjobs.com/UR/job/Milpitas-CA/Optical-Systems-Student-Engineer_2641844) | Milpitas, CA |  | 🎓 |
| 2026-11-05 | Legrand | [Firmware Engineer Intern](https://iadugs.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/1809) | Reno, NV |  |  |
| 2026-11-05 | Meta | [ASIC EDA Infrastructure Engineer Intern](https://www.metacareers.com/jobs/1883872846321140) | Sunnyvale, CA |  |  |
| 2026-11-05 | Neuralink | [Analog and Mixed-Signal IC Design Engineer Intern](https://boards.greenhouse.io/neuralink/jobs/7565469003?gh_jid=7565469003) | South San Francisco, California, United States |  |  |
| 2026-11-05 | Neuralink | [Digital IC Design Engineer Intern](https://boards.greenhouse.io/neuralink/jobs/7090489003?gh_jid=7090489003) | South San Francisco, California, United States |  |  |
| 2026-11-05 | Neuralink | [Electrical Engineer Intern, Implant Embedded Systems](https://boards.greenhouse.io/neuralink/jobs/7702527003?gh_jid=7702527003) | Austin, Texas, United States; South San Francisco, California, United States |  |  |
| 2026-11-05 | Neuralink | [Electrical Engineer Intern, Robotics and Surgery Engineering](https://boards.greenhouse.io/neuralink/jobs/6607398003?gh_jid=6607398003) | South San Francisco, California, United States |  |  |
| 2026-11-05 | Neuralink | [Embedded Software Engineer Intern, Implant Embedded Systems](https://boards.greenhouse.io/neuralink/jobs/6283663003?gh_jid=6283663003) | Austin, Texas, United States; South San Francisco, California, United States |  |  |
| 2026-11-05 | Neuralink | [Firmware Engineer Intern, Robotics and Surgery Engineering](https://boards.greenhouse.io/neuralink/jobs/6648992003?gh_jid=6648992003) | South San Francisco, California, United States |  |  |
| 2026-11-05 | Neuralink | [Manufacturing Intern, Surgery & Robot Hardware](https://boards.greenhouse.io/neuralink/jobs/7666761003?gh_jid=7666761003) | South San Francisco, California, United States |  |  |
| 2026-11-05 | Neuralink | [Mechanical Engineering Intern, Robotics and Surgery Engineering](https://boards.greenhouse.io/neuralink/jobs/6514169003?gh_jid=6514169003) | South San Francisco, California, United States |  |  |
| 2026-11-05 | Neuralink | [Software Engineer Intern, Robotics](https://boards.greenhouse.io/neuralink/jobs/5469305003?gh_jid=5469305003) | Austin, Texas, United States; South San Francisco, California, United States |  |  |
| 2026-11-05 | Peraton | [Electrical Engineer Intern](https://careers-peraton.icims.com/jobs/172055/job?mobile=true&needsRedirect=false) | Topeka, KS | Summer 2027 |  |
| 2026-11-05 | RTX | [Systems Engineering Co-op](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-FL-ST-PETERSBURG-381BD--7401-22nd-Ave-N--BLDG-D/Systems-Engineering-Co-op_01884435) | St. Petersburg, FL; Richardson, TX | Spring 2027 |  |
| 2026-11-05 | Sierra Nevada Corporation | [Firmware Engineer Intern](https://snc.wd1.myworkdayjobs.com/snc_external_career_site/job/Sparks-NV/Firmware-Engineer-Intern--Summer-2027-_R0031233) | Sparks, NV | Summer 2027 |  |
| 2026-11-05 | Texas Instruments | [Analog Design Verification Engineer Intern](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25019663) | Santa Clara, CA |  |  |
| 2026-11-05 | Texas Instruments | [Analog IC Design Engineer Intern](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25019660) | Santa Clara, CA |  |  |
| 2026-11-05 | Texas Instruments | [Digital Design Verification Engineer Intern](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25019665) | Santa Clara, CA |  |  |
| 2026-11-04 | Keysight Technologies | [R&D DSP/FPGA Design Automation Intern](https://jobs.keysight.com/jobs/55153?icims=1) | Santa Rosa, CA |  |  |
| 2026-11-04 | L3Harris Technologies | [Systems Engineer Intern](https://jobs.l3harris.com/job/Nashville-Intern,-Systems-Engineering-TN-37203/1447657800/?ats=successfactors) | Nashville, TN |  |  |
| 2026-11-04 | Logiqal | [Quantum Hardware Intern](https://jobs.ashbyhq.com/logiqal/2734f991-1e21-4c77-bb41-211ffa88449d/application?embed=true) | Princeton, NJ |  |  |
| 2026-11-04 | NVIDIA | [VLSI Timing Methodology Intern](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/VLSI-Timing-Methodology-Intern---Summer-2027_JR2026798) | Canada; Santa Clara, CA; United States | Summer 2027 | 🎓 |
| 2026-11-03 | Bose | [Electrical Engineering Co-op - FPGA and Audio Research Platforms](https://boseallaboutme.wd503.myworkdayjobs.com/Bose_Careers/job/US-MA---Framingham/Electrical-Engineering-Co-op---FPGA-and-Audio-Research-Platforms_R29366) | Framingham, MA |  |  |
| 2026-11-03 | General Dynamics Mission Systems | [Electrical Engineering Intern - FPGA](https://careers-gdms.icims.com/jobs/76081/job?mobile=true&needsRedirect=false) | Middletown, RI |  |  |
| 2026-11-03 | Hewlett Packard Enterprise | [Hardware Engineer Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Sunnyvale-California-United-States-of-America/Hardware-Engineering-Intern_1214064) | Sunnyvale, CA; Spring, TX; Chippewa Falls, WI; Westford, MA |  |  |
| 2026-11-03 | Marvell | [Hardware Signal Integrity Intern](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Hardware-Signal-Integrity-Intern--MS---Summer-2027_2603877) | Santa Clara, CA | Summer 2027 |  |
| 2026-11-03 | Marvell | [Hardware Signal Integrity Intern, MS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Hardware-Signal-Integrity-Intern--MS---Summer-2027_2603877) | Santa Clara, CA | Summer 2027 | 🎓 |
| 2026-11-03 | Meta | [ASIC Engineer Intern - Formal Verification](https://www.metacareers.com/jobs/1450222650641899) | Sunnyvale, CA |  |  |
| 2026-11-03 | Zurn Elkay Water Solutions | [Electrical & Electronics Engineering Intern](https://elkay.wd1.myworkdayjobs.com/Elkay_External/job/Downers-Grove-IL/Electrical---Electronics-Engineering-Intern--Summer-2027-_REQ-020097) | Downers Grove, IL, USA | Summer 2027 |  |
| 2026-11-02 | Anduril | [2027 Electrical Engineer Intern](https://boards.greenhouse.io/andurilindustries/jobs/5148101007?gh_jid=5148101007) | Atlanta, Georgia, United States; Boston, Massachusetts, United States; Broomfield, Colorado, United States; Colorado Springs, Colorado, United States; Costa Mesa, California, United States; Fort Collins, Colorado, United States; Irvine, California, United States; Reston, Virginia, United States; Seattle, Washington, United States; Boston, MA; Seattle, WA; Irvine, CA; Colorado Springs, CO; Reston, VA; Fort Collins, CO; Broomfield, CO; Atlanta, GA; Costa Mesa, CA | Summer 2027 | 🇺🇸 |
| 2026-11-02 | Anduril | [2027 Firmware Engineer Intern](https://boards.greenhouse.io/andurilindustries/jobs/5265158007?gh_jid=5265158007) | Costa Mesa, California, United States; Costa Mesa, CA | Summer 2027 | 🇺🇸 |
| 2026-11-02 | Anduril | [2027 Systems Engineer Intern](https://boards.greenhouse.io/andurilindustries/jobs/5257690007?gh_jid=5257690007) | Boston, Massachusetts, United States; Costa Mesa, California, United States; Fort Collins, Colorado, United States; Reston, Virginia, United States; Seattle, Washington, United States |  | 🇺🇸 |
| 2026-11-02 | Anduril | [Winter 2027 Electrical Engineer Co-op](https://boards.greenhouse.io/andurilindustries/jobs/5236565007?gh_jid=5236565007) | Costa Mesa, California, United States; Quincy, Massachusetts, United States; Quincy, MA; Costa Mesa, CA | Winter 2027 | 🇺🇸 |
| 2026-11-02 | Anduril | [Winter 2027 Robotics Engineer Co-op](https://boards.greenhouse.io/andurilindustries/jobs/5271842007?gh_jid=5271842007) | Quincy, Massachusetts, United States | Winter 2027 | 🇺🇸 |
| 2026-11-02 | Anduril | [Winter 2027 Systems Engineer Co-op](https://boards.greenhouse.io/andurilindustries/jobs/5236599007?gh_jid=5236599007) | Quincy, Massachusetts, United States | Winter 2027 | 🇺🇸 |
| 2026-11-02 | Applied Materials | [2027 Summer Electrical Engineer Intern- Master's (Santa Clara, CA)](https://amat.wd1.myworkdayjobs.com/External/job/Santa-ClaraCA/XMLNAME-2027-Summer-Electrical-Engineer-Intern--Master-s--Santa-Clara--CA-_R2629967) | Santa Clara,CA | Summer 2027 | 🎓 |
| 2026-11-02 | Applied Materials | [Electrical Engineer Intern](https://amat.wd1.myworkdayjobs.com/External/job/Santa-ClaraCA/XMLNAME-2027-Summer-Electrical-Engineer-Intern--Master-s--Santa-Clara--CA-_R2629967) | Santa Clara, CA | Summer 2027 | 🎓 |
| 2026-11-02 | ASML | [Electrical Engineer Co-op Intern](https://asml.wd3.myworkdayjobs.com/asmlext1/job/Wilton-CT-USA/CoOp---Electrical-Engineer--Internship-_J-00356208) | Wilton, CT |  |  |
| 2026-11-02 | GlobalFoundries | [Design Verification Engineer Intern](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---Texas---Richardson/Design-Verification-Engineer-Intern--Summer-2027-_JR-2604024) | Richardson, TX | Summer 2027 |  |
| 2026-11-02 | Micron | [Intern - YE-Electrical Failure Analysis Engineer](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---ID1/Intern---YE-Electrical-Failure-Analysis-Engineer_JR114538) | Boise, ID - ID1 |  |  |
| 2026-11-02 | NASA Jet Propulsion Laboratory | [Electrical & Computer Engineering Intern - Flight Communications and Tracking Section - GNSS, Radiometric & Gravity Sensing Instruments Group](https://citjpl.wd5.myworkdayjobs.com/Jobs/job/JPL-Campus/Academic-Part-Time-Intern_R6220) | Pasadena, CA |  |  |
| 2026-11-02 | NXP Semiconductors | [Hardware/Software System and Application Engineer Intern](https://nxp.wd3.myworkdayjobs.com/en-US/careers/job/Chandler-Office/HW-SW-System-and-Application-Engineer-Intern-Summer-2027_R-10064708) | Chandler, AZ | Summer 2027 |  |
| 2026-11-02 | Rocket Lab | [Fluid Systems Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7986794003) | Long Beach, CA | Summer 2027 | 🇺🇸 |
| 2026-11-02 | Rocket Lab | [Ground Systems Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/8007202003) | Stennis Space Center, MS; Middle River, MD | Spring 2027, Summer 2027 | 🇺🇸 |
| 2026-11-02 | Rocket Lab | [Systems Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7987046003) | Long Beach, CA; Pasadena, CA; Tucson, AZ; Chantilly, VA | Summer 2027 | 🇺🇸 |
| 2026-11-02 | Valmont | [Embedded Systems Engineer Intern](https://valmont.wd1.myworkdayjobs.com/ValmontCareers/job/Valley-NE/Embedded-Systems-Engineering-Intern_R29223) | Valley, NE |  |  |
| 2026-11-02 | Zoox | [Hardware Engineer Intern, Manufacturing Operations [Summer 2027]](https://jobs.lever.co/zoox/53f5297a-fe30-4e1e-ab1c-96db5b23eded) | Foster City, CA | Summer 2027 |  |
| 2026-11-02 | Zoox | [Hardware Engineer Intern, Vehicle Development [Summer 2027]](https://jobs.lever.co/zoox/0accbf9e-9b09-4733-b495-fb6dce13ba62) | Foster City, CA | Summer 2027 |  |
| 2026-10-31 | Applied Materials | [2027 Spring Electrical Engineer Co-op (Billerica, MA)](https://amat.wd1.myworkdayjobs.com/External/job/BillericaMA/XMLNAME-2027-Spring-Electrical-Engineer-Co-op--Billerica--MA-_R2631535-1) | Billerica,MA | Spring 2027 |  |
| 2026-10-30 | Applied Materials | [Summer 2027 Electrical Radio Frequency Engineer Intern- Master's/PhD (Santa Clara, CA)](https://amat.wd1.myworkdayjobs.com/External/job/Santa-ClaraCA/Summer-2027-Electrical-Radio-Frequency-Engineer-Intern--Master-s-PhD--Santa-Clara--CA-_R2629753) | Santa Clara,CA | Summer 2027 | 🎓 |
| 2026-10-30 | GlobalFoundries | [Device Engineering Intern - Silicon Photonics](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---New-York---Malta/Device-Engineering-Intern--Silicon-Photonics--Summer-2027-_JR-2604263) | Malta, NY | Summer 2027 |  |
| 2026-10-30 | Keysight Technologies | [FPGA Design Intern](https://jobs.keysight.com/jobs/55151?icims=1) | Calabasas, CA | Fall 2027 |  |
| 2026-10-30 | Shield AI | [Electrical Engineer Intern - Hardware Test](https://jobs.ashbyhq.com/f7d8749a-72d6-407c-bf98-292ea630c73a/16b044e7-02e2-4657-9b87-782a76b127b1/application?embed=true) | Dallas, TX |  |  |
| 2026-10-30 | Zoox | [Software Engineer Intern, Software Systems [Summer 2027]](https://jobs.lever.co/zoox/8b32157b-ab44-4078-85ea-1d8d7b747a20) | Foster City, CA | Summer 2027 |  |
| 2026-10-29 | CACI | [Systems Engineering Co-op Intern](https://caci.wd1.myworkdayjobs.com/external/job/Rochester-NY-US/Systems-Engineering-Co-op-Intern---Spring-2027_334157) | Rochester, NY | Spring 2027, Summer 2027 |  |
| 2026-10-29 | Diversified Automation | [Hardware Engineering Co-op](https://jobs.lever.co/diversified-automation/7a1f1890-bc5d-4e5e-a510-7fe7f85660d3/apply) | Louisville, KY |  |  |
| 2026-10-29 | Lunar Energy | [Hardware Test Engineer Intern](https://job-boards.greenhouse.io/lunarenergy/jobs/6237015004) | Mountain View, CA | Spring 2027 |  |
| 2026-10-29 | NVIDIA | [VLSI CAD Timing Intern - Applied AI](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/VLSI-CAD-Timing-Intern--Applied-AI---Summer-2027_JR2026799) | Santa Clara, CA; United States | Summer 2027 | 🎓 |
| 2026-10-29 | Toyota Research Institute | [Human Interactive Driving Intern - Platform Research Systems Integration](https://jobs.lever.co/tri/0e7063a7-7761-4843-bc28-bf7870fa44b3/apply) | Los Altos, CA |  | 🎓 |
| 2026-10-29 | V2X | [Electrical Engineer Intern](https://careers.gov2x.com/jobs/63854?icims=1) | Indianapolis, IN, USA | Summer 2027 |  |
| 2026-10-28 | Booz Allen | [Design and Verification Engineer Intern](https://bah.wd1.myworkdayjobs.com/bah_jobs/job/Beavercreek-OH/Design-and-Verification-Engineer-Intern_R0252482) | Beavercreek, OH | Spring 2030 |  |
| 2026-10-28 | Draper | [Analog ASIC Design Intern](https://draper.wd5.myworkdayjobs.com/Draper_Careers/job/Cambridge-MA/Analog-ASIC-Design-Intern--Summer-2027-_JR003085) | Cambridge, MA | Summer 2027 |  |
| 2026-10-28 | Figure AI | [Hardware Reliability Intern [Winter 2027]](https://job-boards.greenhouse.io/figureai/jobs/4613067006) | San Jose, CA | Winter 2027 |  |
| 2026-10-28 | RosaicLabs | [AI Accelerator Design Verification Engineer Intern](https://jobs.lever.co/rosaiclabs/8e3e00f8-5b06-450c-bb63-5cc4fc3136ab/apply) | Austin, TX; Santa Clara, CA |  |  |
| 2026-10-28 | RosaicLabs | [CPU Design Verification Engineer Intern](https://jobs.lever.co/rosaiclabs/11a93b50-2472-4ec9-85d9-c99a3a17405e/apply) | Austin, TX; Santa Clara, CA |  |  |
| 2026-10-28 | RTX | [Electrical Engineer Intern](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-CA-EL-SEGUNDO-E01--2000-E-El-Segundo-Blvd--BLDG-E01/Electrical-Engineering-Intern--Summer-2027-_01883292) | El Segundo, CA | Summer 2027 |  |
| 2026-10-28 | RTX | [Hardware Electrical Engineering Co-op](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-MA-CAMBRIDGE-BBN01--10--50-Moulton-St--MOULTON-B2/Hardware-Electrical-Engineering-Co-Op--Spring-2027-_01883598) | Cambridge, MA | Spring 2027 |  |
| 2026-10-28 | Samsung | [RTL Power Macromodeling Engineer Intern](https://job-boards.greenhouse.io/samsungsemiconductor/jobs/8046830003) | San Jose, CA |  | 🎓 |
| 2026-10-28 | Viavi Solutions | [Hardware Engineer Co-op Intern](https://viavisolutions.wd1.myworkdayjobs.com/careers/job/Germantown-MD-USA/Intern_260005108-1) | Germantown, MD |  |  |
| 2026-10-27 | Boston Dynamics | [Electrical Engineer Co-op](https://bostondynamics.wd1.myworkdayjobs.com/Boston_Dynamics/job/Waltham-Office-POST/Electrical-Engineer-Co-Op_R3315) | Waltham, MA |  |  |
| 2026-10-27 | Cirrus Logic | [Formal Verification Engineer Intern](https://jobs.eu.lever.co/cirrus/533c9938-3d35-48a6-b08b-1dd1675d2bdf/apply) | Austin, TX |  | 🎓 |
| 2026-10-27 | HP IQ | [Electrical Engineer Intern - Hardware](https://job-boards.greenhouse.io/hpiq/jobs/6116396004) | San Francisco, CA | Summer 2027 |  |
| 2026-10-27 | Keysight Technologies | [Electrical Engineering Intern - R&D Design Validation - Test Automation](https://jobs.keysight.com/jobs/55190?icims=1) | Budd Lake, Mt Olive, NJ |  |  |
| 2026-10-27 | Mayo Clinic | [Graduate Engineer Intern - Electronics](https://fa-euwp-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/394029) | Rochester, MN | Summer 2027, Fall 2027 |  |
| 2026-10-26 | Analog Devices | [Embedded Systems Co-Op](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-MA-Boston/Embedded-Systems-Co-Op_R267689) | US, MA, Boston; Boston, MA |  |  |
| 2026-10-26 | Applied Materials | [2027 Summer Electrical Engineering Intern - BS or MS (Gloucester, MA)](https://amat.wd1.myworkdayjobs.com/External/job/GloucesterMA/XMLNAME-2027-Summer-Electrical-Engineering-Intern---BS-or-MS--Gloucester--MA-_R2630812) | Gloucester,MA | Summer 2027 |  |
| 2026-10-26 | Boston Dynamics | [Systems Test Engineer Co-op](https://bostondynamics.wd1.myworkdayjobs.com/Boston_Dynamics/job/Waltham-Office-POST/Systems-Test-Engineer---Co-Op_R3312) | Waltham, MA |  |  |
| 2026-10-26 | General Dynamics Mission Systems | [Systems Engineering Intern - Sonar](https://careers-gdms.icims.com/jobs/75796/job?mobile=true&needsRedirect=false) | Manassas, VA |  |  |
| 2026-10-26 | Morph Labs | [Electrical Engineer Intern](https://job-boards.greenhouse.io/morph/jobs/4467369009) | New York, NY | Winter 2026, Winter 2027 |  |
| 2026-10-26 | Nuro | [Software Engineer, AI Platform - Intern](https://nuro.ai/careersitem?gh_jid=7351061) | Mountain View, California (HQ) |  |  |
| 2026-10-26 | Parallel Systems | [Hardware Engineering Intern - Mechanical and Electrical](https://boards.greenhouse.io/parallel/jobs/5275660007) | Los Angeles, CA | Summer 2027 |  |
| 2026-10-26 | Skydio | [Autonomy Engineer Intern, Autonomy Infrastructure, Systems and Tools, 2027 (HQ)](https://jobs.ashbyhq.com/skydio/ec82eb16-a5b4-46e7-827a-326b33d7d2cb) | San Mateo, California, United States |  |  |
| 2026-10-26 | Skydio | [Autonomy Engineer Intern, Simulation & Robotics, 2027 (HQ)](https://jobs.ashbyhq.com/skydio/6f5caf41-fa1d-4208-9bdc-82c72e5d3f17) | San Mateo, California, United States |  |  |
| 2026-10-26 | Texas Instruments | [Analog Design Engineer Intern](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25018682) | Santa Clara, CA; Dallas, TX |  |  |
| 2026-10-23 | Amazon | [ASIC Engineer Early Career Intern](https://amazon.jobs/en/jobs/10558918/asic-engineer-i-annapurna-labs-early-career-2027) | Seattle, WA; Austin, TX; Cupertino, CA |  |  |
| 2026-10-23 | Amazon | [ASIC Engineer Intern, Summer 2027](https://www.amazon.jobs/en/jobs/10576619) | Sunnyvale, California, USA; Sunnyvale, CA; Seattle, WA; Austin, TX; Cupertino, CA | Summer 2027 |  |
| 2026-10-23 | Amazon | [Cloud Hardware Development Engineer Intern](https://amazon.jobs/en/jobs/10517649/cloud-hardware-development-engineer-intern-annapurna-labs-2027) | Austin, TX; Cupertino, CA | Summer 2027 |  |
| 2026-10-23 | Amazon | [Embedded Firmware Co-op](https://amazon.jobs/en/jobs/10573570/embedded-firmware-co-op-amazon-robotics-spring-2027) | North Reading, MA; Westborough, MA | Spring 2027 |  |
| 2026-10-23 | Amazon | [Hardware Development Engineer Intern,  Summer 2027](https://www.amazon.jobs/en/jobs/10578090) | Sunnyvale, California, USA; Bellevue, Washington, USA; Bellevue, WA; North Reading, MA; Hawthorne, CA; Sunnyvale, CA | Winter 2027, Summer 2027, Fall 2027 |  |
| 2026-10-23 | Amazon | [Software Engineer Intern - Embedded Systems](https://amazon.jobs/en/jobs/10567914/software-development-engineer-intern-embedded-systems-summer-2027-usa) | United States; Redmond, WA; Northridge, LA | Winter 2027, Summer 2027, Fall 2027 |  |
| 2026-10-23 | Intel | [AI Hardware Engineering Intern](https://intel.wd1.myworkdayjobs.com/External/job/US-California-Santa-Clara/AI-Hardware-Engineering-Intern_JR0287533) | US, California, Santa Clara; US, California, Folsom |  |  |
| 2026-10-23 | Multiply Labs | [Robotics Software Engineer Intern](https://jobs.lever.co/multiplylabs/acca98ab-c206-4f71-b7a5-6977e4828586/apply) | San Francisco, CA |  |  |
| 2026-10-23 | Quadric | [RTL Intern](https://jobs.ashbyhq.com/quadric/8bc97324-bcdb-4680-a03c-4c6e590644c2/application?embed=true) | Burlingame, CA |  |  |
| 2026-10-23 | Skydio | [Embedded Software Engineer Intern - Winter 2027](https://jobs.ashbyhq.com/skydio/d79ccbaa-2901-4303-bd90-675db7802366) | San Mateo, California, United States; San Mateo, CA | Winter 2027 |  |
| 2026-10-23 | Upscale AI | [Advanced SerDes & Analog/Mixed-Signal IC Design Intern](https://jobs.lever.co/upscale-ai/2bad3e47-6c00-4ec2-94b5-feb4009619c9/apply) | United States | Summer 2027 | 🎓 |
| 2026-10-22 | Amazon | [System Development Engineer Intern/Co-op, ROBOTICS -  2027](https://www.amazon.jobs/en/jobs/10587087) | North Reading, Massachusetts, USA |  |  |
| 2026-10-22 | Ambarella | [Physical Design Engineer Intern](https://ambarella.wd108.myworkdayjobs.com/ambarella/job/US-Headquarters/Physical-Design-Engineer-Intern_JR100393) | United States |  |  |
| 2026-10-22 | General Dynamics Mission Systems | [Hardware/Electrical Engineer Intern](https://careers-gdms.icims.com/jobs/75776/job?mobile=true&needsRedirect=false) | Scottsdale, AZ |  |  |
| 2026-10-22 | Hewlett Packard Enterprise | [ASIC Engineering Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Durham-North-Carolina-United-States-of-America/ASIC-Engineering-Intern_1214234) | Durham, NC |  | 🎓 |
| 2026-10-22 | Ixian Robotics | [Hardware Intern](https://jobs.ashbyhq.com/ixianrobotics/f974d07a-0186-4cc9-8c63-ef962dd06f0b/application?embed=true) | San Francisco, CA |  |  |
| 2026-10-22 | Peak Energy | [Systems Integration and Test Engineer Intern - Winter 2027](https://peakenergy.com/get-in-touch/careers/jobs?job_id=5185852007&gh_jid=5185852007) | Burlingame, CA | Winter 2027, Summer 2027 |  |
| 2026-10-22 | Rockwell Automation | [Electrical Engineer Intern](https://rockwellautomation.wd1.myworkdayjobs.com/External_Rockwell_Automation/job/Eden-Prairie-Minnesota-United-States/Intern--Electrical-Engineer_R26-8320-1) | Mequon, WI; Eden Prairie, MN |  |  |
| 2026-10-22 | Rockwell Automation | [Firmware Engineer Intern](https://rockwellautomation.wd1.myworkdayjobs.com/External_Rockwell_Automation/job/Mequon-Wisconsin-United-States/Firmware-Engineer-Intern_R26-8321) | Mequon, WI; Eden Prairie, MN |  |  |
| 2026-10-22 | Skydio | [Hardware Test and Reliability Intern - Summer 2027](https://jobs.ashbyhq.com/skydio/36d75e36-eeb2-4399-8887-37c4a5ff5800) | San Mateo, California, United States; San Mateo, CA | Summer 2027 |  |
| 2026-10-22 | Tacit | [System Electrical Engineer Intern](https://jobs.ashbyhq.com/tacit/cadc8b71-ee79-4b44-951b-da7c5a0142eb/application?embed=true) | San Francisco, CA |  | 🎓 |
| 2026-10-21 | Marvell | [Silicon Validation Intern](https://marvell.wd1.myworkdayjobs.com/MarvellCareers/job/Santa-Clara-CA/Silicon-Validation-Intern--BS---Summer-2027_2603850-1) | Santa Clara, CA | Summer 2027 |  |
| 2026-10-21 | Marvell | [Silicon Validation Intern, BS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Silicon-Validation-Intern--BS---Summer-2027_2603850) | Santa Clara, CA | Summer 2027 |  |
| 2026-10-21 | Meta | [Research Intern - Audio Hardware](https://www.metacareers.com/jobs/1445807477756644) | Redmond, WA |  |  |
| 2026-10-21 | The Aerospace Corporation | [Embedded Software Engineer Grad Intern](https://aero.wd5.myworkdayjobs.com/external/job/El-Segundo-CA/XMLNAME-2027-Embedded-Software-Engineering-Grad-Intern_R016950) | El Segundo, CA |  | 🎓 |
| 2026-10-20 | Cummins | [Engineering School-to-Work Intern - Electronics Systems Validation Engineering](https://fa-espx-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/2439243) | Troy, MI |  |  |
| 2026-10-20 | Dell Technologies | [Hardware Engineer 1 Intern](https://iawmqy.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/careers/job/298141) | Austin, TX |  |  |
| 2026-10-20 | Humble Robotics | [Electrical Engineer Intern](https://jobs.lever.co/humble-robotics/b9822bf4-c77c-42ea-a19f-1280ec3ab763/apply) | San Francisco, CA |  |  |
| 2026-10-20 | Humble Robotics | [Embedded Software Engineer Intern](https://jobs.lever.co/humble-robotics/8d1fb5d7-9b07-4fac-8c39-e395dca7f2b3/apply) | San Francisco, CA |  |  |
| 2026-10-20 | Intel | [Design Verification Engineer Intern](https://intel.wd1.myworkdayjobs.com/en-us/external/job/US-Colorado-Fort-Collins/Design-Verification-Graduate-Intern-2027_JR0287651) | Santa Clara, CA; Fort Collins, CO |  | 🎓 |
| 2026-10-20 | Intel | [Design Verification Graduate Intern 2027](https://intel.wd1.myworkdayjobs.com/External/job/US-Colorado-Fort-Collins/Design-Verification-Graduate-Intern-2027_JR0287651) | US, Colorado, Fort Collins; US, California, Santa Clara |  |  |
| 2026-10-20 | Keysight Technologies | [Hardware Engineering Intern](https://jobs.keysight.com/jobs/55112?icims=1) | Santa Rosa, CA |  |  |
| 2026-10-20 | Micron | [Intern - SSD Firmware](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---Main-Site/Intern---SSD-Firmware_JR115210) | Boise, ID - Main Site; San Jose, CA |  |  |
| 2026-10-20 | Micron Technology | [SSD Firmware Intern](https://micron.wd1.myworkdayjobs.com/External/job/San-Jose-CA/Intern---SSD-Firmware_JR115209) | San Jose, CA; Boise, ID |  | 🎓 |
| 2026-10-20 | Rockwell Automation | [Hardware Development Engineer Intern](https://rockwellautomation.wd1.myworkdayjobs.com/External-Rockwell-Automation-Early-Careers/job/Mayfield-Heights-Ohio-United-States/Intern--Hardware-Development-Engineer--May---Aug-2027-_R26-6892-2) | Mayfield Heights, OH | Summer 2027 |  |
| 2026-10-20 | Skydio | [Electrical Engineer Intern](https://jobs.ashbyhq.com/skydio/57336f0f-a8ed-4ede-b6da-d399e5335fe4) | San Mateo, California, United States; San Mateo, CA | Summer 2027 |  |
| 2026-10-20 | Skydio | [Wireless Hardware Engineer Intern - Summer 2027](https://jobs.ashbyhq.com/skydio/1ac972b1-8094-4765-8869-63e1c4d50dea) | San Mateo, California, United States | Summer 2027 |  |
| 2026-10-19 | Badger Meter | [Systems Integration Engineer Intern](https://badgermeter.wd5.myworkdayjobs.com/US_CareerSite/job/US---WI---Milwaukee-HQ/Systems-Integration---Engineering-Intern_4641) | Milwaukee, WI | Summer 2027 |  |
| 2026-10-19 | Heron Power | [Firmware Engineer Intern](http://jobs.ashbyhq.com/heron-power/5dbf22e3-41ba-40de-b428-6fab9934d6da/application?embed=true) | Scotts Valley, CA |  |  |
| 2026-10-19 | Hewlett Packard Enterprise | [Hardware Engineering Design Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Roseville-California-United-States-of-America/Hardware-Engineering-Design-Intern_1214168) | Roseville, CA |  |  |
| 2026-10-19 | Keysight Technologies | [R&D Hardware Engineer Intern](https://jobs.keysight.com/jobs/54804?icims=1) | Santa Clara, CA; Santa Rosa, CA |  |  |
| 2026-10-19 | Meta | [Research Scientist Intern - Robotics Hardware](https://www.metacareers.com/jobs/2105411693413958) | Redmond, WA |  |  |
| 2026-10-18 | Tesla | [Firmware Intern - SoC Firmware Engineer - SI Hardware Infrastructure](https://www.tesla.com/careers/search/job/287024) | Austin, TX | Spring 2027 |  |
| 2026-10-16 | ADT | [Hardware Engineering & Connected Devices Intern](https://fa-erqb-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/3022475) | Boca Raton, FL | Summer 2027 |  |
| 2026-10-16 | AGCO | [Embedded Software Engineer Intern](https://careers.agcocorp.com/job/Hesston-Embedded-Software-Engineering-Intern-Summer-2027-KS-67062/1440993300/?ats=successfactors) | Hesston, KS; Jackson, MN | Summer 2027 |  |
| 2026-10-16 | Figure AI | [Embedded Software Engineering Intern [Winter 2027]](https://job-boards.greenhouse.io/figureai/jobs/4722086006) | San Jose, CA | Winter 2027 |  |
| 2026-10-16 | GlobalFoundries | [Foundation IP Design Verification Intern](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---California---Santa-Clara/Foundation-IP-Design-Verification-Intern--Summer-2027-_JR-2604356) | Santa Clara, CA | Summer 2027 |  |
| 2026-10-16 | Inversion Space | [Avionics Embedded Software Engineer Intern](https://job-boards.greenhouse.io/inversionspace/jobs/4744391005) | Playa Vista, LA | Summer 2027 |  |
| 2026-10-16 | Meta | [Production Systems Engineer Intern](https://www.metacareers.com/jobs/4536253699919879) | Menlo Park, CA |  |  |
| 2026-10-14 | Analog Devices | [Analog Design Engineer Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-MA-Wilmington/Analog-Design-Engineer-Intern_R265297) | US, MA, Wilmington; US, CA, San Jose, Rio Robles; US, NC, Durham |  |  |
| 2026-10-14 | Analog Devices | [Digital Design Engineer Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-NC-Durham/Digital-Design-Engineer-Intern_R265298) | US, NC, Durham; US, CA, San Jose, Rio Robles |  |  |
| 2026-10-14 | Analog Devices | [Mixed Signal Engineer Intern](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-MA-Wilmington/Mixed-Signal-Engineer-Intern_R265299) | US, MA, Wilmington; US, NC, Durham |  |  |
| 2026-10-14 | Applied Materials | [2027 Summer Electrical Engineer  Intern (Controls/PCB) - BS or MS (Gloucester, MA)](https://amat.wd1.myworkdayjobs.com/External/job/GloucesterMA/XMLNAME-2027-Summer-Electrical-Engineer--Intern--Controls-PCB----BS-or-MS--Gloucester--MA-_R2630658) | Gloucester,MA | Summer 2027 |  |
| 2026-10-14 | Applied Materials | [2027 Summer Intern - Electrical Engineer - BS/MS Degree, (Santa Clara)](https://amat.wd1.myworkdayjobs.com/External/job/Santa-ClaraCA/XMLNAME-2027-Summer-Intern---Electrical-Engineer---BS-MS-Degree---Santa-Clara-_R2629428) | Santa Clara,CA | Summer 2027 |  |
| 2026-10-14 | Cadence | [CST Application Engineer Intern - Physical Systems](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/SAN-JOSE/CST-Application-Engineer-Intern---Physical-Systems_R56702-2) | SAN JOSE |  |  |
| 2026-10-14 | Cadence | [CST Application Engineer Intern - Silicon](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/SAN-JOSE/CST-Application-Engineer-Intern---Silicon_R56655-1) | SAN JOSE |  |  |
| 2026-10-14 | Cadence | [CST Application Engineer Intern - Systems ATX](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/SAN-JOSE/CST-Application-Engineer-Intern---Systems-ATX_R56800-3) | SAN JOSE |  |  |
| 2026-10-14 | Cadence | [Product Engineering Internship, Electronics Hardware Design (Fall 2026)](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/Burlington-MA/Product-Engineering-Internship--Electronics-Hardware-Design--Fall-2026-_R54158-2) | Burlington, MA | Fall 2026 |  |
| 2026-10-14 | Figure | [Embedded Software Engineer Intern - Platform](https://job-boards.greenhouse.io/figureai/jobs/4722086006) | San Jose, CA |  |  |
| 2026-10-14 | Formlabs | [Hardware Systems Integration Intern](https://careers.formlabs.com/job/8212683/apply/?gh_jid=8212683) | Somerville, MA | Winter 2027, Spring 2027, Summer 2027 |  |
| 2026-10-14 | Indie | [Design Verification Engineer Intern](https://www.indie.inc/careers/internships/current-openings/?gh_jid=5265698007) | Aliso Viejo, CA |  |  |
| 2026-10-14 | KLA | [Mechatronics/Systems Engineering Internship](https://kla.wd1.myworkdayjobs.com/Search/job/Milpitas-CA/Mechatronics-Systems-Engineering-Internship_2641532-1) | Milpitas, CA |  |  |
| 2026-10-14 | Marvell | [AI-Native Development Platform Engineer Intern, MS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/AI-Native-Development-Platform-Engineer-Intern--MS---Summer-2027_2603848) | Santa Clara, CA | Summer 2027 | 🎓 |
| 2026-10-14 | Marvell | [Electrical Validation Intern, BS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Electrical-Validation-Intern--BS---Summer-2027_2603795) | Santa Clara, CA | Summer 2027, Fall 2027, Winter 2028, Spring 2028, Summer 2028 |  |
| 2026-10-14 | Marvell | [Firmware Engineer Intern, BS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Firmware-Engineer-Intern--BS---Summer-2027_2604461-1) | Santa Clara, CA; Westlake Village, CA | Summer 2027 |  |
| 2026-10-14 | Marvell | [Firmware Engineer Intern, MS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Firmware-Engineer-Intern--MS---Summer-2027_2604513-1) | Santa Clara, CA | Summer 2027 | 🎓 |
| 2026-10-14 | Marvell | [Hardware Engineer Intern, BS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Hardware-Engineer-Intern--BS---Summer-2027_2604975) | Santa Clara, CA | Summer 2027 |  |
| 2026-10-14 | Marvell | [Security Verification/Validation Engineer Intern, BS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Chandler-AZ/Security-Verification-Validation-Engineer-Intern--BS---Summer-2027_2604148) | Chandler, AZ | Summer 2027 |  |
| 2026-10-14 | Micron | [Intern - Next Gen HBM Platform Arch](https://micron.wd1.myworkdayjobs.com/External/job/Folsom-CA/Intern---Next-Gen-HBM-Platform-Arch_JR112993) | Folsom, CA |  |  |
| 2026-10-14 | Micron | [Intern - SSD Firmware - CICD](https://micron.wd1.myworkdayjobs.com/External/job/Longmont-MAX--Office-CO/Intern---SSD-Firmware---CICD_JR114542) | Longmont-MAX- Office, CO |  |  |
| 2026-10-14 | Micron | [Intern - SSD Hardware Engineering](https://micron.wd1.myworkdayjobs.com/External/job/Longmont-MAX--Office-CO/Intern---SSD-Hardware-Engineering_JR114232) | Longmont-MAX- Office, CO |  |  |
| 2026-10-14 | Micron | [Intern – DRAM Technology Physical Design and Block-Level PPA Optimization](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---Main-Site/Intern---DRAM-Technology-Physical-Design-and-Block-Level-PPA-Optimization_JR109584) | Boise, ID - Main Site |  |  |
| 2026-10-14 | Nordson | [Electrical Engineer Intern](https://nordsonhcm.wd501.myworkdayjobs.com/nordsoncareers/job/USA---South-Carolina---Clinton/Electrical-Engineering-Intern_REQ53355) | Clinton, SC |  |  |
| 2026-10-14 | Rockwell Automation | [Electrical Engineer Co-op](https://rockwellautomation.wd1.myworkdayjobs.com/External_Rockwell_Automation/job/Chelmsford-Massachusetts-United-States/Co-op--Electrical-Engineer--June---Dec-2027-_R26-7706-1) | Chelmsford, MA | Summer 2027, Fall 2027 |  |
| 2026-10-14 | Rockwell Automation | [Hardware Development Engineer Co-op](https://rockwellautomation.wd1.myworkdayjobs.com/External-Rockwell-Automation-Early-Careers/job/Mayfield-Heights-Ohio-United-States/Co-op--Hardware-Development-Engineer--Jan---July-2027-_R26-6638) | Mayfield Heights, OH | Winter 2027, Summer 2027, Fall 2027 |  |
| 2026-10-13 | Amazon | [Hardware Development Engineer Intern/Co-Op, ROBOTICS - 2027](https://www.amazon.jobs/en/jobs/10535282) | North Reading, Massachusetts, USA; North Reading, MA; Westborough, MA | Winter 2027, Spring 2027, Summer 2027, Fall 2027 |  |
| 2026-10-13 | Astera Labs | [Analog/Mixed Signal System Test Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4739769005) | San Jose, CA |  | 🎓 |
| 2026-10-13 | Astera Labs | [Digital RTL Design Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4739915005) | San Jose, CA |  |  |
| 2026-10-13 | Hewlett Packard Enterprise | [VLSI Design Verification Masters Level Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Ft-Collins-Colorado-United-States-of-America/VLSI-Design-Verification-Masters-Level-Intern_1213425) | Fort Collins, CO |  | 🎓 |
| 2026-10-13 | Keysight Technologies | [R&D Hardware Design Engineer Intern](https://jobs.keysight.com/jobs/54389?icims=1) | Santa Rosa, CA | Spring 2027 |  |
| 2026-10-13 | Motorola | [Electrical Engineer / PCB Designer Intern](https://motorolasolutions.wd5.myworkdayjobs.com/Careers/job/Plantation-FL/Electrical-Engineer---PCB-Designer-Intern---Summer-2027_R69679) | Plantation, FL | Summer 2027 |  |
| 2026-10-13 | Rivian | [Electronics Design Engineering Intern - Low Voltage Electronics](https://careers.rivian.com/jobs/34370?icims=1) | Champaign, IL, USA | Spring 2027 |  |
| 2026-10-13 | Rivian | [UIUC Research Park Intern - Low Voltage Electronics](https://careers.rivian.com/jobs/34370?lang=en-us) | Champaign, Illinois |  |  |
| 2026-10-12 | Bridge Neurotech | [Hardware Engineering Intern](https://jobs.ashbyhq.com/bridgeneurotech/01c03769-b8eb-46c1-b668-469832b99c51/application?embed=true) | Redwood City, CA |  |  |
| 2026-10-12 | Hewlett Packard Enterprise | [ASIC Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Sunnyvale-California-United-States-of-America/ASIC-Intern_1214034) | Sunnyvale, CA |  |  |
| 2026-10-12 | Hewlett Packard Enterprise | [VLSI Design Verification Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Ft-Collins-Colorado-United-States-of-America/VLSI-Design-Verification-Intern_1213399) | Fort Collins, CO |  |  |
| 2026-10-12 | Hewlett Packard Enterprise | [VLSI Logic Design Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Ft-Collins-Colorado-United-States-of-America/VLSI-Logic-Design-Intern_1213412) | Fort Collins, CO; Chippewa Falls, WI |  |  |
| 2026-10-12 | Life Fitness | [Embedded Software Engineer Intern](https://lifefitness.wd1.myworkdayjobs.com/searchLFN/job/Schaumburg-IL-60173/Embedded-Software-Intern_JR-025276) | Schaumburg, IL, USA |  |  |
| 2026-10-12 | Micron Technology | [SSD Hardware Engineering Intern](https://micron.wd1.myworkdayjobs.com/External/job/Longmont-MAX--Office-CO/Intern---SSD-Hardware-Engineering_JR114232) | Longmont, CO |  |  |
| 2026-10-12 | RTX | [Systems Engineer Co-op - Spring/Summer 2027](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-182--1100-Cimmie-Ave-Ne--BLDG-182/Systems-Engineer-Co-Op--Spring-Summer-2027----Onsite_01873686) | Cedar Rapids, IA | Spring 2027, Summer 2027 |  |
| 2026-10-10 | Meter | [Hardware Engineer Intern](https://jobs.ashbyhq.com/meter/a5f1e4c3-2930-4933-ab38-8f600486494b/application?embed=true) | San Francisco, CA |  |  |
| 2026-10-09 | Applied Materials | [Electrical Engineer Intern - Controls/PCB](https://amat.wd1.myworkdayjobs.com/External/job/GloucesterMA/XMLNAME-2027-Summer-Electrical-Engineer--Intern--Controls-PCB----BS-or-MS--Gloucester--MA-_R2630658) | Gloucester, MA | Summer 2027 |  |
| 2026-10-09 | Astera Labs | [Analog Mixed Signal Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4739767005) | San Jose, CA; Irvine, CA |  | 🎓 |
| 2026-10-09 | Hewlett Packard Enterprise | [ASIC Engineer Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Sunnyvale-California-United-States-of-America/ASIC-Engineer-Intern_1216555) | Sunnyvale, CA; Durham, NC |  |  |
| 2026-10-09 | Werfen | [R&D Systems Hardware Engineering Co-op](https://careers-werfen.icims.com/jobs/11153/job?mobile=true&needsRedirect=false) | Bedford, MA |  |  |
| 2026-10-08 | Amazon | [Embedded Firmware Co-op, Amazon Robotics - Spring 2027](https://www.amazon.jobs/en/jobs/10573570) | North Reading, Massachusetts, USA | Spring 2027 |  |
| 2026-10-08 | Figure AI | [Electrical Engineering Intern [Winter 2027]](https://job-boards.greenhouse.io/figureai/jobs/4676467006) | San Jose, CA | Winter 2027 |  |
| 2026-10-08 | Figure AI | [Firmware Engineering Intern [Winter 2027]](https://job-boards.greenhouse.io/figureai/jobs/4601309006) | San Jose, CA | Winter 2027 |  |
| 2026-10-08 | MSA Safety | [Electrical Engineering Co-op](https://careers.msasafety.com/jobs/10163?icims=1) | Cranberry Township, PA | Spring 2027 |  |
| 2026-10-08 | Rugged Robotics | [Electrical Engineer Intern Co-op](https://job-boards.greenhouse.io/ruggedrobotics/jobs/4724214005) | Houston, TX | Spring 2027, Summer 2027 |  |
| 2026-10-08 | StudyFetch | [Robotics Intern - Learning Kits & Curriculum](https://ats.rippling.com/studyfetch/jobs/2ba84837-7cb6-4278-bd58-ad554ee0b8f5) | Beverly Hills, CA |  |  |
| 2026-10-07 | Amazon | [Software Development Engineer (Embedded Systems) Intern, Amazon Leo - Summer 2027 (USA)](https://www.amazon.jobs/en/jobs/10571374) | Redmond, Washington, USA | Summer 2027 |  |
| 2026-10-07 | Entrust | [Firmware Engineer Co-op](https://entrust.wd1.myworkdayjobs.com/entrustcareers/job/United-States---Shakopee-MN-GHQ/Firmware-Engineering-Co-op_R004419) | Shakopee, MN |  |  |
| 2026-10-07 | Figure | [Firmware Engineer Intern](https://job-boards.greenhouse.io/figureai/jobs/4601309006) | San Jose, CA | Winter 2027 |  |
| 2026-10-07 | Garmin | [FPGA Engineer Intern](https://careers.garmin.com/jobs/19836?icims=1) | Olathe, KS | Summer 2027 |  |
| 2026-10-07 | General Motors | [Systems Engineer Intern - Asd](https://generalmotors.wd5.myworkdayjobs.com/en-CA/Careers_GM/job/Milford-Michigan-United-States-of-America/XMLNAME-2027-Summer-Intern--Systems-Engineer--ASD_JR-202621989) | Milford, MI; Warren, MI | Summer 2027 |  |
| 2026-10-07 | Hewlett Packard Enterprise | [ASIC Design Engineer Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Sunnyvale-California-United-States-of-America/ASIC-Design-Engineer-Intern_1214180) | Sunnyvale, CA |  |  |
| 2026-10-07 | Schneider Electric | [Electronics Hardware Engineer Co-op](https://se.jibeapply.com/jobs/134457?icims=1) | Cedar Rapids, IA; Raleigh, NC | Winter 2027, Summer 2027 |  |
| 2026-10-07 | Skyband Systems | [Avionics Hardware & Test Engineer Intern](https://jobs.ashbyhq.com/skyband%20systems/36bb9bd3-7ecb-42fe-908a-7d7486620d77/application?embed=true) | Kirkland, WA | Spring 2027, Summer 2027 |  |
| 2026-10-07 | Texas Instruments | [Analog Design Engineering Intern - ATD](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25015924) | Dallas, TX, United States |  |  |
| 2026-10-06 | Alliance Laundry Systems | [Embedded Firmware Co-op](https://uscareeropenings-alliancelaundry.icims.com/jobs/13348/job?mobile=true&needsRedirect=false) | Ripon, WI | Summer 2027, Fall 2027 |  |
| 2026-10-06 | Astera Labs | [Advanced Design Verification Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4731412005) | San Jose, CA |  |  |
| 2026-10-06 | Astera Labs | [Digital Design Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4731407005) | San Jose, CA |  |  |
| 2026-10-06 | Astera Labs | [Electrical Validation Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4724534005) | San Jose, CA |  |  |
| 2026-10-06 | Astera Labs | [Firmware Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4731584005) | San Jose, CA |  |  |
| 2026-10-06 | Astera Labs | [Firmware Engineer Intern - Optical](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4738565005) | San Jose, CA |  |  |
| 2026-10-06 | Astera Labs | [Hardware Design Engineer Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4728560005) | San Jose, CA |  |  |
| 2026-10-06 | Astera Labs | [Hardware Electrical Validation Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4740145005) | San Jose, CA |  |  |
| 2026-10-06 | Astera Labs | [Platform Software Diagnostics Intern](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4724492005) | San Jose, CA |  |  |
| 2026-10-06 | Atoms | [Electrical Engineer Intern](https://job-boards.greenhouse.io/cssmerge/jobs/8869098002) | San Francisco, CA | Winter 2027, Summer 2027 |  |
| 2026-10-06 | Nokia | [Optical Systems Group Co-op](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/41218) | San Jose, California; San Jose, CA | Spring 2027 | 🎓 |
| 2026-10-06 | NVIDIA | [PCIe Design Verification Intern](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PCIe-Design-Verification-Intern---Spring-2027_JR2026704) | Santa Clara, CA; Austin, TX | Winter 2027, Summer 2027 |  |
| 2026-10-06 | Rivian | [Engineering Intern Co-op - AI/ML ASIC CAD](https://careers.rivian.com/jobs/34059?icims=1) | Palo Alto, CA | Spring 2027 | 🎓 |
| 2026-10-05 | Cirrus Logic | [Analog Design Engineer Intern](https://jobs.eu.lever.co/cirrus/df033a94-155f-427f-a178-88bd18c3d5ec/apply) | Austin, TX | Spring 2027, Summer 2027, Fall 2027 | 🎓 |
| 2026-10-05 | Cirrus Logic | [Design Verification Engineer Intern](https://jobs.eu.lever.co/cirrus/c71a6365-31c7-4ba1-bdc4-9f2df1fc483e/apply) | Austin, TX | Spring 2027, Summer 2027, Fall 2027 | 🎓 |
| 2026-10-05 | Cirrus Logic | [Digital Design Engineer Intern](https://jobs.eu.lever.co/cirrus/0310fbd1-a2a8-4c0f-a842-86e05ae7d98e/apply) | Austin, TX | Spring 2027, Summer 2027, Fall 2027 | 🎓 |
| 2026-10-05 | Cirrus Logic | [Mixed Signal Products Applications Engineer Intern](https://jobs.eu.lever.co/cirrus/2ca7b254-5c91-4a4e-9ba8-d05c8604eca2/apply) | Austin, TX | Summer 2027 |  |
| 2026-10-05 | Marvell | [Hardware Engineer Intern](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Hardware-Engineer-Intern--BS---Summer-2027_2604975) | Santa Clara, CA |  |  |
| 2026-10-05 | Rivian | [Electronics Design Engineer Co-op Intern - Electronics Design](https://careers.rivian.com/jobs/34040?icims=1) | Palo Alto, CA | Spring 2027 |  |
| 2026-10-05 | Rivian | [Engineering Intern - AI/ML ASIC CAD (Spring 2027 Co-Op)](https://careers.rivian.com/jobs/34059?lang=en-us) | Palo Alto, California | Spring 2027 |  |
| 2026-10-05 | Rivian | [Engineering Intern - Electronics Design (Spring 2027 Co-Op)](https://careers.rivian.com/jobs/34040?lang=en-us) | Palo Alto, California | Spring 2027 |  |
| 2026-10-05 | Rivian | [Software Engineer Intern Co-op - Embedded Software](https://careers.rivian.com/jobs/33832?icims=1) | Palo Alto, CA | Spring 2027 |  |
| 2026-10-05 | Rivian | [Software Engineering Intern - Embedded Software (Spring 2027 Co-op)](https://careers.rivian.com/jobs/33832?lang=en-us) | Palo Alto, California | Spring 2027 |  |
| 2026-10-05 | Tesla | [Embedded Software Engineer Intern - Thermal Systems](https://www.tesla.com/careers/search/job/285797) | Palo Alto, CA | Spring 2027 |  |
| 2026-10-05 | Tesla | [Systems Integration Engineering Intern - Thermal Systems](https://www.tesla.com/careers/search/job/285779) | Palo Alto, CA | Spring 2027 |  |
| 2026-10-04 | Hewlett Packard Enterprise | [Electric Hardware Engineer Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Chippewa-Falls-Wisconsin-United-States-of-America/Electric-Hardware-Engineering-Intern_1213414) | Chippewa Falls, WI |  |  |
| 2026-10-02 | Amazon | [Software Development Engineer Intern (Embedded Systems) - Summer 2027 (USA)](https://www.amazon.jobs/en/jobs/10567914) | Seattle, Washington, USA | Summer 2027 |  |
| 2026-10-02 | Arc | [Electrical Hardware Engineering Intern](https://job-boards.greenhouse.io/arcboatcompany/jobs/5442853008) | Torrance, CA | Summer 2027 |  |
| 2026-10-02 | General Motors | [Systems/Calibration Engineer Intern - ADAS Drive](https://generalmotors.wd5.myworkdayjobs.com/en-CA/Careers_GM/job/Milford-Michigan-United-States-of-America/XMLNAME-2027-Summer-Intern---Systems-Calibration-Engineer--ADAS-Drive_JR-202621623) | Milford, MI | Summer 2027 |  |
| 2026-10-02 | Muon Space | [Electrical Engineer Intern](https://job-boards.greenhouse.io/muonspace/jobs/5255112007) | San Jose, CA | Summer 2027 |  |
| 2026-10-01 | Aurora Innovation | [LiDAR Systems Intern](https://jobs.ashbyhq.com/aurora-operations-inc/ce5ad079-0588-402a-aa0e-b5efe0ba28f1/application?embed=true) | Mountain View, CA | Summer 2027 | 🎓 |
| 2026-10-01 | General Dynamics Mission Systems | [Electrical Engineering Co-op](https://careers-gdms.icims.com/jobs/74924/job?mobile=true&needsRedirect=false) | Pittsfield, MA | Fall 2026, Winter 2027 |  |
| 2026-10-01 | Keysight Technologies | [R&D Electrical Engineering Intern](https://jobs.keysight.com/jobs/54665?icims=1) | Colorado Springs, CO |  |  |
| 2026-09-30 | Amazon | [2027 Frontier AI & Robotics Internship (Undergraduate) - United States, Frontier AI & Robotics, Frontier AI & Robotics](https://www.amazon.jobs/en/jobs/10564599) | San Francisco, California, USA |  |  |
| 2026-09-30 | Rivian | [Audio Hardware Engineer Intern Co-op - Audio Hardware and DSP](https://careers.rivian.com/jobs/33874?icims=1) | Palo Alto, CA | Spring 2027 |  |
| 2026-09-30 | Rivian | [Engineering Intern - ASIC DFT (Spring 2027 Co-Op)](https://careers.rivian.com/jobs/33810?lang=en-us) | Palo Alto, California | Spring 2027 |  |
| 2026-09-30 | Rivian | [Engineering Intern - Audio Hardware and DSP (Spring 2027 Co-op)](https://careers.rivian.com/jobs/33874?lang=en-us) | Palo Alto, California | Spring 2027 |  |
| 2026-09-30 | Rivian | [Engineering Intern - Design Verification, Neural Engine (Spring 2027 Co-op)](https://careers.rivian.com/jobs/33833?lang=en-us) | Palo Alto, California | Spring 2027 |  |
| 2026-09-30 | Rivian | [Engineering Intern - Machine Learning Hardware (Spring 2027 Co-op)](https://careers.rivian.com/jobs/33820?lang=en-us) | Palo Alto, California | Spring 2027 |  |
| 2026-09-30 | Rivian | [Engineering Intern - Mechanical Power Electronics (Spring 2027 Co-Op)](https://careers.rivian.com/jobs/33808?lang=en-us) | Normal, Illinois | Spring 2027 |  |
| 2026-09-30 | Rivian | [Engineering Intern Co-op - Machine Learning Hardware](https://careers.rivian.com/jobs/33820?icims=1) | Palo Alto, CA | Spring 2027 |  |
| 2026-09-30 | Rivian | [Engineering Intern/Co-op - Design Verification - Neural Engine](https://careers.rivian.com/jobs/33833?icims=1) | Palo Alto, CA | Spring 2027 |  |
| 2026-09-30 | Tesla | [Embedded Software Developer Intern - Vehicle Suspension](https://www.tesla.com/careers/search/job/285153) | Palo Alto, CA | Spring 2027 |  |
| 2026-09-30 | Tesla | [Embedded Software Engineer Intern - Silicon Development](https://www.tesla.com/careers/search/job/285084) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-29 | AMCA | [Electrical Engineering Internship - Summer 2027](https://job-boards.greenhouse.io/amca/jobs/4396690009) | El Segundo, CA | Summer 2027 |  |
| 2026-09-29 | Hermeus | [Flight Software Engineering Intern (Simulation/Hardware-In-The-Loop) - Spring & Summer 2027](https://jobs.lever.co/hermeus/78008094-ca81-4a0c-9a18-93b30f932acd) | Los Angeles, CA | Summer 2027 | 🇺🇸 |
| 2026-09-29 | RTX | [Display Systems Engineering Co-op](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-106--400-Collins-Rd-NE--BLDG-106/Display-Systems-Engineering-Co-Op--Summer-Fall-2027----Onsite_01868917) | Cedar Rapids, IA | Summer 2027, Fall 2027 |  |
| 2026-09-29 | Tesla | [AI Hardware Design Verification Engineer Intern - AI Hardware - Tesla AI](https://www.tesla.com/careers/search/job/285088) | Palo Alto, CA; Austin, TX | Winter 2027, Spring 2027 |  |
| 2026-09-29 | Tesla | [AI Hardware RTL Design Engineer Intern - AI Hardware](https://www.tesla.com/careers/search/job/285089) | Palo Alto, CA; Austin, TX | Winter 2027, Spring 2027 |  |
| 2026-09-29 | Tesla | [AI Hardware Signal & Power Integrity Engineer Intern - AI Hardware](https://www.tesla.com/careers/search/job/285120) | Palo Alto, CA; Austin, TX | Winter 2027, Spring 2027 |  |
| 2026-09-28 | GlobalFoundries | [Silicon Photonics Reliability Engineering Intern](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---New-York---Malta/Silicon-Photonics-Reliability-Engineering-Intern--Summer-2027-_JR-2604258) | Malta, NY | Summer 2027 |  |
| 2026-09-28 | The Toro Company | [Electrical/Software Co-op](https://ttc.wd1.myworkdayjobs.com/Toro_External_Careers/job/Iron-Mountain-MI/Electrical-software-Coop_JR17089) | Iron Mountain, MI | Winter 2027 |  |
| 2026-09-26 | Tesla | [Silicon Validation Engineer Intern - AI Hardware](https://www.tesla.com/careers/search/job/284821) | Palo Alto, CA | Spring 2027 |  |
| 2026-09-25 | Rivian and Volkswagen Group Technologies | [Embedded Systems Software Engineering Intern - January - August 2027](https://jobs.ashbyhq.com/rivianvw.tech/f421a524-72da-4dd6-a549-bbee9e98622e/application?embed=true) | Champaign, IL, USA | Winter 2027 |  |
| 2026-09-25 | Zurn Elkay Water Solutions | [Embedded Hardware Intern](https://elkay.wd1.myworkdayjobs.com/Elkay_External/job/Milwaukee-WI/Embedded-Hardware-Intern--Summer-2027-_REQ-020151) | Milwaukee, WI | Summer 2027 |  |
| 2026-09-24 | Cummins | [Electronic Systems Co-op](https://fa-espx-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/2437584) | Columbus, IN, USA |  |  |
| 2026-09-24 | Tesla | [Robotics Electrical Design Engineer Intern - Tactile Sensing](https://www.tesla.com/careers/search/job/284593) | Palo Alto, CA | Spring 2027 |  |
| 2026-09-24 | Tesla | [Software Engineer Industrial Firmware Intern - Energy Engineering](https://www.tesla.com/careers/search/job/284448) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-24 | Tesla | [Solar Hardware Engineer Intern - PV Cell - Energy Engineering](https://www.tesla.com/careers/search/job/284489) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-23 | Astranis | [Electrical Engineer Intern](https://job-boards.greenhouse.io/astranis/jobs/4704784006) | San Francisco, CA | Summer 2027 |  |
| 2026-09-23 | Astranis | [Electrical Reliability Associate Intern](https://job-boards.greenhouse.io/astranis/jobs/4704788006) | San Francisco, CA | Winter 2027 |  |
| 2026-09-22 | Eaton | [Electrical Engineer Intern/Co-op - Engineering](https://eaton.eightfold.ai/careers/job/687238597770) | Peachtree City, GA | Summer 2027 |  |
| 2026-09-22 | Tesla | [Firmware Integration Engineer Intern - Factory Firmware](https://www.tesla.com/careers/search/job/284156) | Austin, TX | Spring 2027 |  |
| 2026-09-22 | Tesla | [Power Electronics Electrical Engineer Intern - Energy Engineering](https://www.tesla.com/careers/search/job/284183) | Palo Alto, CA | Winter 2027, Spring 2027 | 🎓 |
| 2026-09-22 | Two Sigma | [Hardware Engineering Intern](https://twosigma.avature.net/careers/JobDetail/14289) | New York, NY | Summer 2027 |  |
| 2026-09-21 | General Motors | [Embedded and Systems Engineering Intern - Digital Product](https://generalmotors.wd5.myworkdayjobs.com/en-CA/Careers_GM/job/Warren-Michigan-United-States-of-America/XMLNAME-2027-Summer-Intern---Digital-Product--Embedded-and-Systems-Engineering_JR-202620513) | Austin, TX; Milford, MI; Mountain View, CA; Warren, MI | Summer 2027 |  |
| 2026-09-21 | Rivian | [Engineering Intern - Product Development Systems (Spring 2027 Co-Op)](https://careers.rivian.com/jobs/33798?lang=en-us) | Torrance, California | Spring 2027 |  |
| 2026-09-21 | Symbotic | [Hardware Engineer Intern - Hardware Engineering](https://symbotic.wd504.myworkdayjobs.com/Symbotic/job/USA-Wilmington-MA---ITC/Hardware-Engineer_R8101) | Wilmington, MA |  |  |
| 2026-09-18 | Formlabs | [Hardware Test Engineer Intern](https://careers.formlabs.com/job/8196515/apply/?gh_jid=8196515) | Somerville, MA | Winter 2027, Spring 2027 |  |
| 2026-09-18 | RTX | [Digital Hardware Design Engineer Co-op - Winter/Spring](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-130--5350-C-Ave-NE--BLDG-130/Digital-Hardware-Design-Engineer-Co-op--Spring-Summer-_01871518-1) | Cedar Rapids, IA | Winter 2026, Spring 2027, Summer 2027, Fall 2027 |  |
| 2026-09-18 | Tesla | [Internship - Electrical Engineer - Power Electronics - Optimus - Winter/Spring 2027](https://www.tesla.com/careers/search/job/284009) | Palo Alto, CA | Spring 2027 |  |
| 2026-09-18 | Tesla | [Reliability Electronics Design Engineer Intern - Energy Engineering](https://www.tesla.com/careers/search/job/284126) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-16 | CesiumAstro | [Electrical Engineer Intern - Hardware](https://jobs.lever.co/CesiumAstro/ccb0f99f-0cc7-4517-8d1c-faeca53b5e5c/apply) | Westminster, CO | Summer 2027 |  |
| 2026-09-15 | Bracco | [Firmware Engineer Co-op](https://bracco.wd103.myworkdayjobs.com/braccocareers/job/USA-Eden-Prairie-Minnesota-55344/Firmware-Engineering-Co-op_JR100324) | Eden Prairie, MN | Spring 2027, Summer 2027 |  |
| 2026-09-15 | Gecko Robotics | [Embedded Software Engineer Intern - RoboSPLAT - Field Infra](https://jobs.ashbyhq.com/gecko-robotics/24561868-f075-4edf-a991-59ff0174e92a/application?embed=true) | Pittsburgh, PA | Summer 2027 |  |
| 2026-09-15 | Lunar Outpost | [Embedded Software Engineer Intern - Summer 2027](https://lunaroutpost.bamboohr.com/careers/392/) | Golden, CO | Summer 2027 |  |
| 2026-09-15 | Texas Instruments | [Systems Engineering Intern(SEM) - A&D](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25017921) | Dallas, TX, United States |  |  |
| 2026-09-14 | Bedrock Robotics | [Hardware Engineer Intern - Machine Integration & Test](https://jobs.ashbyhq.com/bedrock-robotics/c9c08251-6a42-4f9c-be4d-2621995cc8f9/application?embed=true) | San Francisco, CA | Summer 2027 |  |
| 2026-09-14 | Dell Technologies | [Hardware Engineering Intern - Infrastructure Solutions Group](https://iawmqy.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/careers/job/297770) | Round Rock, TX; Hopkinton, MA | Summer 2027 |  |
| 2026-09-11 | Bedrock Robotics | [Hardware Engineer Intern](https://jobs.ashbyhq.com/bedrock-robotics/949feb1b-c60f-43c5-94de-7dd9cd70ba4a/application?embed=true) | San Francisco, CA | Summer 2027 |  |
| 2026-09-11 | Draper | [Systems Engineering Co-op - Spring 2027](https://draper.wd5.myworkdayjobs.com/Draper_Careers/job/Cambridge-MA/Systems-Engineering-Co-Op--Spring-2027-_JR002882) | Cambridge, MA | Spring 2027 |  |
| 2026-09-11 | Emerson Electric | [Hardware Design Engineer Intern](https://hdjq.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/26010801) | Round Rock, TX | Summer 2027 |  |
| 2026-09-11 | Texas Instruments | [Systems Engineering Intern - MS/PhD](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25017542) | Dallas, TX, United States |  | 🎓 |
| 2026-09-10 | Amazon | [Industrial Development Engineer Intern/Co-op, ROBOTICS - 2027](https://www.amazon.jobs/en/jobs/10536817) | North Reading, Massachusetts, USA |  |  |
| 2026-09-10 | Antares Nuclear | [Electrical Engineer Intern](https://jobs.ashbyhq.com/Antares/3061297c-a666-47be-a58a-b62881bf183d/application?embed=true) | Torrance, CA | Summer 2027 |  |
| 2026-09-10 | Bedrock Robotics | [Sensor Systems Engineer Intern](https://jobs.ashbyhq.com/bedrock-robotics/d7da851b-55c2-45d4-bf8b-aa879282f25c/application?embed=true) | San Francisco, CA | Summer 2027 |  |
| 2026-09-10 | Garmin | [Electrical Design Engineer Intern](https://careers.garmin.com/jobs/19896?icims=1) | Tulsa, OK | Summer 2027 |  |
| 2026-09-10 | Insulet | [Embedded Software Engineering Co-op](https://insulet.wd5.myworkdayjobs.com/insuletcareers/job/Acton-Massachusetts/Co-op--Embedded-Software-Engineering--January-June-2027--Onsite-_REQ-2026-17966) | Acton, MA | Winter 2027 |  |
| 2026-09-10 | The Toro Company | [Hardware and Software Engineering Intern](https://ttc.wd1.myworkdayjobs.com/Toro_External_Careers/job/Perry-OK/Hardware-and-Software-Engineering-Intern---Ditch-Witch_JR17183) | Perry, OK | Summer 2027 |  |
| 2026-09-09 | Hermeus | [Avionics Electrical Engineering Intern - Summer 2027](https://jobs.lever.co/hermeus/b7babdb5-64ee-49ad-a193-918d6a31c462) | Atlanta, GA | Summer 2027 | 🇺🇸 |
| 2026-09-09 | Motorola | [FPGA Design Engineering Intern](https://motorolasolutions.wd5.myworkdayjobs.com/Careers/job/Schaumburg-IL/FPGA-Design-Engineering-Intern---Summer-2027_R68401) | Schaumburg, IL, USA | Summer 2027 |  |
| 2026-09-09 | Saronic | [Electrical Engineer Intern (Summer 2027)](https://jobs.ashbyhq.com/saronic/c7779462-3c4c-44d9-8314-1be93a0e478a) | Austin, TX | Summer 2027 | 🇺🇸 |
| 2026-09-08 | Bedrock Robotics | [Sensor Hardware Test Engineer Intern](https://jobs.ashbyhq.com/bedrock-robotics/1f413f83-b897-4938-a19e-ab91bd326c51/application?embed=true) | San Francisco, CA | Summer 2027 |  |
| 2026-09-08 | Blue Origin | [Electrical Systems Engineer Co-op - Fixed Term](https://blueorigin.wd5.myworkdayjobs.com/blueorigin/job/Los-Angeles-CA/Electronics-Electrical-Systems-Engineer-Co-Op_R71548) | Los Angeles, CA | Winter 2027, Spring 2027 |  |
| 2026-09-08 | Formlabs | [Hardware Reliability Intern](https://careers.formlabs.com/job/8186619/apply/?gh_jid=8186619) | Somerville, MA | Summer 2027 |  |
| 2026-09-08 | Revel | [Embedded Software Engineer Intern](https://jobs.ashbyhq.com/revel/f8eec1fd-da28-47ce-bca4-2fbe9c48a889/application?embed=true) | San Francisco, CA; Los Angeles, CA | Summer 2027 |  |
| 2026-09-08 | RTX | [Systems Engineer Co-op - Avi MIL Fms/Das](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-182--1100-Cimmie-Ave-Ne--BLDG-182/XMLNAME-2027-Summer-Fall-Co-Op---Systems-Engineer---AVI-MIL-FMS-DAS--Onsite-_01872240) | Cedar Rapids, IA | Summer 2027, Fall 2027 |  |
| 2026-09-08 | Trimble | [Hardware/Software Testing Intern](https://trimble.wd1.myworkdayjobs.com/en-US/TrimbleCareers/job/US---CO-Westminster/Hardware-Software-Testing-Intern_R57677-1) | Dayton, OH; Portsmouth, NH; Lake Oswego, OR; Westminster, CO | Summer 2027 |  |
| 2026-09-05 | Fab2 | [Electrical Engineer Intern](https://jobs.ashbyhq.com/fab2/aec19ef8-2257-4295-abc2-87afd05224ae/application?embed=true) | San Francisco, CA; Austin, TX | Summer 2027 |  |
| 2026-09-05 | Fab2 | [Electrical Engineering Intern - Summer](https://jobs.ashbyhq.com/Fab2/aec19ef8-2257-4295-abc2-87afd05224ae) | Austin; San Francisco Office |  |  |
| 2026-09-05 | Fab2 | [Electrical Engineering Intern, High Frequency Power Electronics - Summer](https://jobs.ashbyhq.com/Fab2/b3628272-a336-4dd6-968d-041bc4de5bc5) | Austin |  |  |
| 2026-09-05 | Fab2 | [Embedded Software Engineering Intern - Summer](https://jobs.ashbyhq.com/Fab2/15020e6e-be1c-4455-95a3-aa798474cec4) | Austin; San Francisco Office |  |  |
| 2026-09-05 | Fab2 | [Rust Software Engineering Intern, Chip Design Tools - Summer](https://jobs.ashbyhq.com/Fab2/2b0ab443-c7d8-4547-9766-111747f0b361) | Austin; San Francisco Office |  |  |
| 2026-09-05 | Solidigm | [Hardware & Product Development Engineering Intern](https://jobs.smartrecruiters.com/Solidigm/744000147613839) | Rancho Cordova, CA | Summer 2027 |  |
| 2026-09-05 | Solidigm | [Hardware, Electrical Validation and Product Engineering Intern - Validation](https://jobs.smartrecruiters.com/Solidigm/744000147613779) | Rancho Cordova, CA | Summer 2027 | 🎓 |
| 2026-09-05 | Solidigm | [Software Development & Firmware Engineering Intern - Multiple Teams](https://jobs.smartrecruiters.com/Solidigm/744000147613629) | Rancho Cordova, CA; Longmont, CO; Sacramento, CA | Summer 2027 |  |
| 2026-09-05 | Solidigm | [Software Engineering Intern - Firmware & AI Engineering](https://jobs.smartrecruiters.com/Solidigm/744000147613769) | Rancho Cordova, CA | Summer 2027 | 🎓 |
| 2026-09-04 | Amazon | [Software Development Engineer Intern/Co-Op, ROBOTICS -  2027](https://www.amazon.jobs/en/jobs/10529525) | North Reading, Massachusetts, USA |  |  |
| 2026-09-04 | Tesla | [Electrical Engineer Intern - Energy Engineering](https://www.tesla.com/careers/search/job/279743) | Palo Alto, CA; Austin, TX | Spring 2027 |  |
| 2026-09-03 | Apex | [Software Engineer Intern - Embedded Systems](https://jobs.ashbyhq.com/apex-technology-inc/4203604c-2330-4c89-8432-37af718a6bda/application?embed=true) | Los Angeles, CA | Spring 2027, Summer 2027 |  |
| 2026-09-03 | Booz Allen | [Electronic Warfare FPGA Engineer Intern](https://bah.wd1.myworkdayjobs.com/bah_jobs/job/Beavercreek-OH/University---Summer-2027-Electronic-Warfare-FPGA-Engineering-Intern_R0248465-1) | Beavercreek, OH | Summer 2027 |  |
| 2026-09-03 | GE Vernova | [Hardware Engineer Intern - Critical Infrastructure Communications](https://gevernova.wd5.myworkdayjobs.com/only_confidential_executive_recruiting/job/Rochester/GE-Vernova-Grid-Solutions---Hardware-Engineering-Intern--Critical-Infrastructure-Communications----Spring-Summer-2027_R5051647-1) | Rochester, NY | Summer 2027 |  |
| 2026-09-03 | General Matter | [Embedded Software Engineer Intern](https://job-boards.greenhouse.io/generalmatter/jobs/5377131008) | Los Angeles, CA | Summer 2027 |  |
| 2026-09-03 | Hermeus | [Mission Systems Engineering Intern - Spring/Summer 2027](https://jobs.lever.co/hermeus/9229aa88-f54d-4ecd-85ee-b31f53b4207d) | Atlanta, GA | Summer 2027 | 🇺🇸 |
| 2026-09-03 | Hewlett Packard Enterprise | [Pre-Silicon Diagnostics Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Ft-Collins-Colorado-United-States-of-America/Pre-Silicon-Diagnostics-Intern_1213394) | Fort Collins, CO | Summer 2027 |  |
| 2026-09-03 | Shure | [Automated Test Engineer Intern - Hardware](https://careersus-shure.icims.com/jobs/4960/job?mobile=true&needsRedirect=false) | Niles, IL, USA | Summer 2027 |  |
| 2026-09-03 | Shure | [Electrical Engineering Intern - Digital Circuitry](https://careersus-shure.icims.com/jobs/5013/job?mobile=true&needsRedirect=false) | Niles, IL, USA | Summer 2027 |  |
| 2026-09-03 | Shure | [Embedded Software Intern](https://careersus-shure.icims.com/jobs/5018/job?mobile=true&needsRedirect=false) | Niles, IL, USA | Summer 2027 |  |
| 2026-09-03 | Tesla | [Access Control Systems Integration Engineer Intern - Access Control Systems](https://www.tesla.com/careers/search/job/282258) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-03 | Tesla | [Embedded Software Engineer Intern - High Voltage Systems](https://www.tesla.com/careers/search/job/282227) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-03 | Tesla | [Embedded Software Engineer Intern - Optimus](https://www.tesla.com/careers/search/job/282340) | Palo Alto, CA | Spring 2027, Summer 2027 |  |
| 2026-09-03 | Tesla | [Embedded Software Engineer Intern - Steering - Chassis Systems](https://www.tesla.com/careers/search/job/282248) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-03 | Tesla | [Embedded Systems Software Engineer Intern - AI Platforms](https://www.tesla.com/careers/search/job/282331) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-03 | Tesla | [Software Integration Engineer Intern - Battery Management Systems](https://www.tesla.com/careers/search/job/282241) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-09-02 | Intel | [Platform Hardware and Systems Engineering Intern](https://intel.wd1.myworkdayjobs.com/en-us/external/job/US-Oregon-Hillsboro/Platform-Hardware-and-Systems-Engineering---Intern--Graduate_JR0286828) | Austin, TX; Santa Clara, CA; Hillsboro, OR; Folsom, CA; Phoenix, AZ | Spring 2027, Summer 2027 | 🎓 |
| 2026-09-02 | Intel | [Platform Hardware and Systems Engineering Intern - Bachelor's](https://intel.wd1.myworkdayjobs.com/en-us/external/job/US-Oregon-Hillsboro/Platform-Hardware-and-Systems-Engineering---Intern--Bachelor-s_JR0286827) | Austin, TX; Santa Clara, CA; Hillsboro, OR; Folsom, CA; Phoenix, AZ | Spring 2027, Summer 2027 |  |
| 2026-09-02 | Intel | [Silicon Hardware Engineering Intern - Graduate](https://intel.wd1.myworkdayjobs.com/en-us/external/job/US-Oregon-Hillsboro/Silicon-Hardware-Engineering---Intern--Graduate_JR0286830) | Austin, TX; Santa Clara, CA; Hillsboro, OR; Folsom, CA; Phoenix, AZ | Spring 2027, Summer 2027 | 🎓 |
| 2026-09-02 | Texas Instruments | [Analog IC Design Engineering Intern - Bachelors](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25017543) | Dallas, TX, United States |  |  |
| 2026-09-02 | Texas Instruments | [Analog IC Design Engineering Intern - MS/PhD](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25017544) | Dallas, TX, United States |  | 🎓 |
| 2026-09-02 | Texas Instruments | [Design Verification Engineering Intern - Bachelors](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25017545) | Dallas, TX, United States |  |  |
| 2026-09-02 | Texas Instruments | [Design Verification Engineering Intern - MS/PhD](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25017546) | Dallas, TX, United States |  | 🎓 |
| 2026-09-02 | Texas Instruments | [Digital IC Design Engineering Intern - Bachelors](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25017547) | Dallas, TX, United States |  |  |
| 2026-09-02 | Texas Instruments | [Digital IC Design Engineering Intern - MS/PhD](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25017548) | Dallas, TX, United States |  | 🎓 |
| 2026-09-01 | AeroVironment | [Embedded Software Engineer Intern](https://avav.wd1.myworkdayjobs.com/en-US/avav/job/Simi-Valley-CA/Summer-2027-Embedded-Software-Engineering-Intern_8388) | Dayton, OH; Annapolis Junction, MD; Pottstown, PA; Albuquerque, NM; Sunrise, FL; Arlington County, Arlington, VA; Melbourne, FL; Petaluma, CA; Centreville, VA; Lawrence, KS; Minneapolis, MN; San Luis Obispo, CA; Huntsville, AL; San Diego, CA; Moorpark, CA; Simi Valley, CA | Summer 2027 |  |
| 2026-09-01 | AeroVironment | [Systems Test Engineer Intern](https://avav.wd1.myworkdayjobs.com/en-US/avav/job/Simi-Valley-CA/Summer-2027-Systems-Test-Engineer_8390) | Germantown, MD; Annapolis Junction, MD; Pottstown, PA; Albuquerque, NM; Sunrise, FL; Arlington County, Arlington, VA; Melbourne, FL; Petaluma, CA; Fairborn, OH; Minneapolis, MN; San Luis Obispo, CA; Herndon, VA; Huntsville, AL; Moorpark, CA; Simi Valley, CA |  |  |
| 2026-09-01 | Freeform | [Electrical Engineer Intern](https://job-boards.greenhouse.io/freeformfuturecorp/jobs/7982398003) | Los Angeles, CA | Spring 2027 |  |
| 2026-09-01 | Stanley Black & Decker | [Embedded Software Engineering Intern](https://sbdinc.wd1.myworkdayjobs.com/en-US/Stanley_Black_Decker_Career_Site/job/Towson-MD-United-States/Embedded-Engineering-Summer-Intern-2027_REQ-1000052019) | Towson, MD | Summer 2027 |  |
| 2026-09-01 | Vermeer | [Embedded Software Engineer Intern](https://vermeer.wd5.myworkdayjobs.com/externalcareersite/job/Pella-Iowa-USA---Corporate-Office/Embedded-Software-Engineer-Internship-Summer-2027_REQ-22165) | Pella, IA | Summer 2027 |  |
| 2026-08-31 | Aerotech | [Electrical/Computer Engineering Intern Co-op](https://aerotech.applytojob.com/apply/FrPUDToawu/ElectricalComputer-Engineering-Internship-Or-Coop-2027) | Pittsburgh, PA | Summer 2027 |  |
| 2026-08-28 | Fab2 | [Embedded Software Engineer Intern - Winter](https://jobs.ashbyhq.com/fab2/3c7fd0f1-b25f-413c-8e62-6ef00a9d47da/application?embed=true) | San Francisco, CA; Austin, TX | Winter 2027 |  |
| 2026-08-28 | Hewlett Packard Enterprise | [Firmware Engineer Intern](https://hpe.wd5.myworkdayjobs.com/jobsathpe/job/Spring-Texas-United-States-of-America/Firmware-Engineer-Intern_1213627) | Andover, MA; Bloomington, MN; San Jose, CA; Spring, TX; Durham, NC; Westford, MA; Chippewa Falls, WI; Fort Collins, CO; Sunnyvale, CA; Roseville, CA |  |  |
| 2026-08-28 | Tesla | [Electrical Engineer Intern - Energy Service Tooling](https://www.tesla.com/careers/search/job/281457) | Hayward, CA | Spring 2027 |  |
| 2026-08-27 | Amazon | [ASIC Engineer Intern, Annapurna Labs - 2027](https://www.amazon.jobs/en/jobs/10517535) | Cupertino, California, USA |  |  |
| 2026-08-27 | Amazon | [Cloud Hardware Development Engineer Intern, Annapurna Labs - 2027](https://www.amazon.jobs/en/jobs/10517649) | Austin, Texas, USA |  |  |
| 2026-08-26 | Tesla | [AI Hardware Physical Design Engineer Intern - AI Hardware](https://www.tesla.com/careers/search/job/281233) | Palo Alto, CA; Austin, TX; Fort Collins, CO | Spring 2027 |  |
| 2026-08-26 | Vertiv | [Firmware Engineer Intern - Summer 2027](https://egup.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20278957) | Delaware, OH | Summer 2027 | 🎓 |
| 2026-08-25 | GE Appliances | [Electrical Engineer Co-op](https://haier.wd3.myworkdayjobs.com/ge_appliances/job/USA-Louisville-KY/Electrical-Engineering-Co-op-Fall-2027_REQ-26594) | Louisville, KY | Summer 2027, Fall 2027 |  |
| 2026-08-25 | Honeywell | [Embedded Engineer Intern](https://ibqbjb.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/Honeywell/job/155561) | United States | Summer 2027 |  |
| 2026-08-25 | Verkada | [Embedded Software Engineer Intern](https://job-boards.greenhouse.io/verkada/jobs/5211595007) | San Mateo, CA | Winter 2027, Summer 2027 |  |
| 2026-08-19 | NVIDIA | [Hardware ASIC Design Intern - Hardware](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Hardware-ASIC-Design_JR2023486) | Santa Clara, CA | Summer 2027 |  |
| 2026-08-19 | NVIDIA | [Hardware Engineering Intern](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Hardware-Engineering_JR2023508-1) | Santa Clara, CA | Summer 2027 |  |
| 2026-08-19 | NVIDIA | [Hardware Physical Design / VLSI Intern](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Hardware-Physical-Design---VLSI_JR2023501) | Santa Clara, CA | Summer 2027 |  |
| 2026-08-19 | NVIDIA | [Hardware Verification Intern](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Hardware-Verification_JR2023500) | Santa Clara, CA | Summer 2027 |  |
| 2026-08-19 | NVIDIA | [Mixed Signal Design Intern](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Mixed-Signal-Design_JR2023502) | Santa Clara, CA | Summer 2027 |  |
| 2026-08-14 | ByteDance | [ASIC Design Engineer Intern - Video Silicon IP](https://jobs.bytedance.com/en/position/7670332179383699717/detail) | San Jose, CA | Summer 2027 | 🎓 |
| 2026-08-13 | Specter Aerospace | [Embedded Software Co-op](https://specteraerospace.bamboohr.com/careers/119/) | Boston, MA | Spring 2027 |  |
| 2026-08-13 | Tesla | [Firmware Engineer Intern - New Programs Engineering](https://www.tesla.com/careers/search/job/279991) | Fremont, CA | Spring 2027 |  |
| 2026-08-10 | Rockwell Automation | [Embedded Software Engineer Co-op](https://rockwellautomation.wd1.myworkdayjobs.com/External-Rockwell-Automation-Early-Careers/job/Mayfield-Heights-Ohio-United-States/Spring-2027-Co-op--Embedded-Software-Engineer--January-2027---August-2027-_R26-3473) | Mayfield Heights, OH | Spring 2027, Summer 2027 |  |
| 2026-08-10 | Tesla | [Electronic Design Engineer Intern - Electronic Systems](https://www.tesla.com/careers/search/job/279760) | Palo Alto, CA | Winter 2027, Spring 2027 |  |
| 2026-08-03 | SpaceX | [Silicon Engineer Intern/Co-op](https://boards.greenhouse.io/spacex/jobs/8621763002) | Palo Alto, CA; Irvine, CA; Redmond, WA | Spring 2027, Summer 2027 |  |
| 2026-08-01 | HPR (Hyannis Port Research) | [FPGA Engineer Intern](https://job-boards.greenhouse.io/hyannisportresearch/jobs/7822801003) | Needham, MA | Summer 2027 |  |
| 2026-07-31 | Virtu Financial | [Hardware Engineer Intern - FPGA](https://job-boards.greenhouse.io/virtu/jobs/8657286002) | Austin, TX | Summer 2027 | 🎓 |
| 2026-07-21 | Optiver | [FPGA Engineer Intern](https://www.optiver.com/join-us/jobs/8641352002/?gh_jid=8641352002) | Austin, TX; Chicago, IL, USA | Summer 2027 |  |
| 2026-07-20 | GE Healthcare | [Engineering Development Program Intern - Hardware](https://gehc.wd5.myworkdayjobs.com/GEHC_ExternalSite/job/Waukesha/Edison-Engineering-Development-Program-Internship---Hardware_R4043923-1) | Twinsburg, OH; Waukesha, WI | Summer 2027 |  |
| 2026-04-27 | Figure | [Electrical Engineer Intern](https://job-boards.greenhouse.io/figureai/jobs/4676467006) | San Jose, CA | Winter 2027 |  |
| 2026-04-15 | Zoox | [Contract Student Worker  – Firmware Engineer (FW Thermal/Body)](https://jobs.lever.co/zoox/07f0834f-06ec-44c7-a24b-3efa08589d38) | Foster City, CA |  |  |
| 2026-04-13 | Etched | [DFT Intern](https://jobs.ashbyhq.com/Etched/5f1f5739-3b58-467c-b351-ff183c94d96d) | San Jose |  |  |
| 2026-02-07 | Etched | [Electrical Platform Intern](https://jobs.ashbyhq.com/Etched/904ddf46-55fc-4a8f-8b49-f32cfe88116a) | San Jose |  |  |
| 2026-02-07 | Etched | [Firmware Intern](https://jobs.ashbyhq.com/Etched/699f3ab2-07e4-466c-9d76-3d4a3abb4ebc) | San Jose |  |  |
| 2025-12-17 | Amazon | [Robotics - Hardware Development Engineer Intern/Co-op - 2026 (Robotics, Mechanical, Electrical, Hardware Test, Reliability, Failure Analysis, Operations, and more)](https://www.amazon.jobs/en/jobs/3145033) | Westborough, Massachusetts, USA |  |  |
<!-- JOBS:END -->
