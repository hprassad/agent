"""Pydantic schemas for request/response."""
from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    """Base item fields."""

    name: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """Schema for creating an item."""

    pass


class Item(ItemBase):
    """Item response schema."""

    id: int

    class Config:
        from_attributes = True
