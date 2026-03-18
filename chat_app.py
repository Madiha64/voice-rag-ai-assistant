import streamlit as st
from rag_pipeline import ask_question

st.set_page_config(page_title="RAG AI Assistant", page_icon="🤖")

st.title(" RAG AI Assistant")
st.write("Ask questions from your knowledge base.")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    if st.button(" Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:

    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI answer
    with st.spinner("Thinking..."):
        answer = ask_question(user_input)

    # Show AI message
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )