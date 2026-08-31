<div align="center">

<img src="https://raw.githubusercontent.com/Sembla/Sembla/main/assets/banner-applied-ai.png" width="100%" alt="Henrique Sembla — Applied AI, Process Automation and Data Analysis"/>

# Henrique Sembla

**Applied AI · Process Automation · Data Analysis**

I build practical solutions that connect AI, automation and data to real technical and operational workflows.

[Saldo Real — Live](https://saldo-real-production.up.railway.app/) · [LinkedIn](https://www.linkedin.com/in/henriquessembla) · [Email](mailto:henriquesembla@gmail.com)

</div>

---

## Selected projects

These are the strongest examples of my current work. Each one includes public evidence, tests, automation or a working demonstration.

| Project | What it demonstrates | Verification |
|---|---|---|
| **[Saldo Real](https://github.com/Sembla/Saldo-Real)** | Live personal-finance PWA focused on forward-looking cash-flow decisions: safe-to-spend balance, recurring movements, conservative income confidence, 7/30-day projections, financial-flow health and decision simulation. Native Node.js API, SQLite persistence, local visitor mode, JSON backup/export and responsible product limits. | **[Live demo](https://saldo-real-production.up.railway.app/)** · Railway deployment · in-app help · 10-page user manual · automated domain/auth/API tests |
| **[Lead Intelligence Agent](https://github.com/Sembla/Sembla/tree/main/projects/lead-intelligence-agent)** | Autonomous lead-qualification workflow using Python, TF-IDF and Logistic Regression to classify HOT/WARM/COLD leads, calculate priority and recommend the next commercial action. | **GitHub Actions verified** · scheduled every 6 hours · reproducible synthetic dataset · generated CSV + Markdown report |
| **[AI ERP Assistant](https://github.com/Sembla/ai-erp-assistant)** | Node.js application for querying synthetic ERP-like operational data in Portuguese. Deterministic analytics, HTTP API, responsive interface and an optional aggregate-only LLM explanation mode. | **[Live demo](https://ai-erp-assistant-2ehm.onrender.com/)** · [Interface capture](https://github.com/Sembla/ai-erp-assistant/blob/main/docs/evidence/live-demo.jpg) · [30/30 evaluation fixtures](https://github.com/Sembla/ai-erp-assistant/blob/main/docs/evidence/evaluation-report.json) · [Privacy report](https://github.com/Sembla/ai-erp-assistant/blob/main/docs/evidence/privacy-report.json) · 14 automated tests |
| **[Engineering BOM Intelligence](https://github.com/Sembla/Engineering-BOM-Intelligence)** | Tested workflow for turning neutral CAD-style project data into a normalized bill of materials with deterministic quality indicators and CSV export. | [Reproducible evidence snapshot](https://github.com/Sembla/Engineering-BOM-Intelligence/blob/main/docs/evidence/demo-summary.svg) · fictional public sample · normalized export · 16 automated tests |

### Featured live product — Saldo Real

**Question:** how much money is actually safe to spend before upcoming obligations create a cash-flow problem?

Saldo Real models the next 7 and 30 days instead of only describing past transactions. It preserves a user-defined reserve, applies confidence only to uncertain income, identifies the lowest projected balance and lets the user simulate paying now, waiting or splitting a purchase before making the decision.

**Functional evidence:** the public Railway deployment supports visitor mode without an account, recurring income/expenses, projections, decision simulation, plans, account mode, JSON backup/export and an in-app user guide. The repository documents the calculation rules, architecture, security decisions and product limitations.

**Status:** 🟢 Live MVP · **Deployment:** Railway · **Version:** 0.3.2

[Open live application](https://saldo-real-production.up.railway.app/) · [View source](https://github.com/Sembla/Saldo-Real)

<div align="center">

<a href="https://ai-erp-assistant-2ehm.onrender.com/">
  <img src="https://raw.githubusercontent.com/Sembla/ai-erp-assistant/main/docs/evidence/live-demo.jpg" width="78%" alt="AI ERP Assistant live interface"/>
</a>

</div>

## About me

My background combines IT infrastructure, engineering projects, technical visualization and data. That mix shaped the way I work: I start with the process and the people who use it, then choose the simplest technology that can make the work better.

Sometimes that means a Python automation, an API or a dashboard. In other cases, it means using generative AI or real-time 3D visualization to make technical information easier to understand. I also care about the less visible part of the work: testing outputs, documenting limitations and keeping sensitive information out of public examples.

My current focus is applied AI, process automation and data analysis. The projects in this profile show what I built, how I made the decisions and where each prototype still has limitations.

## Applied case studies

### [AI-assisted project presentation](case-studies/ai-commercial-presentation/README.md)

[![AI-assisted project presentation preview](case-studies/ai-commercial-presentation/assets/tour-preview.gif)](case-studies/ai-commercial-presentation/README.md)

An anonymized proof of concept showing how sanitized technical input can be transformed into a conceptual visualization and an AI-generated virtual tour. The documentation separates conceptual output from technical documentation and records known generative-AI distortions.

**Evidence:** [case documentation](case-studies/ai-commercial-presentation/README.md) · [technical pipeline](case-studies/ai-commercial-presentation/pipeline/README.md) · [source code](case-studies/ai-commercial-presentation/pipeline/media_pipeline.py)

### [Real-time retail tour with Twinmotion](case-studies/twinmotion-retail-tour/README.md)

[![Twinmotion retail tour preview](case-studies/twinmotion-retail-tour/assets/tour-preview.gif)](case-studies/twinmotion-retail-tour/README.md)

A fictional pharmacy environment transformed into a controlled 3D walkthrough with Twinmotion. The public case uses a conceptual redraw instead of the technical source layout and clearly distinguishes real-time 3D visualization from generative video.

**Evidence:** [case documentation](case-studies/twinmotion-retail-tour/README.md) · [sanitized layout](case-studies/twinmotion-retail-tour/assets/layout-conceitual-sanitizado.png) · [optimized tour](case-studies/twinmotion-retail-tour/assets/tour-twinmotion.mp4)

### [AI-assisted product creatives](case-studies/sbl-tech-ai-creatives/README.md)

Two short product creatives developed with AI-assisted video workflows, human review and channel-specific editing. Reported campaign results were **more than 10,000 people reached per video in approximately two days**, plus **more than 2,000 store-directed actions**. The case separates reach and traffic from verified sales attribution.

**Evidence:** [case documentation](case-studies/sbl-tech-ai-creatives/README.md) · [media manifest](case-studies/sbl-tech-ai-creatives/media-manifest.json) · [FIFINE preview](case-studies/sbl-tech-ai-creatives/assets/fifine-preview.gif) · [XZONE preview](case-studies/sbl-tech-ai-creatives/assets/xzone-preview.gif)

## Additional technical prototypes

| Project | Technical focus | Current scope |
|---|---|---|
| [Data Insight AI](https://github.com/Sembla/Data-insight-ai) | Sales KPIs, local deterministic answers and aggregate-only optional LLM context | Portfolio prototype · 8 automated tests |
| [GenAI Risk Analyst Pro](https://github.com/Sembla/GenAI-Risk-Analyst-Pro) | Deterministic synthetic classification, TF-IDF retrieval and explanation-only optional LLM | Educational architecture prototype · 9 automated tests |

## Technical toolkit

| Area | Tools and experience |
|---|---|
| Applied AI | Generative AI, prompt engineering, image and video workflows, output validation |
| Programming & automation | Python, JavaScript, TypeScript, Node.js, REST APIs, Git and GitHub |
| Data | SQL, Power BI, data analysis and KPI development |
| Engineering & visualization | AutoCAD, TopSolid Wood, Twinmotion, real-time 3D visualization and BOM workflows |
| Infrastructure & governance | Windows Server, Active Directory, cloud fundamentals, cybersecurity and ISO 27001 concepts |

## Working standards

- Public software projects use synthetic, fictional or anonymized data.
- Deterministic rules remain separate from optional LLM explanations where accuracy matters.
- Claims are linked to evidence when verification is available.
- Limitations are documented instead of hidden.
- Portfolio prototypes are not presented as production systems.

## Education

- Bachelor's degree in Computer Science.
- Postgraduate studies in Artificial Intelligence and Data Science.
- MBA studies in Cybersecurity and Project Management.
- Postgraduate studies in Systems Analysis and Development.

## Repository status

The original [GenAI Risk Analyst](https://github.com/Sembla/genai-risk-analyst) and [Data Insight AI Revision 1](https://github.com/Sembla/Data-insight-ai-REV1) are superseded versions and are not part of the selected portfolio.

---

<div align="center">

Open to opportunities involving **Applied AI, Automation, Data and Process Improvement**.

[LinkedIn](https://www.linkedin.com/in/henriquessembla) · [Email](mailto:henriquesembla@gmail.com)

</div>
