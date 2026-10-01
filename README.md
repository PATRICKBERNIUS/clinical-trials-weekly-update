# Weekly Clinical Trials Digest

A pipeline that fetches clinical trials with results posted in the last week from
ClinicalTrials.gov, uses an LLM to curate and summarize the most noteworthy
findings across therapeutic areas, and emails a weekly briefing — so I can stay
current on interesting science without reading individual trial listings myself.

## Status
- [x] Fetch recently-results-posted trials from the ClinicalTrials.gov API
- [x] LLM-generated weekly briefing, organized by category, curated for interest
- [x] Email delivery
- [ ] Scheduled automation via GitHub Actions
- [ ] Tests + CI

## How it works
1. `fetch_studies.py` queries the ClinicalTrials.gov v2 API for trials whose
   results were first posted in the last 7 days (`ResultsFirstPostDate`)
2. `llm_summary.py` sends the trial data to Claude, which selects the most
   noteworthy findings and writes a categorized briefing in plain language
3. `send_email.py` emails the briefing

## Setup
1. `pip install -r requirements.txt`
2. Create a `.env` file with:
   ```
   CLAUDE_API=your_anthropic_api_key
   GMAIL_ADDRESS=your_gmail_address
   GMAIL_APP_PASSWORD=your_gmail_app_password
   ```
3. `python run.py`

## Data source
[ClinicalTrials.gov API v2](https://clinicaltrials.gov/data-api/api) — free,
public, no API key required.