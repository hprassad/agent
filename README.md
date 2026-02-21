# FastAPI Backend

A simple FastAPI backend application.

## Structure

```
app/
  __init__.py
  main.py           # FastAPI app and router registration
  config.py         # Settings (pydantic-settings)
  api/
    routes/
      health.py     # /health, /health/live
      example.py    # /api/items
  models/
    schemas.py      # Pydantic request/response models
requirements.txt
README.md
```

## Setup & Run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- **API:** http://127.0.0.1:8000  
- **Docs:** http://127.0.0.1:8000/docs  

## Endpoints

| Method | Path           |
|--------|----------------|
| GET    | /              |
| GET    | /health        |
| GET    | /health/live   |
| GET    | /api/items     |
| POST   | /api/items     |
| GET    | /api/items/{id}|
