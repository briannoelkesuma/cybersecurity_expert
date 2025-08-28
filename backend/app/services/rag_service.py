# backend/app/services/rag_service.py
from database import milvus_client
# TODO: Import a helper to call Ollama

def answer_question(query: str) -> tuple[str, list]:
    """The main RAG pipeline for answering questions."""
    print(f"Answering question: {query}")
    # 1. Embed the user's query
    # TODO: query_vector = embedder.get_embedding(query)

    # 2. Search for relevant context in Milvus
    # TODO: search_results = milvus_client.search(query_vector)

    # 3. Construct a prompt with the context and query
    # TODO: prompt = _build_prompt(query, search_results)
    
    # 4. Call the LLM (Ollama) to generate an answer
    # TODO: answer = ollama_helper.generate(prompt)
    
    # 5. Extract sources from search_results
    # TODO: sources = [{"title": r.entity.get('title'), "url": r.entity.get('url')} for r in search_results]

    # --- Placeholder ---
    answer = f"This is a generated answer for: '{query}'."
    sources = [{"title": "Example Source", "url": "https://example.com"}]
    # --- End Placeholder ---

    return answer, sources