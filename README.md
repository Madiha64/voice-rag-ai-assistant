# Voice RAG AI Assistant

An AI-powered multi-agent assistant built using **LangChain, LangGraph, and MCP-style client/server architecture**.

The system combines conversational AI, document-based question answering, web search, tool execution, vision-related tasks, and voice interaction in a unified agentic workflow.

---

## Project Overview

This project demonstrates how multiple AI capabilities can be coordinated through an **agentic architecture**.

Instead of sending every user query directly to one LLM, the system uses:

- **LangChain** for LLM and RAG components
- **LangGraph** for agent orchestration and routing
- **MCP-style architecture** for connecting the main agent system with external tools/services
- **Ollama** for local LLM inference
- **Streamlit** for the user interface

---

## Key Features

- 💬 Conversational AI
- 📄 PDF Document Question Answering
- 🔎 Web Search
- 🧮 Tool/Calculation Agent
- 👁️ Vision Agent
- 🎤 Voice Assistant
- 🧠 Document-based RAG
- 🔀 LangGraph-based agent routing
- 🔌 MCP-style tool/client-server communication
- 🖥️ Streamlit interactive interface
- 🤖 Local LLM inference using Ollama

---

## 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │       User          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Streamlit       │
                         │      Interface      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     LangGraph       │
                         │   Agent Workflow    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Planner        │
                         │   Agent Routing     │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
        ┌───────────┐        ┌───────────┐        ┌───────────┐
        │   Chat    │        │    RAG    │        │    Web    │
        │   Agent   │        │   Agent   │        │   Agent   │
        └───────────┘        └─────┬─────┘        └─────┬─────┘
                                   │                    │
                                   └────────┬───────────┘
                                            │
                                            ▼
                                   ┌────────────────┐
                                   │ MCP-style      │
                                   │ Client/Server  │
                                   │ Communication  │
                                   └───────┬────────┘
                                           │
                         ┌─────────────────┼─────────────────┐
                         │                 │                 │
                         ▼                 ▼                 ▼
                    ┌─────────┐       ┌─────────┐       ┌─────────┐
                    │  Tools  │       │ Vision  │       │  Web    │
                    │ Service │       │ Service │       │ Search  │
                    └─────────┘       └─────────┘       └─────────┘
```

---

## LangGraph Orchestration

LangGraph is used to control the multi-agent workflow.

The graph contains nodes for:

1. Planner
2. Chat Agent
3. RAG Agent
4. Web Agent
5. Tool Agent
6. Vision Agent

```text
User Query
     │
     ▼
  Planner
     │
     ├──► Chat
     │
     ├──► RAG
     │
     ├──► Web
     │
     ├──► Tool
     │
     └──► Vision
```

---

## 🔌 MCP-style Tool Architecture

The project uses a client/server pattern for connecting agents with external capabilities.

```text
LangGraph
    │
    ▼
MCP Client
    │
    ▼
MCP Server
    │
    ├──► Web Search
    ├──► RAG / Document Service
    ├──► Tool Service
    └──► Vision Service
```

---

## 📄 Document RAG

The Document RAG pipeline allows users to upload PDF documents and ask questions about their contents.

### Workflow

```text
PDF Upload
    │
    ▼
Text Extraction
    │
    ▼
Text Chunking
    │
    ▼
Embeddings
    │
    ▼
FAISS Vector Database
    │
    ▼
Similarity Search
    │
    ▼
Top-K Relevant Chunks
    │
    ▼
LLM
    │
    ▼
Grounded Answer
```

### Technologies

- PyPDF
- LangChain Text Splitters
- Hugging Face Embeddings
- FAISS
- Ollama

The RAG system is designed to answer questions using retrieved document context rather than relying only on general LLM knowledge.

---

## 🔎 Web Search Agent

The Web Agent provides external information retrieval.

### Workflow

```text
User Query
    │
    ▼
Planner
    │
    ▼
Web Agent
    │
    ▼
DuckDuckGo Search
    │
    ▼
Search Results
    │
    ▼
Ollama LLM
    │
    ▼
Final Answer
```

---

## 🧮 Tool Agent

The Tool Agent handles calculation-related requests.

### Example

```text
User: Calculate 25 * 4
        │
        ▼
      Planner
        │
        ▼
    Tool Agent
        │
        ▼
    Calculation
        │
        ▼
       Result
```

---

## 🎤 Voice Assistant

The system also supports voice interaction.

### Voice Pipeline

```text
Microphone
    │
    ▼
Audio Recording
    │
    ▼
FFmpeg / Pydub
    │
    ▼
WAV Audio
    │
    ▼
Speech Recognition
    │
    ▼
Text Query
    │
    ▼
LangGraph
    │
    ▼
Agent
    │
    ▼
AI Response
```

---

## Local LLM

The project uses Ollama for local LLM inference.

This allows the application to run LLM inference locally without requiring every interaction to be sent to a cloud API.

The project has been tested with:

- **Phi-3** — lightweight local model
- **Llama 3** — larger local model

---

## Project Objective

The main objective of this project is to develop a modular agentic AI assistant that demonstrates the integration of:

**LangChain + LangGraph + MCP-style architecture + RAG + Local LLMs**

The project focuses on separating:

- User interaction
- Agent planning
- Agent orchestration
- Retrieval
- Tool execution
- External services
- LLM response generation

---

## 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

1. Building applications with LangChain
2. Designing workflows with LangGraph
3. Implementing Retrieval-Augmented Generation
4. Building vector-based document retrieval
5. Connecting agents with tools
6. Designing client/server tool architectures
7. Integrating local LLMs with Ollama
8. Building voice-enabled AI applications
9. Creating modular multi-agent systems
10. Developing AI applications with Streamlit

---

## Future Improvements

- Automatic MCP tool registry
- More MCP tools
- Improved planner-based routing
- Persistent conversation memory

---

## ⭐ Project Highlights

### Core Architecture

```text
LangChain
     +
LangGraph
     +
MCP-style Client/Server
     +
RAG
     +
Local LLM
     +
Voice
     +
Web Search
     +
Tools
```

---

## Author

Developed as an AI/ML engineering project focused on:

- Generative AI
- Agentic AI
- Large Language Models
- RAG
- Computer Vision
- Multi-Agent Systems

---

## Keywords

LangChain, LangGraph, MCP, Agentic AI, Multi-Agent AI, RAG, LLM, Ollama, FAISS, Streamlit, Generative AI, Voice AI, Web Search, AI Agents
