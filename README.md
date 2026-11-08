# JobBot

A job scraper and Gmail digest bot for hardware/firmware/embedded systems roles. Scrapes ~80 hardware, semiconductor, robotics, space, and automotive companies for firmware, embedded, hardware, and systems engineer roles: internships, co-ops, and new-grad roles in Toronto, Montreal, Ottawa, and Vancouver, plus internships anywhere in the US. Emails a daily digest and keeps the table below up to date.

**Features:**
- Scrapes ~80 hardware/semiconductor/robotics/space/automotive companies
- Filters for firmware/embedded/hardware/systems roles in target Canadian cities (Toronto, Montreal, Ottawa, Vancouver), and internships/co-ops anywhere in the US
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
_Updated 2026-11-08 22:40 UTC — 144 jobs posted in the last 14 days_

### Internships & Co-ops (104)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-11-08 | Google | [Hardware Engineering Intern, PhD, Summer 2027](https://www.google.com/about/careers/applications/jobs/results/97352132356645574) | Mountain View, CA, USA; Ann Arbor, MI, USA; Atlanta, GA, USA; Austin, TX, USA; Boulder, CO, USA; Cambridge, MA, USA; Bellevue, WA, USA; Chicago, IL, USA; Irvine, CA, USA; Kirkland, WA, USA; Los Angeles, CA, USA; Madison, WI, USA; New York, NY, USA; Palo Alto, CA, USA; Portland, OR, USA; Pittsburgh, PA, USA; Raleigh, NC, USA; Durham, NC, USA; Reston, VA, USA; Redmond, WA, USA; Redwood City, CA, USA; San Diego, CA, USA; Goleta, CA, USA; San Bruno, CA, USA; Seattle, WA, USA; San Francisco, CA, USA; San Jose, CA, USA; Santa Cruz, CA, USA; South San Francisco, CA, USA; Sunnyvale, CA, USA; Washington D.C., DC, USA |
| 2026-11-08 | Google | [Silicon Engineering Intern, PhD, Summer 2027](https://www.google.com/about/careers/applications/jobs/results/136529930677560006) | Sunnyvale, CA, USA; Austin, TX, USA; Madison, WI, USA |
| 2026-11-08 | Infineon | [Intern - Data Center Power Systems](https://jobs.infineon.com/careers/job/563808971984423) | El Segundo, CA, US |
| 2026-11-08 | Infineon | [Intern- Analog Design](https://jobs.infineon.com/careers/job/563808972303150) | Austin, TX, US |
| 2026-11-08 | Infineon | [Internship - Analog Mixed Signal Design](https://jobs.infineon.com/careers/job/563808971905261) | El Segundo, CA, US |
| 2026-11-08 | L3Harris | [Electrical Engineering Intern](https://careers.l3harris.com/en/job/salt-lake-city/electrical-engineering-intern/4832/100436666368) | Salt Lake City, UT |
| 2026-11-08 | L3Harris | [Intern, Systems Engineering](https://careers.l3harris.com/en/job/nashville/intern-systems-engineering/4832/102854131552) | Nashville, TN |
| 2026-11-08 | L3Harris | [Systems Engineering Intern](https://careers.l3harris.com/en/job/salt-lake-city/systems-engineering-intern/4832/100989135664) | Salt Lake City, UT |
| 2026-11-08 | L3Harris | [Systems Engineering Intern](https://careers.l3harris.com/en/job/salt-lake-city/systems-engineering-intern/4832/100667887008) | Salt Lake City, UT |
| 2026-11-08 | L3Harris | [Systems Engineering Intern](https://careers.l3harris.com/en/job/salt-lake-city/systems-engineering-intern/4832/101700268160) | Salt Lake City, UT |
| 2026-11-08 | L3Harris | [Systems Engineering Intern](https://careers.l3harris.com/en/job/salt-lake-city/systems-engineering-intern/4832/101323972064) | Salt Lake City, UT |
| 2026-11-08 | Microsoft | [Research Intern - Research in Software Engineering, ML Systems, Agents](https://apply.careers.microsoft.com/careers/job/1970393557054069) | Redmond, WA, US |
| 2026-11-06 | Astranis | [Embedded Software Developer, Network/Payload Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704571006) | San Francisco |
| 2026-11-06 | GM | [2027 Summer Intern – Software Engineer, AV/AI Platform](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/GM-Automation---Sunnyvale---GM-Automation---Sunnyvale/XMLNAME-2027-Summer-Intern---Software-Engineer--AV-AI-Platform_JR-202621696) | GM Automation - Sunnyvale - GM Automation - Sunnyvale; Warren, Michigan, United States of America |
| 2026-11-05 | KLA | [Optical Systems Student Engineer](https://kla.wd1.myworkdayjobs.com/Search/job/Milpitas-CA/Optical-Systems-Student-Engineer_2641844-1) | Milpitas, CA |
| 2026-11-05 | Neuralink | [Analog and Mixed-Signal IC Design Engineer Intern](https://boards.greenhouse.io/neuralink/jobs/7565469003?gh_jid=7565469003) | South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [Digital IC Design Engineer Intern](https://boards.greenhouse.io/neuralink/jobs/7090489003?gh_jid=7090489003) | South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [Electrical Engineer Intern, Implant Embedded Systems](https://boards.greenhouse.io/neuralink/jobs/7702527003?gh_jid=7702527003) | Austin, Texas, United States; South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [Electrical Engineer Intern, Robotics and Surgery Engineering](https://boards.greenhouse.io/neuralink/jobs/6607398003?gh_jid=6607398003) | South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [Embedded Software Engineer Intern, Implant Embedded Systems](https://boards.greenhouse.io/neuralink/jobs/6283663003?gh_jid=6283663003) | Austin, Texas, United States; South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [Firmware Engineer Intern, Robotics and Surgery Engineering](https://boards.greenhouse.io/neuralink/jobs/6648992003?gh_jid=6648992003) | South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [IT Systems Administrator Intern](https://boards.greenhouse.io/neuralink/jobs/7736276003?gh_jid=7736276003) | Austin, Texas, United States; South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [Manufacturing Intern, Surgery & Robot Hardware](https://boards.greenhouse.io/neuralink/jobs/7666761003?gh_jid=7666761003) | South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [Mechanical Engineering Intern, Robotics and Surgery Engineering](https://boards.greenhouse.io/neuralink/jobs/6514169003?gh_jid=6514169003) | South San Francisco, California, United States |
| 2026-11-05 | Neuralink | [Software Engineer Intern, Robotics](https://boards.greenhouse.io/neuralink/jobs/5469305003?gh_jid=5469305003) | Austin, Texas, United States; South San Francisco, California, United States |
| 2026-11-05 | NVIDIA | [Research and Engineering Intern, Agentic Systems Intelligence – Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Research-and-Engineering-Intern--Agentic-Systems-Intelligence---Summer-2027_JR2028260) | US, CA, Santa Clara; US, TX, Austin; US, WA, Redmond |
| 2026-11-05 | Waymo | [2027 Summer Intern, MS/PhD, Perception Systems Engineering: Pedestrian Detection Precision](https://careers.withwaymo.com/jobs?gh_jid=8234670) | San Francisco, California |
| 2026-11-04 | Intel | [Robotics PhD Intern](https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/Robotics-PhD-Intern_JR0288833) | US, Oregon, Hillsboro; US, Arizona, Phoenix |
| 2026-11-04 | NVIDIA | [VLSI Timing Methodology Intern - Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/VLSI-Timing-Methodology-Intern---Summer-2027_JR2026798) | US, CA, Santa Clara |
| 2026-11-04 | Rocket Lab | [Fluid Systems Intern Spring 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7986788003) | Long Beach, CA |
| 2026-11-04 | Texas Instruments | [Analog Design Eng Intern](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25019660) | Santa Clara, CA, United States |
| 2026-11-04 | Texas Instruments | [Analog Design Verification Eng Intern](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25019663) | Santa Clara, CA, United States |
| 2026-11-04 | Texas Instruments | [Digital Design Verification Engineering Intern](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/25019665) | Santa Clara, CA, United States |
| 2026-11-03 | Astranis | [Electrical Integration Intern - Avionics (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704826006) | San Francisco |
| 2026-11-03 | Astranis | [Electrical Integration Intern - RF (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4715788006) | San Francisco |
| 2026-11-03 | Astranis | [Electrical Reliability Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704784006) | San Francisco |
| 2026-11-03 | Astranis | [Electrical Reliability Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704782006) | San Francisco |
| 2026-11-03 | Astranis | [FPGA Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704805006) | San Francisco |
| 2026-11-03 | Astranis | [FPGA Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4704803006) | San Francisco |
| 2026-11-03 | Astranis | [Hardware Test Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4707012006) | San Francisco |
| 2026-11-03 | Astranis | [Power Electronics Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4706425006) | San Francisco |
| 2026-11-03 | Astranis | [Power Electronics Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4706427006) | San Francisco |
| 2026-11-03 | Astranis | [RF Hardware Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4708436006) | San Francisco |
| 2026-11-03 | Astranis | [RF Hardware Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4708417006) | San Francisco |
| 2026-11-03 | Astranis | [Software Defined Radio Hardware Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4716088006) | San Francisco |
| 2026-11-03 | Astranis | [Software Defined Radio Hardware Intern (Winter 2027)](https://job-boards.greenhouse.io/astranis/jobs/4716087006) | San Francisco |
| 2026-11-03 | Astranis | [Software Engineer - Enterprise Systems Intern (Summer 2027)](https://job-boards.greenhouse.io/astranis/jobs/4705610006) | San Francisco, CA |
| 2026-11-03 | Ciena | [Hardware Engineering Co-op (Winter 2027)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Engineering-Co-op--Winter-2027-_R032054) | Ottawa |
| 2026-11-03 | Marvell | [Hardware Signal Integrity Intern, MS - Summer 2027](https://marvell.wd1.myworkdayjobs.com/MarvellCareers2/job/Santa-Clara-CA/Hardware-Signal-Integrity-Intern--MS---Summer-2027_2603877) | Santa Clara, CA |
| 2026-11-02 | Anduril | [2027 Electrical Engineer Intern](https://boards.greenhouse.io/andurilindustries/jobs/5148101007?gh_jid=5148101007) | Atlanta, Georgia, United States; Boston, Massachusetts, United States; Broomfield, Colorado, United States; Colorado Springs, Colorado, United States; Costa Mesa, California, United States; Fort Collins, Colorado, United States; Irvine, California, United States; Reston, Virginia, United States; Seattle, Washington, United States |
| 2026-11-02 | Anduril | [2027 Firmware Engineer Intern](https://boards.greenhouse.io/andurilindustries/jobs/5265158007?gh_jid=5265158007) | Costa Mesa, California, United States |
| 2026-11-02 | Anduril | [2027 Systems Engineer Intern](https://boards.greenhouse.io/andurilindustries/jobs/5257690007?gh_jid=5257690007) | Boston, Massachusetts, United States; Costa Mesa, California, United States; Fort Collins, Colorado, United States; Reston, Virginia, United States; Seattle, Washington, United States |
| 2026-11-02 | Anduril | [Winter 2027 Electrical Engineer Co-op](https://boards.greenhouse.io/andurilindustries/jobs/5236565007?gh_jid=5236565007) | Costa Mesa, California, United States; Quincy, Massachusetts, United States |
| 2026-11-02 | Anduril | [Winter 2027 Robotics Engineer Co-op](https://boards.greenhouse.io/andurilindustries/jobs/5271842007?gh_jid=5271842007) | Quincy, Massachusetts, United States |
| 2026-11-02 | Anduril | [Winter 2027 Systems Engineer Co-op](https://boards.greenhouse.io/andurilindustries/jobs/5236599007?gh_jid=5236599007) | Quincy, Massachusetts, United States |
| 2026-11-02 | Applied Materials | [2027 Summer Electrical Engineer Intern- Master's (Santa Clara, CA)](https://amat.wd1.myworkdayjobs.com/External/job/Santa-ClaraCA/XMLNAME-2027-Summer-Electrical-Engineer-Intern--Master-s--Santa-Clara--CA-_R2629967) | Santa Clara,CA |
| 2026-11-02 | Micron | [Intern - YE-Electrical Failure Analysis Engineer](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---ID1/Intern---YE-Electrical-Failure-Analysis-Engineer_JR114538) | Boise, ID - ID1 |
| 2026-11-02 | NVIDIA | [AI Compiler and Kernel Intern – Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-TX-Austin/AI-Compiler-and-Kernel-Intern---Summer-2027_JR2029220-1) | US, TX, Austin |
| 2026-11-02 | Rocket Lab | [Electrical Engineering Intern Spring 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7990045003) | Toronto, CAN |
| 2026-11-02 | Rocket Lab | [Electrical Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7998598003) | Pasadena, CA |
| 2026-11-02 | Rocket Lab | [Electrical Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7990043003) | Toronto, CAN |
| 2026-11-02 | Rocket Lab | [Electrical Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7990683003) | Long Beach, CA |
| 2026-11-02 | Rocket Lab | [Fluid Systems Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7986794003) | Long Beach, CA |
| 2026-11-02 | Rocket Lab | [Ground Systems Engineering Intern Spring 2027](https://job-boards.greenhouse.io/rocketlab/jobs/8007204003) | Stennis Space Center, MS |
| 2026-11-02 | Rocket Lab | [Ground Systems Engineering Intern Spring 2027](https://job-boards.greenhouse.io/rocketlab/jobs/8042094003) | Middle River, MD |
| 2026-11-02 | Rocket Lab | [Ground Systems Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/8042092003) | Middle River, MD |
| 2026-11-02 | Rocket Lab | [Ground Systems Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/8007202003) | Stennis Space Center, MS |
| 2026-11-02 | Rocket Lab | [Systems Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7990270003) | Tucson, AZ |
| 2026-11-02 | Rocket Lab | [Systems Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7990138003) | Pasadena, CA |
| 2026-11-02 | Rocket Lab | [Systems Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7990272003) | Chantilly, VA |
| 2026-11-02 | Rocket Lab | [Systems Engineering Intern Summer 2027](https://job-boards.greenhouse.io/rocketlab/jobs/7987046003) | Long Beach, CA |
| 2026-11-02 | Zoox | [Hardware Engineer Intern, Manufacturing Operations [Summer 2027]](https://jobs.lever.co/zoox/53f5297a-fe30-4e1e-ab1c-96db5b23eded) | Foster City, CA |
| 2026-11-02 | Zoox | [Hardware Engineer Intern, Vehicle Development [Summer 2027]](https://jobs.lever.co/zoox/0accbf9e-9b09-4733-b495-fb6dce13ba62) | Foster City, CA |
| 2026-11-02 | Zoox | [Hardware Engineer Intern, Vehicle Systems [Summer 2027]](https://jobs.lever.co/zoox/0c32245b-f51d-40d2-8e57-a0be1b744c5b) | Foster City, CA |
| 2026-10-31 | Applied Materials | [2027 Spring Electrical Engineer Co-op (Billerica, MA)](https://amat.wd1.myworkdayjobs.com/External/job/BillericaMA/XMLNAME-2027-Spring-Electrical-Engineer-Co-op--Billerica--MA-_R2631535-1) | Billerica,MA |
| 2026-10-30 | Altera | [FPGA Development Tools - Intern](https://altera.wd1.myworkdayjobs.com/altera/job/Toronto-Ontario-Canada/FPGA-Development-Tools---Intern_R03394) | Toronto, Ontario, Canada |
| 2026-10-30 | Applied Materials | [Summer 2027 Electrical Radio Frequency Engineer Intern- Master's/PhD (Santa Clara, CA)](https://amat.wd1.myworkdayjobs.com/External/job/Santa-ClaraCA/Summer-2027-Electrical-Radio-Frequency-Engineer-Intern--Master-s-PhD--Santa-Clara--CA-_R2629753) | Santa Clara,CA |
| 2026-10-30 | Ciena | [ASIC Engineer Intern](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/ASIC-Engineer-Intern_R031750) | Ottawa |
| 2026-10-30 | GM | [2027 Summer Intern – Research and Development - Power Electronics & Energy Conversion Systems](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Pontiac-Michigan-United-States-of-America/XMLNAME-2027-Summer-Intern---Research-and-Development---Power-Electronics---Energy-Conversion-Systems_JR-202623048) | Pontiac, Michigan, United States of America; Warren, Michigan, United States of America |
| 2026-10-30 | MDA Space | [Engineering Student - FPGA Designer - Winter 2027](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=216d347b-2abb-43e8-8fbc-268adecf0aa3) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-10-30 | MDA Space | [Engineering Student - FPGA Verification - Winter 2027](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=e40bbead-0940-4adb-9ae8-2b3d4d3d6874) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-10-30 | Nokia | [Silicon Photonics Packaging Engineer Co-op](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/40848) | Sunnyvale, California |
| 2026-10-30 | NVIDIA | [ASIC Verification Intern - Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/Canada-Toronto/ASIC-Verification-Intern---Summer-2027_JR2027982) | Canada, Toronto |
| 2026-10-30 | NVIDIA | [PCIe Design Verification Intern - Spring 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PCIe-Design-Verification-Intern---Spring-2027_JR2026704) | US, CA, Santa Clara |
| 2026-10-30 | NVIDIA | [PCIe Design Verification Intern - Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-TX-Austin/PCIe-Design-Verification-Intern---Summer-2027_JR2026708) | US, TX, Austin |
| 2026-10-30 | NVIDIA | [PhD Research Intern, AI Accelerator Design and VLSI - 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Research-Intern--AI-Accelerator-Design-and-VLSI---2027_JR2026584-1) | US, CA, Santa Clara |
| 2026-10-30 | NVIDIA | [PhD Research Intern, Autonomous Systems and Physical AI Research - 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Research-Intern--Autonomous-Systems-and-Physical-AI-Research---2027_JR2024171) | US, CA, Santa Clara |
| 2026-10-30 | NVIDIA | [PhD Research Intern, Programming Systems - 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Research-Intern--Programming-Systems---2027_JR2025379) | US, CA, Santa Clara |
| 2026-10-30 | NVIDIA | [PhD Research Intern, Robotics - Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-WA-Seattle/Research-Intern--Robotics---Summer-2027_JR2025647) | US, WA, Seattle; US, CA, Santa Clara |
| 2026-10-30 | NVIDIA | [VLSI CAD Timing Intern, Applied AI - Summer 2027](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/VLSI-CAD-Timing-Intern--Applied-AI---Summer-2027_JR2026799) | US, CA, Santa Clara |
| 2026-10-30 | Zoox | [Software Engineer Intern, Software Systems [Summer 2027]](https://jobs.lever.co/zoox/8b32157b-ab44-4078-85ea-1d8d7b747a20) | Foster City, CA |
| 2026-10-29 | Ciena | [Embedded Software Engineer – Co-op Winter 2027](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-Software-Engineer---Co-op-Winter-2027_R032005) | Ottawa |
| 2026-10-29 | Ciena | [Hardware Characterization Automation Co-op (Winter 2027)](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Characterization-Automation-Co-op--Winter-2027-_R032014) | Ottawa |
| 2026-10-29 | Micron | [Intern - ASIC Digital Design](https://micron.wd1.myworkdayjobs.com/External/job/Minneapolis-MN/Intern---ASIC-Digital-Design_JR112163) | Minneapolis, MN |
| 2026-10-28 | Amazon | [2027 Applied Science Internship - Robotics - United States](https://www.amazon.jobs/en/jobs/10591833) | North Reading, Massachusetts, USA |
| 2026-10-28 | Figure AI | [Hardware Reliability Intern [Winter 2027]](https://job-boards.greenhouse.io/figureai/jobs/4613067006) | San Jose, CA |
| 2026-10-27 | Ciena | [Optical Performance Lab Verification and Testing Co-op](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Optical-Performance-Lab-Verification-and-Testing-Co-op_R031991) | Ottawa |
| 2026-10-27 | GM | [2027 Summer Intern – AI & Hardware Analytics, ADPT](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Warren-Michigan-United-States-of-America/XMLNAME-2027-Summer-Intern---AI---Hardware-Analytics--ADPT_JR-202621756) | Warren, Michigan, United States of America; Milford, Michigan, United States of America |
| 2026-10-27 | GM | [2027 Summer Intern, Systems Engineer, ASD](https://generalmotors.wd5.myworkdayjobs.com/Careers_GM/job/Milford-Michigan-United-States-of-America/XMLNAME-2027-Summer-Intern--Systems-Engineer--ASD_JR-202621989) | Milford, Michigan, United States of America; Warren, Michigan, United States of America |
| 2026-10-26 | Analog Devices | [Embedded Systems Co-Op](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-MA-Boston/Embedded-Systems-Co-Op_R267689) | US, MA, Boston |
| 2026-10-26 | Applied Materials | [2027 Summer Electrical Engineering Intern - BS or MS (Gloucester, MA)](https://amat.wd1.myworkdayjobs.com/External/job/GloucesterMA/XMLNAME-2027-Summer-Electrical-Engineering-Intern---BS-or-MS--Gloucester--MA-_R2630812) | Gloucester,MA |
| 2026-10-26 | Nuro | [Software Engineer, AI Platform - Intern](https://nuro.ai/careersitem?gh_jid=7351061) | Mountain View, California (HQ) |
| 2026-10-26 | Skydio | [Autonomy Engineer Intern, Autonomy Infrastructure, Systems and Tools, 2027 (HQ)](https://jobs.ashbyhq.com/skydio/ec82eb16-a5b4-46e7-827a-326b33d7d2cb) | San Mateo, California, United States |
| 2026-10-26 | Skydio | [Autonomy Engineer Intern, Simulation & Robotics, 2027 (HQ)](https://jobs.ashbyhq.com/skydio/6f5caf41-fa1d-4208-9bdc-82c72e5d3f17) | San Mateo, California, United States |

### Full-time (40)

| Posted | Company | Role | Location |
|--------|---------|------|----------|
| 2026-11-08 | Ericsson | [RAN System Verification Professional](https://jobs.ericsson.com/careers/job/563121777356246) | Ottawa, ON, CA |
| 2026-11-08 | Microsoft | [Innovative Data Platform Solution Engineer](https://apply.careers.microsoft.com/careers/job/1970393557008790) | Toronto, ON, CA; Calgary, AB, CA; Vancouver, BC, CA; Ottawa, ON, CA |
| 2026-11-06 | AMD | [Mixed Signal Custom Layout  - Temporary/Seasonal](https://careers.amd.com/jobs/93711?lang=en-us) | MARKHAM, Canada |
| 2026-11-06 | Ciena | [Embedded Security Software Developer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-Security-Software-Developer---New-Grad_R032066) | Ottawa |
| 2026-11-06 | Ericsson | [RAN System Verification Professional](https://jobs.ericsson.com/careers/job/563121777519784) | Ottawa, ON, CA |
| 2026-11-05 | AMD | [IP-Post Silicon Validation Engineer](https://careers.amd.com/jobs/97341?lang=en-us) | VANCOUVER, Canada |
| 2026-11-05 | AMD | [IP-Post Silicon Validation Engineer](https://careers.amd.com/jobs/96261?lang=en-us) | MARKHAM, Canada |
| 2026-11-05 | Arm | [IP Verification Engineer](https://careers.arm.com/job/toronto/ip-verification-engineer/33099/102559123680) | Toronto, Canada |
| 2026-11-05 | MDA Space | [Systems Engineer, Missions](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=2d5d7a56-04bd-45b8-b057-814b59fd3b61) | Richmond, British Columbia, Canada |
| 2026-11-03 | AMD | [IP Silicon Validation Engineer](https://careers.amd.com/jobs/97103?lang=en-us) | VANCOUVER, Canada |
| 2026-11-02 | AMD | [RTL Design Engineer](https://careers.amd.com/jobs/87376?lang=en-us) | MARKHAM, Canada |
| 2026-11-02 | Ciena | [ASIC Front End Implementation Engineer](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Senior-Physical-Design-Engineer_R031691) | Ottawa |
| 2026-11-02 | Ciena | [Embedded Software Engineer](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Embedded-software-engineer_R031266) | Ottawa |
| 2026-11-02 | Ciena | [Hardware Engineer - New Grad](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Hardware-Engineer---New-Grad_R031914) | Ottawa |
| 2026-11-02 | Ciena | [Mixed Signal Design Engineer](https://ciena.wd5.myworkdayjobs.com/Careers/job/Ottawa/Mixed-Signal-Design-Engineer_R030994) | Ottawa |
| 2026-11-02 | Huawei | [Engineer - Optical Communication Systems (Test, Modeling & Sensing)](https://huaweicanada.recruitee.com/o/engineer-optical-communication-systems-test-modeling-sensing) | Ottawa, Ontario, Canada |
| 2026-11-02 | MDA Space | [Satellite Bus Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=e9f6a21e-c486-4ebf-9a82-7fb787af7f51) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-11-02 | MDA Space | [Satellite Electrical Propulsion Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=13713581-7e6f-4ed1-8a9b-7a9be4e13a78) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-11-02 | MDA Space | [Satellite Electrical Propulsion Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=54b10edf-751f-4890-b864-373b1ea7786d) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-11-02 | MDA Space | [Satellite Flight Software (FSW) Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=540fc56c-c323-46d2-8999-8ecc0a2cf271) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-11-02 | MDA Space | [Satellite TT&C/PDT Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=465bf57b-6fac-47dc-9e26-25109058ab70) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-11-02 | MDA Space | [Satellite TT&C/PDT Systems Engineer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=af876f95-db07-4ae5-8c02-83f115df577e) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-10-30 | AMD | [IP Silicon Validation Engineer](https://careers.amd.com/jobs/93586?lang=en-us) | MARKHAM, Canada |
| 2026-10-30 | AMD | [Systems Design Engineer](https://careers.amd.com/jobs/93526?lang=en-us) | MARKHAM, Canada |
| 2026-10-30 | Tenstorrent | [Software Engineer, Acceleration Kernel Development](https://job-boards.greenhouse.io/tenstorrent/jobs/4155609007) | Santa Clara, California, United States; Toronto, Ontario, Canada |
| 2026-10-29 | AMD | [DSP Systems Engineer](https://careers.amd.com/jobs/93754?lang=en-us) | OTTAWA, Canada |
| 2026-10-29 | MDA Space | [Power Electronics PCB Designer](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=93853f48-b76d-4281-9ee1-98449f442859) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-10-29 | MDA Space | [Test Engineer - Payload, Platform and Spacecraft](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=240fa344-ce98-4581-b104-2a467d48ebfa) | Sainte-Anne-de-Bellevue, Quebec, Canada |
| 2026-10-29 | MDA Space | [Test Engineer Payload, Platform et Spacecraft](https://recruiting.ultipro.ca/MAC5000MCDW/JobBoard/664818ff-3594-4bec-9f30-3394e59e19f3/OpportunityDetail?opportunityId=efed66d0-4fb6-46a9-bda1-380197de5e8b) | Sainte-Anne-de-Bellevue, Quebec, Canada |
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
<!-- JOBS:END -->
