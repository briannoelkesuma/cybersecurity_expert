# backend/database/milvus_client.py

from pymilvus import connections, utility, FieldSchema, CollectionSchema, DataType, Collection
import config # Import your central configuration

def connect_and_setup():
    """
    Connects to the Milvus server and ensures the collection exists with the correct schema.
    This function is designed to be run at application startup.
    """
    try:
        # 1. Connect to Milvus
        # The 'default' alias is used by subsequent Milvus operations.
        connections.connect("default", uri=config.MILVUS_URI)
        print("✅ Successfully connected to Milvus.")

        collection_name = config.MILVUS_COLLECTION_NAME

        # 2. Check if the collection already exists
        if utility.has_collection(collection_name):
            print(f"Collection '{collection_name}' already exists.")
            # Optional: Load collection into memory for searching
            Collection(collection_name).load()
            return

        # 3. Define the schema if the collection doesn't exist
        print(f"Collection '{collection_name}' does not exist. Creating now...")
        fields = [
            FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, max_length=36),
            FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=config.EMBEDDING_DIMENSION),
            FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
            FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=512),
            FieldSchema(name="url", dtype=DataType.VARCHAR, max_length=512),
            FieldSchema(name="summary", dtype=DataType.VARCHAR, max_length=2048)
        ]
        schema = CollectionSchema(fields, description="Cybersecurity knowledge base")

        # 4. Create the collection
        collection = Collection(name=collection_name, schema=schema)
        print(f"✅ Collection '{collection_name}' created successfully.")

        # 5. Create an index for the vector field for efficient searching
        index_params = {
            "metric_type": "L2",  # L2 is a common distance metric
            "index_type": "IVF_FLAT",
            "params": {"nlist": 128}
        }
        collection.create_index(field_name="vector", index_params=index_params)
        print(f"✅ Index created for 'vector' field.")

        # Load the collection into memory
        collection.load()
        print(f"✅ Collection '{collection_name}' loaded into memory.")

    except Exception as e:
        print(f"❌ An error occurred during Milvus setup: {e}")
        # Depending on your needs, you might want to exit the application if the DB isn't available
        raise

# --- You will add other functions like insert() and search() here later ---

def insert(vector: list, text: str, title: str, url: str, summary: str):
    """Placeholder for the insert function."""
    from uuid import uuid4
    collection = Collection(config.MILVUS_COLLECTION_NAME)
    doc_id = str(uuid4())
    entities = [
        [doc_id], [vector], [text], [title], [url], [summary]
    ]
    collection.insert(entities)
    collection.flush() # Ensure data is written to disk
    return doc_id

def search(query_vector: list, top_k=5):
    """Placeholder for the search function."""
    collection = Collection(config.MILVUS_COLLECTION_NAME)
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = collection.search(
        data=[query_vector],
        anns_field="vector",
        param=search_params,
        limit=top_k,
        output_fields=["summary", "title", "url"]
    )
    # The search result is complex, we simplify it here
    hits = []
    for hit in results[0]:
        hits.append({
            "score": hit.distance,
            "entity": {
                "summary": hit.entity.get('summary'),
                "title": hit.entity.get('title'),
                "url": hit.entity.get('url'),
            }
        })
    return hits