# 🤖 AI Chatbot using LangGraph + RAG

An AI-powered chatbot built using **LangGraph**, **LangChain**, and **Streamlit** with support for **RAG (Retrieval-Augmented Generation)**, real-time streaming responses, conversational memory, and observability using **LangSmith**.

The project is designed to deliver accurate, context-aware responses by combining LLM reasoning with external knowledge retrieval through a vector database.

---

## 🚀 Features

- 🔍 **RAG Pipeline**
  - Retrieves relevant context from a vector database before generating responses.
  - Improves factual accuracy and reduces hallucinations.

- 🧠 **Conversational Memory**
  - Maintains chat history and contextual understanding across interactions.

- ⚡ **Streaming Responses**
  - Real-time token streaming for smoother and interactive conversations.

- 🔄 **LangGraph Workflows**
  - Multi-step agent workflows with controlled execution flow.
  - Better orchestration compared to standard chains.

- 📊 **LangSmith Integration**
  - End-to-end tracing, debugging, monitoring, and observability.

- 🌐 **Streamlit Frontend**
  - Clean and interactive web interface for chatting with the AI assistant.

- 💾 **Memory Backup Support**
  - Stores conversation memory/state for continuity and recovery.

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **LangGraph**
- **LangSmith**
- **Streamlit**
- **Vector Database** (FAISS / ChromaDB)
- **OpenAI / LLM APIs**

---

⚙️ Installation
1️⃣ Clone the repository
git clone <your-repo-url>
cd <project-folder>
2️⃣ Create virtual environment
python -m venv venv
3️⃣ Activate virtual environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
4️⃣ Install dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory and add your API keys:

OPENAI_API_KEY=your_api_key

LANGCHAIN_API_KEY=your_langsmith_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=your_project_name

▶️ Run the Application
streamlit run frontend.py

🧠 How It Works
User sends a query through the Streamlit UI.
LangGraph manages the execution workflow.
Relevant documents are retrieved from the vector database.
Retrieved context is passed to the LLM using RAG.
Response is streamed back to the frontend in real time.
LangSmith traces the complete execution flow for debugging and monitoring.

📸 Core Concepts Used
Retrieval-Augmented Generation (RAG)
Agentic Workflow Orchestration
Vector Embeddings & Semantic Search
Conversational AI
LLM Streaming
AI Observability & Tracing

🔮 Future Improvements
Multi-agent support
Voice interaction
Authentication system
Deployment on cloud platforms
Advanced memory management
File upload and document chat support
📌 Author

Developed by Chetan Mittal
