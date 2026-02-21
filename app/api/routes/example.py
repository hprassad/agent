"""Example API endpoints."""
from fastapi import APIRouter, HTTPException

from app.models.schemas import Item, ItemCreate

router = APIRouter()

items_store: list[Item] = []


@router.get("/items", response_model=list[Item])
def list_items():
    """List all items."""
    return items_store


@router.post("/items", response_model=Item)
def create_item(item: ItemCreate):
    """Create a new item."""
    new_item = Item(
        id=len(items_store) + 1,
        name=item.name,
        description=item.description,
    )
    items_store.append(new_item)
    return new_item


@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Get item by id."""
    for item in items_store:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
