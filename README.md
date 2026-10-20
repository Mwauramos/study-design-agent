# AI-Assisted Epidemiological Study Design Agent

A multi-agent LangGraph pipeline that helps epidemiologists design rigorous research studies. Built as part of the ZENIK.AI Computational Epidemiology Portfolio.

## Live Demo

https://study-design-agent-nxw7lx8xzv4yhjkm9mannj.streamlit.app

## What It Does

Enter a research question and the system runs four sequential AI agents:

1. **Study Design Agent** - Recommends the optimal study design (RCT, cohort, case-control, cross-sectional, ecological)
2. **Sample Size Agent** - Estimates required sample size with statistical justification
3. **Confounding Checker Agent** - Identifies top 5 confounding variables and control strategies
4. **Protocol Drafter Agent** - Generates a structured grant-ready research protocol

## Tech Stack

- LangGraph (multi-agent orchestration)
- LangChain + OpenAI GPT-4o
- Streamlit

## Project Structure

```
study-design-agent/
├── src/
│   ├── agents.py
│   └── graph.py
├── app.py
├── requirements.txt
└── .env
```

## Setup

```bash
conda create -n study-agent python=3.10 -y
conda activate study-agent
pip install -r requirements.txt
```

Add your OpenAI API key to `.env`:


Run locally:

```bash
streamlit run app.py
```

## Author

Amos Mwaura | ZENIK.AI | Healthcare AI Engineering  
mwauramos.n@gmail.com
