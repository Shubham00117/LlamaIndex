# 🦙 LlamaIndex — Complete Study Guide & Code Examples

> A comprehensive, production-grade LlamaIndex curriculum covering **19 topics** and **122 subtopics** — from setup to real-world deployment patterns.

---

## 📖 What's Inside

This repository contains two main resources:

### 📝 Study Notes (`Notes/`)
Beautiful, dark-themed HTML notes for each of the 19 topics — designed for visual learners. Open any `.html` file in a browser to study.

### 💻 Code Examples (`code_examples/`)
Self-contained, well-commented Python scripts organized by topic. Each file demonstrates a specific concept and can be run independently.

---

## 🗂️ Topics Covered

| # | Topic | Subtopics | Notes | Code |
|---|-------|-----------|-------|------|
| 1  | **Setup & Project Foundation** | Installation, Settings, Async basics | [Notes](./Notes/Topic%201%20Setup%20%26%20Project%20Foundation.html) | [Code](./code_examples/01_setup_and_project_foundation/) |
| 2  | **Document Loading & Parsing** | SimpleDirectoryReader, LlamaHub, LlamaParse, Custom loaders | [Notes](./Notes/Topic%202%20Document%20Loading%20%26%20Parsing.html) | [Code](./code_examples/02_document_loading_and_parsing/) |
| 3  | **Text Chunking & Ingestion** | SentenceSplitter, IngestionPipeline, Node parsers | [Notes](./Notes/Topic%203%20%20Text%20Chunking%20%26%20Ingestion.html) | [Code](./code_examples/03_text_chunking_and_ingestion/) |
| 4  | **Indexing** | VectorStoreIndex, Document management, Metadata filtering, PropertyGraphIndex | [Notes](./Notes/Topic%204%20Indexing.html) | [Code](./code_examples/04_indexing/) |
| 5  | **Vector Stores** | Pinecone, Qdrant, ChromaDB, Weaviate, Milvus, PGVector, Redis | [Notes](./Notes/Topic%205%20Vector%20Stores.html) | [Code](./code_examples/05_vector_stores/) |
| 6  | **Embeddings** | OpenAI, HuggingFace, Ollama, Custom models | [Notes](./Notes/Topic%206%20Embeddings.html) | [Code](./code_examples/06_embeddings/) |
| 7  | **LLM Integrations** | OpenAI, Anthropic, Azure, Groq, Ollama, Mistral, Bedrock, Gemini | [Notes](./Notes/Topic%207%20LLM%20Integrations.html) | [Code](./code_examples/07_llm_integrations/) |
| 8  | **Query Engine & Retrieval** | Response modes, Streaming, BM25, Hybrid search, Advanced retrievers | [Notes](./Notes/Topic%208%20Query%20Engine%20%26%20Retrieval.html) | [Code](./code_examples/08_query_engine_and_retrieval/) |
| 9  | **Re-ranking** | Cohere, BGE, LLM-based reranking, MMR diversity | [Notes](./Notes/Topic%209%20Re-ranking.html) | [Code](./code_examples/09_reranking/) |
| 10 | **Chat Engine** | Multi-turn chat, Modes, Memory, Chat stores | [Notes](./Notes/Topic%2010%20Chat%20Engine.html) | [Code](./code_examples/10_chat_engine/) |
| 11 | **Structured Output & Data Extraction** | Pydantic output, Text-to-SQL, CSV querying | [Notes](./Notes/Topic%2011%20Structured%20Output%20%26%20Data%20Extraction.html) | [Code](./code_examples/11_structured_output/) |
| 12 | **Agents** | ReAct, FunctionCalling, Custom tools, Multi-agent | [Notes](./Notes/Topic%2012%20%20Agents.html) | [Code](./code_examples/12_agents/) |
| 13 | **Workflows** | Event-driven architecture, State, Branching, Parallelism, HITL | [Notes](./Notes/Topic%2013%20Workflows.html) | [Code](./code_examples/13_workflows/) |
| 14 | **Prompt Engineering** | System prompts, Templates, Patterns | [Notes](./Notes/Topic%2014%20Prompt%20Engineering.html) | [Code](./code_examples/14_prompt_engineering/) |
| 15 | **Observability & Debugging** | Tracing, Arize Phoenix, Token counting, Callbacks | [Notes](./Notes/Topic%2015%20Observability.html) | [Code](./code_examples/15_observability/) |
| 16 | **Evaluation** | Faithfulness, Relevancy, Retrieval metrics, Ragas, Batch eval | [Notes](./Notes/Topic%2016%20Evaluation.html) | [Code](./code_examples/16_evaluation/) |
| 17 | **MCP (Model Context Protocol)** | MCP tools with agents, LlamaIndex as MCP server | [Notes](./Notes/Topic%2017%20MCP.html) | [Code](./code_examples/17_mcp/) |
| 18 | **Production Deployment** | FastAPI, Async, Caching, Docker, llama_deploy, CI/CD | [Notes](./Notes/Topic%2018%20Production%20Deployment.html) | [Code](./code_examples/18_production_deployment/) |
| 19 | **Real-World Project Patterns** | Enterprise Q&A, Multi-tenant RAG, Corrective RAG, Full-stack | [Notes](./Notes/Topic%2019%20Real-World%20Project%20Patterns.html) | [Code](./code_examples/19_real_world_patterns/) |

---

## 🚀 Quick Start

### 1. Install Core Packages

```bash
# Core — always required
pip install llama-index-core

# LLM provider (pick one)
pip install llama-index-llms-openai          # OpenAI
pip install llama-index-llms-ollama          # Ollama (local, free)

# Embedding model (pick one)
pip install llama-index-embeddings-openai    # OpenAI
pip install llama-index-embeddings-huggingface  # HuggingFace (local, free)
```

### 2. Set Your API Key

```bash
export OPENAI_API_KEY="your-key-here"
```

### 3. Run Any Example

```bash
cd code_examples/01_setup_and_project_foundation
python 01_installation.py
```

---

## 🏗️ Project Structure

```
LLama Index/
├── README.md                    ← You are here
├── Llama_Tpics.txt              ← Full topic list (122 subtopics)
├── Notes/                       ← 📝 Visual HTML study notes
│   ├── Topic 1 Setup & Project Foundation.html
│   ├── Topic 2 Document Loading & Parsing.html
│   ├── ...
│   └── Topic 19 Real-World Project Patterns.html
└── code_examples/               ← 💻 Runnable Python code
    ├── INDEX.md                 ← Master file listing with all topics
    ├── 01_setup_and_project_foundation/
    │   ├── README.md
    │   ├── 01_installation.py
    │   ├── 02_settings_configuration.py
    │   └── 03_async_basics.py
    ├── 02_document_loading_and_parsing/
    │   ├── README.md
    │   ├── 01_simple_directory_reader.py
    │   ├── ...
    │   └── 06_metadata_extraction.py
    ├── ...
    └── 19_real_world_patterns/
        ├── README.md
        └── 01_enterprise_qa.py
```

---

## 📊 Stats

| Metric | Count |
|--------|-------|
| Topics | 19 |
| Subtopics | 122 |
| Study Notes (HTML) | 19 |
| Code Example Files (.py) | 52 |
| README Files | 19 + 1 (root INDEX.md) |
| Total Files | 72+ |

---

## 🎯 Learning Path

**Beginner** — Start with Topics 1–4 to understand the RAG pipeline fundamentals.

**Intermediate** — Topics 5–10 cover production vector stores, retrieval strategies, and chat engines.

**Advanced** — Topics 11–16 dive into agents, workflows, evaluation, and observability.

**Production** — Topics 17–19 cover deployment, MCP, and real-world project architectures.

---

## 📌 Key Conventions

- **snake_case** for all file and variable names
- **PascalCase** for class names
- Every code file has a **docstring header** explaining the topic
- All scripts are **self-contained** — no cross-file dependencies
- Code requiring API keys clearly states `⚠️ Requires:` at the top

---

## 📚 Resources

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [LlamaHub (Data Connectors)](https://llamahub.ai/)
- [LlamaCloud (LlamaParse)](https://cloud.llamaindex.ai/)
- [LlamaIndex GitHub](https://github.com/run-llama/llama_index)

---

<p align="center"><em>Built for learning LlamaIndex from zero to production 🚀</em></p>
