# Lead Intelligence Agent

A small autonomous AI/ML workflow that qualifies commercial leads without manual supervision.

## What it does

The agent reads incoming lead messages from `data/leads.csv`, trains a lightweight text-classification model locally, classifies each lead as **hot**, **warm**, or **cold**, assigns a priority score and recommends the next commercial action.

The workflow runs automatically with **GitHub Actions** every 6 hours and also whenever the lead dataset or classifier changes. The result is written to `output/qualified_leads.csv` and summarized in `output/latest_report.md`.

## Why this project exists

This is a compact portfolio proof of applied AI + automation. It demonstrates:

- automated workflow execution;
- text classification with TF-IDF + Logistic Regression;
- lead prioritization;
- reproducible outputs;
- GitHub Actions scheduling;
- no paid API or external AI service required;
- synthetic data only.

## Architecture

```text
Lead data (CSV)
      |
      v
TF-IDF vectorization
      |
      v
Logistic Regression classifier
      |
      v
HOT / WARM / COLD
      |
      v
Priority score + recommended action
      |
      v
CSV output + Markdown report
      |
      v
Scheduled GitHub Action
```

## Run locally

```bash
python -m pip install -r projects/lead-intelligence-agent/requirements.txt
python projects/lead-intelligence-agent/src/qualify_leads.py
```

## Automation

The repository workflow `.github/workflows/lead-intelligence-agent.yml` runs:

- every 6 hours;
- manually through `workflow_dispatch`;
- when files under `projects/lead-intelligence-agent/data/` or `src/` change.

If the generated output changes, the workflow commits the new qualification report automatically.

## Current scope and limitations

This is a **functional portfolio automation**, not a claim of a commercial production deployment. The training set and incoming leads are synthetic. The classifier is intentionally small and auditable. A production version would normally connect to a CRM webhook, persist model/version metadata, add monitoring and possibly use an LLM for enriched reasoning or response generation.

## Possible next integrations

Kommo/CRM webhook → queue → classifier → AI enrichment → PostgreSQL/Sheets → Power BI/dashboard → consultant notification.
