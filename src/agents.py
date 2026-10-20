from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0.3)


def study_design_agent(state: dict) -> dict:
    research_question = state["research_question"]
    messages = [
        SystemMessage(content="""You are an expert epidemiologist specializing in study design.
Given a research question, recommend the most appropriate study design (RCT, cohort, 
case-control, cross-sectional, ecological) and explain why. Be concise and structured."""),
        HumanMessage(content=f"Research question: {research_question}")
    ]
    response = llm.invoke(messages)
    return {**state, "study_design": response.content}


def sample_size_agent(state: dict) -> dict:
    messages = [
        SystemMessage(content="""You are a biostatistician. Given a study design and research question,
provide sample size estimation guidance. Include: expected effect size, power (80-90%),
significance level (0.05), and formula/approach to use. Be practical and concise."""),
        HumanMessage(content=f"""Research question: {state['research_question']}
Study design: {state['study_design']}""")
    ]
    response = llm.invoke(messages)
    return {**state, "sample_size": response.content}


def confounding_checker_agent(state: dict) -> dict:
    messages = [
        SystemMessage(content="""You are an epidemiologist specializing in confounding and bias.
Given a study design, identify the top 5 potential confounding variables and suggest
specific control strategies for each. Format as a numbered list."""),
        HumanMessage(content=f"""Research question: {state['research_question']}
Study design: {state['study_design']}""")
    ]
    response = llm.invoke(messages)
    return {**state, "confounders": response.content}


def protocol_drafter_agent(state: dict) -> dict:
    messages = [
        SystemMessage(content="""You are a clinical research protocol writer for African healthcare contexts.
Draft a concise research protocol with these sections:
1. Background and Rationale
2. Study Objectives
3. Methodology
4. Sampling Strategy
5. Data Collection Tools
6. Ethical Considerations
7. Limitations

Keep it professional and suitable for a grant application."""),
        HumanMessage(content=f"""Research question: {state['research_question']}
Study design: {state['study_design']}
Sample size guidance: {state['sample_size']}
Key confounders to control: {state['confounders']}""")
    ]
    response = llm.invoke(messages)
    return {**state, "protocol": response.content}