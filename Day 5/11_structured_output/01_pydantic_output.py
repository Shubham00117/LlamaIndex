"""
Topic 11 — Structured Output & Data Extraction
Subtopics #61-66: Pydantic Output, Schema Extraction, Text-to-SQL, CSV

Force LLMs to return structured data using Pydantic models.
Essential for building reliable data pipelines.

⚠️ Requires: pip install llama-index-core llama-index-llms-openai pydantic
"""

from pydantic import BaseModel, Field
from typing import List


# ─── Define your output schema ───
class MovieReview(BaseModel):
    """Structured output for a movie review."""
    title: str = Field(description="Name of the movie")
    rating: float = Field(description="Rating out of 10")
    sentiment: str = Field(description="positive, negative, or neutral")
    key_themes: List[str] = Field(description="Main themes in the movie")


def pydantic_output_example():
    """Get structured output from LLM using Pydantic."""
    
    code = '''
from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-4o")

# Use structured_predict to get Pydantic output
result = llm.structured_predict(
    MovieReview,
    prompt="Review the movie 'Inception'",
)

print(f"Title: {result.title}")
print(f"Rating: {result.rating}")
print(f"Sentiment: {result.sentiment}")
print(f"Themes: {result.key_themes}")
'''
    
    print("=" * 60)
    print("  Pydantic Structured Output")
    print("=" * 60)
    print(code)


def text_to_sql_example():
    """Natural language to SQL queries."""
    
    code = '''
from llama_index.core import SQLDatabase, VectorStoreIndex
from sqlalchemy import create_engine

# Connect to your database
engine = create_engine("sqlite:///my_database.db")
sql_database = SQLDatabase(engine, include_tables=["users", "orders"])

# Create a natural language SQL query engine
from llama_index.core.query_engine import NLSQLTableQueryEngine

query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=["users", "orders"],
)

# Query in natural language!
response = query_engine.query("How many orders were placed last month?")
print(response)  # Returns the answer from SQL results
'''
    
    print("\n📋 Text-to-SQL:")
    print(code)


def csv_querying_example():
    """Query CSV files with natural language."""
    
    code = '''
from llama_index.core.query_engine import PandasQueryEngine
import pandas as pd

# Load CSV
df = pd.read_csv("sales_data.csv")

# Create query engine over DataFrame
query_engine = PandasQueryEngine(df=df, verbose=True)

# Natural language query
response = query_engine.query("What was the total revenue in Q3?")
print(response)
'''
    
    print("\n📋 CSV Querying with Natural Language:")
    print(code)


if __name__ == "__main__":
    pydantic_output_example()
    text_to_sql_example()
    csv_querying_example()
