def run():

    import streamlit as st
    from pypdf import PdfReader
    from langchain_text_splitters import CharacterTextSplitter
    from langchain_community.vectorstores import FAISS
    from langchain_community.embeddings import HuggingFaceEmbeddings
    import ollama

    # Page settings
    st.set_page_config(page_title="Document RAG Assistant", page_icon="📄")

    st.title(" Document RAG AI Assistant")
    st.write("Upload a PDF and ask questions from it.")

    # Upload PDF
    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

    if uploaded_file:

        # Read PDF
        pdf_reader = PdfReader(uploaded_file)

        text = ""
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content

        # Split text into chunks
        splitter = CharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        docs = splitter.split_text(text)

        # Create embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Create vector database
        vector_db = FAISS.from_texts(docs, embeddings)

        st.success("Document processed successfully!")

        # Question input
        question = st.text_input("Ask a question about the document")

        if question:

            # Search similar chunks
            results = vector_db.similarity_search(question, k=3)

            context = "\n".join([doc.page_content for doc in results])

            # Prompt
            prompt = f"""
You are an AI assistant.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""

            # AI thinking animation
            with st.spinner(" AI is thinking..."):

                response = ollama.chat(
                    model="llama3",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

            answer = response["message"]["content"]

            # Display answer
            st.markdown("###  AI Answer")
            st.write(answer)

            # Show sources
            st.markdown("### 📚 Source Chunks")

            for doc in results:
                st.info(doc.page_content[:300] + "...")