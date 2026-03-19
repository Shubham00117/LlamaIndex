"""
Topic 16 — Evaluation
Subtopics #91-98: Faithfulness, Relevancy, Retrieval, Ragas, Batch Eval

Evaluate RAG pipeline quality with automated metrics.

⚠️ Requires: pip install llama-index-core llama-index-llms-openai
"""


def evaluation_examples():
    """Show all evaluation patterns."""
    
    faithfulness = '''
# Faithfulness — is the answer grounded in the context?
from llama_index.core.evaluation import FaithfulnessEvaluator

evaluator = FaithfulnessEvaluator()

# Evaluate a response
result = await evaluator.aevaluate_response(response=query_response)

print(f"Faithful: {result.passing}")   # True/False
print(f"Score: {result.score}")        # 0-1
print(f"Feedback: {result.feedback}")  # Explanation
'''
    
    relevancy = '''
# Relevancy — is the answer relevant to the question?
from llama_index.core.evaluation import RelevancyEvaluator

evaluator = RelevancyEvaluator()

result = await evaluator.aevaluate_response(
    query="What is RAG?",
    response=query_response,
)

print(f"Relevant: {result.passing}")
'''
    
    retrieval = '''
# Retrieval evaluation — how good is the retriever?
from llama_index.core.evaluation import RetrieverEvaluator

# Create evaluator
retriever_evaluator = RetrieverEvaluator.from_metric_names(
    metric_names=["mrr", "hit_rate"],
    retriever=index.as_retriever(similarity_top_k=5),
)

# Evaluate with test queries
eval_results = await retriever_evaluator.aevaluate_dataset(eval_dataset)

for result in eval_results:
    print(f"Query: {result.query}")
    print(f"MRR: {result.metric_vals_dict['mrr']:.4f}")
    print(f"Hit Rate: {result.metric_vals_dict['hit_rate']:.4f}")
'''
    
    batch = '''
# Batch evaluation pipeline
from llama_index.core.evaluation import BatchEvalRunner

runner = BatchEvalRunner(
    evaluators={
        "faithfulness": FaithfulnessEvaluator(),
        "relevancy": RelevancyEvaluator(),
    },
    workers=4,  # Parallel evaluation
)

eval_results = await runner.aevaluate_queries(
    query_engine=query_engine,
    queries=test_queries,
)

# Aggregate results
for metric, results in eval_results.items():
    scores = [r.score for r in results if r.score is not None]
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{metric}: {avg:.2%}")
'''
    
    print("=" * 60)
    print("  RAG Evaluation")
    print("=" * 60)
    print("\n📊 Faithfulness:")
    print(faithfulness)
    print("📊 Relevancy:")
    print(relevancy)
    print("📊 Retrieval Evaluation:")
    print(retrieval)
    print("📊 Batch Evaluation:")
    print(batch)


if __name__ == "__main__":
    evaluation_examples()
