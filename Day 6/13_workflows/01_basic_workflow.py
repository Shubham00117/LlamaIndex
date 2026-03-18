"""
Topic 13 — Workflows
Subtopics #75-83: Event-driven Workflows

Workflows are the MOST important feature for production LlamaIndex apps.
They provide an event-driven architecture for complex pipelines.

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.workflow import (
    Workflow,
    step,
    Event,
    StartEvent,
    StopEvent,
    Context,
)


# ─── Define custom events ───
class QueryEvent(Event):
    """Event carrying a user query."""
    query: str


class RetrievalEvent(Event):
    """Event carrying retrieved nodes."""
    nodes: list
    query: str


# ─── Define the workflow ───
class RAGWorkflow(Workflow):
    """Simple RAG workflow: receive query → retrieve → generate → respond."""
    
    @step
    async def receive_query(self, ev: StartEvent) -> QueryEvent:
        """Step 1: Receive and validate the user query."""
        query = ev.get("query", "")
        print(f"📝 Received query: {query}")
        return QueryEvent(query=query)
    
    @step
    async def retrieve(self, ctx: Context, ev: QueryEvent) -> RetrievalEvent:
        """Step 2: Retrieve relevant nodes from the index."""
        # In production, you'd use an actual retriever here
        nodes = [f"Relevant content for: {ev.query}"]
        
        # Store in context for later steps
        await ctx.set("query", ev.query)
        
        print(f"🔍 Retrieved {len(nodes)} nodes")
        return RetrievalEvent(nodes=nodes, query=ev.query)
    
    @step
    async def generate(self, ctx: Context, ev: RetrievalEvent) -> StopEvent:
        """Step 3: Generate response using LLM + retrieved context."""
        # In production, you'd call the LLM here
        response = f"Answer based on {len(ev.nodes)} sources for: {ev.query}"
        
        print(f"✅ Generated response")
        return StopEvent(result=response)


async def run_workflow():
    """Run the RAG workflow."""
    
    workflow = RAGWorkflow(timeout=30)
    result = await workflow.run(query="What is LlamaIndex?")
    
    print(f"\n📋 Final result: {result}")
    return result


def show_workflow_patterns():
    """Show advanced workflow patterns."""
    
    branching = '''
# Conditional branching
@step
async def classify(self, ev: StartEvent) -> QueryEvent | ErrorEvent:
    if is_valid(ev.query):
        return QueryEvent(query=ev.query)
    else:
        return ErrorEvent(error="Invalid query")
'''
    
    parallel = '''
# Concurrent step execution
@step
async def parallel_retrieve(self, ev: QueryEvent) -> RetrievalEvent:
    import asyncio
    
    # Run multiple retrievals in parallel
    results = await asyncio.gather(
        retriever1.aretrieve(ev.query),
        retriever2.aretrieve(ev.query),
    )
    
    all_nodes = results[0] + results[1]
    return RetrievalEvent(nodes=all_nodes, query=ev.query)
'''
    
    human_loop = '''
# Human-in-the-loop
class HumanApprovalEvent(Event):
    content: str
    approved: bool = False

@step
async def wait_for_approval(self, ev: HumanApprovalEvent) -> StopEvent:
    if ev.approved:
        return StopEvent(result="Approved and processed!")
    else:
        return StopEvent(result="Rejected by human review.")
'''
    
    print("=" * 60)
    print("  Workflow Patterns")
    print("=" * 60)
    print("\n🔀 Conditional Branching:")
    print(branching)
    print("⚡ Parallel Execution:")
    print(parallel)
    print("👤 Human-in-the-Loop:")
    print(human_loop)


if __name__ == "__main__":
    import asyncio
    
    show_workflow_patterns()
    
    print("\n" + "=" * 60)
    print("  Running RAG Workflow")
    print("=" * 60)
    asyncio.run(run_workflow())
