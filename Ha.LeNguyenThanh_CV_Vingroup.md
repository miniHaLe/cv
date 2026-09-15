# Le Nguyen Thanh Ha

**AI Product Engineer — I take an operational problem from business case to a system in production, and I own every layer in between. Alone when the scope allows it; leading the team when it does not.**

+84 396 913 492 · thanhha.le@outlook.com · linkedin.com/in/hale03 · github.com/miniHaLe · Ho Chi Minh City — available for Hanoi relocation or remote

---

## Executive Summary

Twelve AI and business systems in production across retail, hospitality, gaming, logistics and finance operations. Six of them I delivered end to end on my own — requirements, architecture, model, backend, interface, security review, deployment and handover. The other six I built as primary author inside product teams, including the flagship platform of my current company.

What distinguishes the work is not the models. It is that every system was built to be **audited, operated and extended by people other than me**: phased delivery with written completion criteria and sign-off gates, human confirmation before automated output is treated as fact, role-based access enforced structurally, dead-letter queues so no failure is silent, and rollback on every release. That is the discipline a finance function expects and an AI function rarely gets.

| Headline | Evidence |
|---|---|
| **12** production systems | 4 at DFlo · 6 independent contracts · 1 at Rainscales · 1 at Viettel Solutions |
| **6** delivered solo, end to end | requirements → security review → deployment → client handover |
| **~3×** inference throughput on unchanged hardware | 120 requests/s at TP95 latency, no accuracy regression |
| **101** security findings closed | across 3 remediation releases, manual review signed off |
| **4** languages at launch | EN / VI / JA / ZH on a customer-facing product, day one |

| What I delivered | Business outcome | Verifiable evidence |
|---|---|---|
| TesselAI retail image scoring — Viettel Solutions | Manual field-audit review replaced by automated scoring across the retail footprint | Business case authored → built → released to production; ~3× throughput gain |
| Sauron restaurant AI platform — DFlo | Live operations visibility replacing manual floor checks; automated food quality control | Primary author, six services, 399 commits |
| Financial analytics platform — independent contract | Inconsistent finance, KPI and HR workbooks reconciled into governed, traceable dashboards | 11 phases with written completion criteria; 101 security findings closed |
| Multi-branch operations platform — independent contract | Spreadsheet operations of a repair chain replaced by one system with branch-level data isolation | 21 business resources live; isolation enforced in the access token |
| Casino floor intelligence — Rainscales | Customer and staff detection under camera placements that had defeated earlier attempts | 95% mAP at ~25 FPS on one GPU |

---

## Where I Would Start at Vingroup

I do not know your internal systems. I do know which of my delivered systems map onto the problems a group finance function and a group AI function carry, and I would rather show working code than a slide.

**For the finance function**

- **Subsidiary reporting consolidation.** My financial analytics platform already takes inconsistent workbooks from different sources, proposes how they relate, waits for a human to confirm, and produces traceable dashboards. That is the shape of group-level consolidation across operating companies — with the audit trail built in.
- **Governed AI, not black-box AI.** Every number the system produces can be traced to a source cell and a confirmed mapping. Accuracy gates refuse to report a pass on synthetic data. This is the control posture an internal-audit or CFO office can sign off on.
- **Document and meeting intelligence.** Transcription, summary, PDF/XLSX reporting and a searchable cross-meeting knowledge base, deployed on Azure with infrastructure-as-code — reproducible, auditable, and already in production for a distribution-centre client.

**For the AI function**

- **Computer vision that survives the real site.** Retail shelf scoring, restaurant floor and kitchen monitoring, casino floor detection under bad camera angles, warehouse rack analysis — four industries, all in production. The same stack applies to retail tenants, hospitality properties, manufacturing and logistics sites, and residential security estates.
- **Natural-language search over a CCTV estate.** Managers describe an incident and get the exact clip. Built once for a 100-camera network, once for a restaurant chain.
- **LLM agents with guardrails over operational data.** Non-technical managers ask questions in plain language; the agent answers from history with conversation memory and constraints on what it may assert.
- **GPU cost at scale.** ~3× throughput on the same hardware through inference-path re-engineering, and 30 → 5 FPS detection cadence with tracker interpolation at no visible quality loss. At group scale, that is the difference between a cost line and a capital request.

---

## How I Lead Delivery

I have led projects, not headcount — and I am ready to do both. The evidence:

- **I own the business case, not just the build.** At Viettel Solutions I identified the opportunity, wrote the proposal, and aligned business and field-operations teams on measurable acceptance criteria before a model was trained — so "correct" was defined by the business, not by the engineer.
- **I run engagements as phases with sign-off gates.** Six independent contracts delivered under written completion criteria per phase, client confirmation at each gate, and a handover that let non-technical staff operate and recover the system without me. An 11-phase financial platform was delivered this way with zero scope disputes.
- **I set the engineering standard others inherit.** Primary author of a six-service platform now maintained by a team: CI/CD with automatic rollback, documented architecture, unit-tested calculation modules, and a four-language interface shipped on day one.
- **I have shipped inside teams as well as alone.** Building-wide CCTV retrieval delivered in a team of five; products at DFlo, Rainscales and Viettel delivered alongside product, business and operations colleagues.

**How I would run a team at Vingroup:** one accountable owner per service, tracer-bullet delivery (thin end-to-end slices before depth), a weekly working demo to the business sponsor, written completion criteria per phase, and a handover package as a deliverable rather than an afterthought. It is the method I already apply to myself.

---

## Ways to Engage

I am flexible on structure; the working method above stays the same in every case.

| Model | What it looks like |
|---|---|
| **Full-time employee** | AI product or platform engineer, or technical lead of a small delivery team. Hanoi relocation or remote. |
| **Fixed-scope project contract** | A defined outcome delivered in phases with written completion criteria, sign-off at each gate, and full handover. This is how all six independent systems were delivered. |
| **Embedded technical lead** | Stand up or unblock an internal team on a specific system, transfer the method and the code, then step back. |

Available immediately. Private repositories can be opened for technical review under a mutual NDA.

---

## Professional Experience

### AI Engineer — DFlo · Jul 2025 – Present

Primary author and technical owner of *Sauron*, the company's flagship AI platform for restaurant operations, plus three further client-facing AI products.

- **Turned a manual floor-check process into a live operations view.** Architected a six-service platform (API gateway, computer-vision engine, food quality control, analytics agent, dashboard, and a Postgres/MongoDB/Redis data layer) delivering real-time table occupancy, movement heatmaps, automated food quality scoring, and conversational reporting in a single product — **399 commits, primary author**.
- **Removed manual quality sampling from the kitchen line.** Designed an automated food quality-control pipeline on a vision-language model: classification across 24 dish variants, asymmetric scoring, server-side automatic capture. Engineered for accountability — **circuit breakers, a dead-letter queue so no evaluation is silently lost**, and streamed diagnostics so operators see *why* a dish failed.
- **Restored a fully failed production line and closed the gap permanently.** Diagnosed a 100% quality-control failure caused by configuration values silently not reaching the vision model, fixed the root cause across all three consumers of that configuration, and rebuilt the retry path so exhausted retries always reach the dead-letter queue with a diagnosable reason.
- **Unlocked multi-user operation.** Built a session-isolation layer giving each operator an independent camera session — the change that took the platform from single-operator demo to concurrent commercial use.
- **Made operations data self-serve for non-technical managers.** Shipped natural-language video moment retrieval (describe the moment, get the clip) and an LLM analytics agent with guardrails and conversation memory over historical operations data.
- **Delivered in four markets from day one.** Owned the customer-facing dashboard end to end with **full EN / VI / JA / ZH localisation**, accessibility remediation, and analytics panels backed by unit-tested calculation modules.
- **Cut infrastructure cost without degrading the product.** Reduced GPU detection cadence 30 → 5 FPS using tracker interpolation; automated releases with **CI/CD and automatic rollback**.

**Additional products delivered at DFlo**
- **Conveyor-belt dish counting for KichiKichi (Golden Gate Group)** — production computer-vision system counting dishes by category through every stage of the belt across dual cameras, with live dashboards for store managers. Cut the API surface from 30+ endpoints to 13.
- **Enterprise video intelligence platform** — extended a research retrieval system into a production service handling **video libraries of 24+ hours**, with vector search, batch processing and session caching.
- **Meeting intelligence for a distribution-centre client** — recording through transcription, AI summary, PDF/XLSX reporting and a searchable cross-meeting knowledge base; deployed to **Microsoft Azure with infrastructure-as-code**.

### Independent Delivery Practice — fixed-scope contracts · Nov 2024 – Aug 2026

Six production business systems delivered solo under fixed-scope contracts — requirements, architecture, build, security review, deployment and handover documentation. Clients were Vietnamese SMEs with no in-house IT function, so every system had to be operable and recoverable by non-technical staff.

- **Financial analytics platform — built for people who do not trust a black box.** Clients upload inconsistent financial, KPI and HR workbooks; the platform reconciles them into structured tables, **proposes how the files relate and waits for a human to confirm before anything is treated as fact**, and produces editable dashboards. Delivered across **11 phases with documented completion criteria**; three remediation releases closed **101 distinct security findings**, and a manual security review was completed and signed off. Accuracy gates are enforced mechanically — the test harness *refuses to report a pass* on synthetic data.
- **Multi-branch operations platform for an appliance-repair chain** — replaced spreadsheet operations with a single system covering **21 business resources**. Access control is structural: **branch-level data segregation enforced in the access token itself**, sensitive actions permission-guarded, confidential fields stripped before data leaves the server. Migrated the production host and automated database and API releases so the client's releases stopped depending on my availability.
- **Content and tax-agency systems** *(3 clients)* — one built deliberately in **zero-dependency Node.js** so the client can run, patch and back up the system indefinitely without a build toolchain or vendor lock-in; rate limiting, forced credential setup on first use, automated search-engine indexing.
- **Commercial websites with real administrative back-ends** *(3 clients)* — content management, file handling, scripted deployment, handed over with operating documentation.

### AI Engineer — Rainscales (Contract) · Feb 2025 – Jun 2025

- Delivered customer and staff detection with multi-camera counting for a casino client under difficult physical camera placement — the constraint that had blocked earlier attempts — at **95% mAP and ~25 FPS on a single GPU**, meeting the client's real-time threshold.
- Built behavioural recognition (hand-raising, head-turning) so floor staff are directed to guests who need help, without additional headcount.
- Produced warehouse layout placement rules for Linfox from depth-estimation and rack-detection analysis, converting camera output into an operational decision.

### AI Engineer — Viettel Solutions · Jun 2023 – Jan 2025

**TesselAI — from internal proposal to a commercial product in production**

- **Identified the opportunity, wrote the business case, then built and released the product** — automated market image scoring using computer vision, adopted commercially and replacing manual field-audit review across the retail footprint.
- **Delivered ~3× throughput on unchanged hardware** by re-engineering the inference path — 120 requests per second at TP95 latency with no loss of accuracy. Capacity gained without capital expenditure.
- Trained and deployed the detection and segmentation models running in the production scoring pipeline.
- Worked directly with business and field-operations teams to convert audit rules into measurable, testable acceptance criteria.

---

## Governance, Security & Delivery Discipline

Drawn from delivered work, for a finance- or audit-minded reader:

- **Human confirmation before trust.** No inferred relationship between client workbooks is acted on until a person confirms it. Automation proposes; a human approves.
- **Remediation with evidence.** 101 security findings identified and closed across three releases, plus a completed manual security review with outstanding items explicitly recorded rather than quietly dropped.
- **Access control by design.** Branch-scoped data isolation enforced at the token level, role-based permissions on sensitive actions, least-privilege data projections.
- **No silent failure.** Dead-letter queues and diagnostic error reporting, so a failed automated evaluation is always visible and recoverable.
- **Reversible releases.** Continuous delivery with automatic rollback; deployment documented as runbooks so the client never depends on one individual.

---

## Technical Capability

- **Artificial Intelligence:** computer vision (YOLO11/YOLOX, OpenCV, person re-identification and tracking), vision-language models (Gemini), LLM agents with guardrails (Agno, LangChain), retrieval-augmented generation, speech recognition, PyTorch, TensorFlow, ONNX, Triton
- **Backend & Data:** Python (FastAPI, Celery, Flask), TypeScript (NestJS, Express), PostgreSQL, MongoDB, Redis, vector databases, PySpark, Pandas, Power BI
- **Frontend:** Next.js, React, TypeScript, Tailwind, multi-locale product delivery (EN/VI/JA/ZH), automated testing
- **Cloud & Operations:** Google Cloud, Microsoft Azure (Container Apps, infrastructure-as-code), Docker, CI/CD with automated rollback, self-hosted runners, secure reverse proxy and tunnel access
- **Languages:** Python · TypeScript / JavaScript · SQL · Go · Bash
- **Spoken:** Vietnamese (native) · English (professional working proficiency)

---

## Selected Projects & Open Source

- **Building-wide CCTV action retrieval** *(team of 5)* — natural-language video search across a 100-camera network so security teams find incidents in seconds instead of hours.
- **Open-source contributor, PyTorch AnimeGAN** *(188+ stars)* — improved training stability and added multi-GPU support to a widely used image-generation project.

---

## Verification

Engineering claims are independently checkable at **github.com/miniHaLe** — 797 commits across 75 peer-reviewed pull requests. Commercial repositories are private; read access under a mutual NDA within two business days.
