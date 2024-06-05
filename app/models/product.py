from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    id: Optional[str] = Field(None, alias='_id')
    name: str
    quantity: int
    price: float
    status: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
