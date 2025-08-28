# backend/config.py
import os

# --- Directory Setup ---
# This ensures paths are correct regardless of where you run the script from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MILVUS_DATA_DIR = os.path.join(DATA_DIR, "milvus_db") # Define the directory path
GRAPH_DATA_DIR = os.path.join(DATA_DIR, "graph_db")   # Define the directory path

os.makedirs(MILVUS_DATA_DIR, exist_ok=True)
os.makedirs(GRAPH_DATA_DIR, exist_ok=True)

# --- AI Models ---
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384
LLM_MODEL = "llama3"
OLLAMA_BASE_URL = "http://localhost:11434"

# --- Database Paths ---
# Now we construct the final file paths
MILVUS_URI = os.path.join(MILVUS_DATA_DIR, "milvus.db")
GRAPH_DB_PATH = os.path.join(GRAPH_DATA_DIR, "cyber_graph.gpickle")
MILVUS_COLLECTION_NAME = "cybersecurity_knowledge"