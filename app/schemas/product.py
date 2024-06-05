from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    quantity: int
    price: float
    status: str

class ProductUpdate(BaseModel):
    name: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    status: Optional[str]
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProductOut(BaseModel):
    id: str
    name: str
    quantity: int
    price: float
    status: str
    created_at: datetime
    updated_at: datetime
