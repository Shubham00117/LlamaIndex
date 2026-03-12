"""
Topic 5 — Vector Stores
Subtopics #23-26: Milvus, MongoDB Atlas, PGVector, Redis

These four stores cover enterprise-scale, relational, and
ultra-low latency use cases.

⚠️ Each requires its own pip install and running service.
"""


def all_stores_reference():
    """Reference for Milvus, MongoDB Atlas, PGVector, Redis."""
    
    stores = {
        "Milvus (billion-scale)": '''
pip install llama-index-vector-stores-milvus

from llama_index.vector_stores.milvus import MilvusVectorStore

vector_store = MilvusVectorStore(
    uri="http://localhost:19530",
    collection_name="my_collection",
    dim=1536   # Must match your embedding dimension
)''',
        "MongoDB Atlas Vector Search": '''
pip install llama-index-vector-stores-mongodb

from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient

client = MongoClient("mongodb+srv://...")
vector_store = MongoDBAtlasVectorSearch(
    mongodb_client=client,
    db_name="my_db",
    collection_name="embeddings",
    index_name="vector_index"
)''',
        "PGVector (Postgres + vector)": '''
pip install llama-index-vector-stores-postgres

from llama_index.vector_stores.postgres import PGVectorStore

vector_store = PGVectorStore.from_params(
    host="localhost", port=5432,
    database="mydb", user="postgres", password="...",
    table_name="embeddings", embed_dim=1536
)''',
        "Redis Vector Store": '''
pip install llama-index-vector-stores-redis

from llama_index.vector_stores.redis import RedisVectorStore
import redis

redis_client = redis.Redis(host="localhost", port=6379)
vector_store = RedisVectorStore(
    redis_client=redis_client,
    index_name="my_index",
    index_prefix="llama"
)''',
    }
    
    print("=" * 60)
    print("  Additional Vector Store Integrations")
    print("=" * 60)
    
    for name, code in stores.items():
        print(f"\n{'─' * 50}")
        print(f"  🗄️  {name}")
        print(f"{'─' * 50}")
        print(code)
    
    print("\n💡 Tips:")
    print("  • PGVector → Use if you already have Postgres")
    print("  • Redis    → Use when latency must be <5ms")
    print("  • Milvus   → Use for billion+ vector scale")
    print("  • MongoDB  → Use if you already use MongoDB")


if __name__ == "__main__":
    all_stores_reference()
