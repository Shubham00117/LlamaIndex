# 8-Day LlamaIndex Mastery Roadmap

This roadmap is designed for a structured 8-day deep dive into LlamaIndex, covering everything from core indexing to advanced production patterns. Each day includes both conceptual HTML notes and working code examples.

## 📅 The 8-Day Schedule

| Day | Topics | Focus Areas | Status |
| :--- | :--- | :--- | :--- |
| **Day 1** | **Foundation: Setup, Loading, Chunking** | Topics 1-3. Setting up `llama-index-core`, data connectors (`SimpleDirectoryReader`, `LlamaHub`), and chunking strategies (`SentenceSplitter`). | ✅ Uploaded to Git / Present Locally |
| **Day 2** | **Indexing & Vector Stores** | Topics 4-5. `VectorStoreIndex`, Node Management, and persistence in DBs like Pinecone, Qdrant, Chroma, and PGVector. | ✅ Uploaded to Git / Present Locally |
| **Day 3** | **Embeddings & LLM Integrations** | Topics 6-7. OpenAI, Claude, Gemini, local HF models, and choosing the right embedding dimensions. | ✅ Uploaded to Git / Present Locally |
| **Day 4** | **Retrieval & Re-ranking** | Topics 8-9. Advanced retrieval (BM25, Hybrid), Streaming responses, and quality improvement via Rerankers (Cohere, BGE). | ✅ Uploaded to Git / Present Locally |
| **Day 5** | **Chat Engines & Data Extraction** | Topics 10-11. Building multi-turn chat interfaces with memory and extracting structured pydantic data from documents. | ✅ Uploaded to Git / Present Locally |
| **Day 6** | **Agents & Workflows** | Topics 12-13. Moving from passive pipelines to active Agents (ReAct) and event-driven Workflows for complex production logic. | ✅ Uploaded to Git / Present Locally |
| **Day 7** | **Prompts, Observability & Eval** | Topics 14-16. System prompts tuning, tracing pipelines with Arize Phoenix, and RAG evaluation (Faithfulness, Relevance). | 📂 Present Locally (To be uploaded) |
| **Day 8** | **MCP, Production & Real-World Patterns** | Topics 17-19. Connecting with Model Context Protocol (MCP), FastAPI deployment, Dockerization, and enterprise architectural patterns. | 📂 Present Locally (To be uploaded) |

---

## 📂 Directory Structure

The repository is organized into daily folders (`Day 1/` to `Day 8/`). Each folder contains:
1.  **HTML Notes**: Detailed conceptual guide for the topics.
2.  **Topic Folders**: Nested folders (e.g., `01_setup_and_project_foundation`) containing working Python scripts and their own READMEs.

---

## 🚀 Getting Started

1.  **Day 1** is your prerequisite—ensure your environment is ready and you understand how data becomes "Nodes".
2.  Follow the sequence chronologically to see how simple retrieval evolves into complex Agents and Workflows.
3.  Use the scripts in **Day 8** to wrap your logic into production-ready APIs.
