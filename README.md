#  Voice RAG AI Assistant

An AI-powered assistant that combines Chat, Document Question Answering, and Voice Interaction using LLMs.

---

##  Features

- Chat AI (Llama3 via Ollama)
- Document RAG (Ask questions from PDF)
-  Voice Assistant (Speech → Text → AI Response)
-  Reduced hallucination using RAG + Top-K retrieval

---

##  Tech Stack

- Streamlit
- Ollama (Llama3)
- FAISS (Vector Database)
- Sentence Transformers
- SpeechRecognition
- Pydub + FFmpeg

---

##  How it Works

1. Upload PDF → split into chunks  
2. Convert text into embeddings  
3. Store in FAISS  
4. Retrieve Top-K relevant chunks  
5. Send context to LLM  
6. Generate grounded response  

---

##  Voice Pipeline

Speech → FFmpeg → WAV → SpeechRecognition → LLM → Answer

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run main_app.py
