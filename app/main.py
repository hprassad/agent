"""FastAPI application entry point."""
from fastapi import FastAPI

from app.config import settings
from app.api.routes import health, example

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(example.router, prefix="/api", tags=["example"])


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Welcome to the API", "docs": "/docs"}
