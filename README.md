# AI Study Design Agent

A multi-agent system that takes a research question and produces a complete epidemiological study protocol, including study design, sample size calculation, confounder identification, and a grant-ready protocol document.

**Live Demo**: https://study-design-agent-nxw7lx8xzv4yhjkm9mannj.streamlit.app

---

## What This Does

Designing an epidemiological study requires coordinating multiple decisions: choosing the right study design for the question, calculating an appropriate sample size, identifying potential confounders, and documenting everything in a format suitable for ethics review or grant submission. This agent automates that workflow.

A researcher enters a question — for example, "What is the association between indoor air pollution and childhood pneumonia in Nairobi informal settlements?" — and the system produces a structured protocol document ready for review.

---

## Features

- Multi-agent LangGraph workflow with specialised agents for each protocol component
- Study design selection based on research question type
- Sample size calculation with justification
- Confounder and bias identification
- Grant-ready protocol document generation
- Streamlit interface for interactive use

---

## Agent Architecture

The system uses a LangGraph state machine with four agents running in sequence:

1. **Design Agent** — selects the appropriate study design and justifies the choice
2. **Sample Size Agent** — calculates sample size with assumptions stated
3. **Confounder Agent** — identifies key confounders and recommends control strategies
4. **Protocol Writer** — synthesises all outputs into a structured protocol document

---

## Tech Stack

- Python
- LangGraph (multi-agent orchestration)
- LangChain
- GPT-4o (OpenAI)
- Streamlit

---

## Project Structure

```
study-design-agent/
├── agents/                # Individual agent definitions
├── graph/                 # LangGraph state machine
├── app.py                 # Streamlit interface
└── requirements.txt
```

---

## Running Locally

```bash
git clone https://github.com/Mwauramos/study-design-agent
cd study-design-agent
pip install -r requirements.txt
# Add your OpenAI API key to .env
streamlit run app.py
```

---

## Context

Part of the ZENIK.AI portfolio — healthcare AI and data engineering projects for African health systems.

**Author**: Amos Mwaura  
**Contact**: mwauramos.n@gmail.com  
**Portfolio**: https://mwauramos.github.io/zenik-ai
