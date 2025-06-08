#!/bin/bash
# Start the FastAPI server with Uvicorn
uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --reload \
    --log-level info
