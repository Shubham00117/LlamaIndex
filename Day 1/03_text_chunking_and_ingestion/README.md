# Topic 3: Text Chunking & Ingestion

## Overview
After loading documents, they must be split into smaller chunks (Nodes) before embedding. Choosing the right chunking strategy directly impacts retrieval quality.

## Key Concepts

| Subtopic | Description |
|----------|-------------|
| SentenceSplitter & TokenTextSplitter (#10) | Two main splitters — sentence-boundary vs strict token-count |
| Ingestion Pipeline (#11) | Chains transformations into a reusable pipeline with incremental indexing |
| Transformations (#12) | Composable steps: splitters, metadata extractors, embedding models |
| Node Parsers (#13) | Specialized parsers: Hierarchical, Markdown, JSON, Code |

## Chunk Size Guidelines
- **128–256 tokens**: Precise retrieval for fact-heavy Q&A (medical, legal)
- **512 tokens**: Good default for most RAG use cases
- **1024+ tokens**: Summarization, broad context tasks
