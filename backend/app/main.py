# backend/app/main.py
from fastapi import FastAPI
from . import api_router
from database import milvus_client

app = FastAPI(
    title="AI-Powered Security Knowledge Platform API",
    description="API for querying cybersecurity knowledge and analyzing trends.",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    """
    Actions to perform on application startup.
    - Connect to Milvus and create the collection if it doesn't exist.
    """
    print("Application starting up...")
    milvus_client.connect_and_setup()
    print("Milvus connection established and collection is ready.")

app.include_router(api_router.router, prefix="/api/v1")

@app.get("/", tags=["Health Check"])
def read_root():
    """A simple health check endpoint."""
    return {"status": "ok", "message": "Welcome to the API!"}