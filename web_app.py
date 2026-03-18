import streamlit as st
from rag_pipeline import ask_question

st.title("🎤 Voice RAG AI Assistant")

question = st.text_input("Ask a question")

if question:
    answer = ask_question(question)

    st.write("### 🤖 AI Answer")
    st.write(answer)