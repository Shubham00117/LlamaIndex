# Topic 9: Re-ranking

## Overview
Re-ranking is a **post-retrieval** step that re-orders retrieved nodes by relevance. It dramatically improves answer quality in production by filtering out low-relevance noise.

## Methods
| Method | Description |
|--------|-------------|
| Cohere Reranker | Cloud API, best quality |
| BGE Reranker | Local, free, good quality |
| LLM-based Reranking | Use your LLM to score relevance |
| MMR (Maximum Marginal Relevance) | Ensures diversity in results |
