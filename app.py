import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from src.graph import build_graph

st.set_page_config(
    page_title="ZENIK.AI | Study Design Agent",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 AI-Assisted Epidemiological Study Design Agent")
st.markdown("---")

st.markdown("""
This tool uses a multi-agent LangGraph pipeline to help epidemiologists design 
rigorous research studies. Enter your research question below and the system will:
- Recommend the optimal study design
- Estimate required sample size
- Identify key confounding variables
- Draft a structured research protocol
""")

research_question = st.text_area(
    "Enter your epidemiological research question:",
    placeholder="e.g. What is the association between indoor air pollution and acute respiratory infections in children under 5 in rural Kenya?",
    height=100
)

if st.button("🚀 Generate Study Design", type="primary"):
    if not research_question.strip():
        st.warning("Please enter a research question.")
    else:
        graph = build_graph()
        
        initial_state = {
            "research_question": research_question,
            "study_design": "",
            "sample_size": "",
            "confounders": "",
            "protocol": ""
        }
        
        with st.spinner("Running multi-agent pipeline..."):
            with st.status("Agent progress", expanded=True) as status:
                st.write("🔬 Study Design Agent running...")
                result = graph.invoke(initial_state)
                st.write("📊 Sample Size Agent running...")
                st.write("🔍 Confounding Checker Agent running...")
                st.write("📝 Protocol Drafter Agent running...")
                status.update(label="Pipeline complete!", state="complete")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Recommended Study Design")
            st.markdown(result["study_design"])
            
            st.subheader("📊 Sample Size Guidance")
            st.markdown(result["sample_size"])
        
        with col2:
            st.subheader("⚠️ Key Confounding Variables")
            st.markdown(result["confounders"])
        
        st.subheader("📄 Draft Research Protocol")
        st.markdown(result["protocol"])
        
        st.download_button(
            label="📥 Download Protocol",
            data=result["protocol"],
            file_name="research_protocol.txt",
            mime="text/plain"
        )

st.markdown("---")
st.caption("ZENIK.AI | Healthcare AI Engineering | Amos Mwaura")