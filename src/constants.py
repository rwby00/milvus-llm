import os

# Article dataset to ingest into our knowledge base
DATA_FP = "../cnn_dailymail/3.0.0/train-00000-of-00003.parquet"
NUM_ARTICLES = 100

# We use Milvus vector database for knowledge base
MILVUS_URL = os.environ.get("MILVUS_URL", "http://localhost:19530")
MILVUS_HOST = MILVUS_URL.split("//")[-1].split(":")[0]
MILVUS_PORT = MILVUS_URL.split(":")[-1]
MILVUS_COLLECTION_NAME = "articles_collection"
VECTOR_DIM = 1024
EMBEDDING_MODEL_NAME = "mixedbread-ai/mxbai-embed-large-v1"

# vLLM OpenAI Compatible Server for LLM
VLLM_HOST = os.environ.get("VLLM_HOST", "http://localhost:8000/v1")
LLM_NAME = "astronomer/Llama-3-8B-Instruct-GPTQ-4-Bit"
MAX_TOKENS = 1024
TOP_P = 0.95
TEMPERATURE = 0.01
PRESENCE_PENALTY = 1.03
