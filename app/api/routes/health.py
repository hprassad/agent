"""Health check endpoints."""
from fastapi import APIRouter

router = APIRouter()


@router.get("")
def health():
    """Simple health check."""
    return {"status": "ok"}


@router.get("/live")
def liveness():
    """Liveness probe."""
    return {"live": True}
