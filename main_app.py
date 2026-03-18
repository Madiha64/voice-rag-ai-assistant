import streamlit as st
import ollama
from io import BytesIO

st.set_page_config(page_title="AI Assistant", page_icon=" ")

st.title(" AI Assistant Dashboard")

tool = st.sidebar.radio(
    "Choose AI Tool",
    ["💬 Chat AI", "📄 Document RAG", "🎤 Voice Assistant"]
)

# ---------------- CHAT AI ----------------

if tool == "💬 Chat AI":

    st.header(" Chat AI")

    user_input = st.text_input("Ask something")

    if user_input:

        with st.spinner("AI is thinking..."):

            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": user_input}]
            )

        answer = response["message"]["content"]

        st.markdown(" AI Answer")
        st.write(answer)


# ---------------- DOCUMENT RAG ----------------

elif tool == "📄 Document RAG":

    st.header(" Document RAG Assistant")

    from pypdf import PdfReader
    from langchain_text_splitters import CharacterTextSplitter
    from langchain_community.vectorstores import FAISS
    from langchain_community.embeddings import HuggingFaceEmbeddings

    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file:

        pdf_reader = PdfReader(uploaded_file)

        text = ""
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content

        splitter = CharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        docs = splitter.split_text(text)

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vector_db = FAISS.from_texts(docs, embeddings)

        st.success("Document processed successfully!")

        question = st.text_input("Ask a question about the document")

        if question:

            results = vector_db.similarity_search(question, k=3)

            context = "\n".join([doc.page_content for doc in results])

            prompt = f"""
Context:
{context}

Question:
{question}
"""

            with st.spinner("AI is thinking..."):

                response = ollama.chat(
                    model="llama3",
                    messages=[{"role": "user", "content": prompt}]
                )

            answer = response["message"]["content"]

            st.markdown(" AI Answer")
            st.write(answer)


# ---------------- VOICE ASSISTANT ----------------
elif tool == "🎤 Voice Assistant":

    st.header("🎤 Voice AI Assistant")

    from streamlit_mic_recorder import mic_recorder

    st.write("Click the microphone and speak")

    audio = mic_recorder(
        start_prompt="🎤 Start Recording",
        stop_prompt="⏹ Stop Recording",
        just_once=True
    )

    if audio:

        st.audio(audio["bytes"])

        # ✅ NEW CODE HERE (PASTE THIS BLOCK)
        from io import BytesIO
        from pydub import AudioSegment
        import tempfile
        import speech_recognition as sr

        audio_bytes = audio["bytes"]

        audio_segment = AudioSegment.from_file(BytesIO(audio_bytes), format="webm")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
            audio_segment.export(tmpfile.name, format="wav")
            wav_path = tmpfile.name

        recognizer = sr.Recognizer()

        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        query = recognizer.recognize_google(audio_data)

        st.write("You said:", query)

        # 👇 KEEP YOUR OLLAMA PART SAME
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": query}]
        )

        answer = response["message"]["content"]

        st.markdown("AI Answer")
        st.write(answer)