# cybersecurity_expert

## Health check on backend and starting backend server
```python
cd backend
python -m uvicorn app.main:app --reload
```

## Backend Technical Architecture
```python
backend/
├── .gitignore
├── requirements.txt
├── config.py # Central configuration for all settings.
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI application entry point and startup logic.
│ ├── api_router.py # Single router file for all API endpoints.
│ ├── schemas.py # Pydantic models for API request/response validation.
│ │
│ └── services/
│ ├── init.py
│ ├── rag_service.py # Core logic for answering queries (RAG).
│ ├── trends_service.py # Logic for trend/gap analysis and reports.
│ └── feedback_service.py # Logic for handling user feedback.
│
├── database/
│ ├── init.py
│ ├── milvus_client.py # Manages all interactions with Milvus Lite.
│ └── graph_client.py # Manages loading, saving, and querying the NetworkX graph.
│
├── docs/ # For all documentation related files.
│
├── ingestion/
│ ├── init.py
│ └── pipeline.py # The complete, orchestrated data ingestion process.
│
├── scripts/
│ └── run_ingestion.py # Executable script to trigger the ingestion pipeline.
│
└── data/ # (Ignored by Git) Stores persistent data files for milvus and graph
```
