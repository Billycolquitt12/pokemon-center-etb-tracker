"""
Hosting notes (example):
- Push project to GitHub
- Host on Render (Web Service)
- Build command: pip install -r requirements.txt
- Start command: uvicorn service.app:app --host 0.0.0.0 --port 10000
- Add environment variables for DB credentials:
  DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
"""

from fastapi import FastAPI
from service.routers.items_api import router as items_router

app = FastAPI(title="Pokemon ETB Tracker API")
app.include_router(items_router, prefix="/items", tags=["items"])