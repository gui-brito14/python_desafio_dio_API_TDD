from fastapi import APIRouter, HTTPException, Path, Query
from typing import List
from app.crud import product as crud
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut

router = APIRouter()

@router.post("/", response_model=ProductOut, status_code=201)
async def create_product(product: ProductCreate):
    try:
        return crud.create_product(product)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/", response_model=List[ProductOut])
async def list_products(skip: int = 0, limit: int = 10):
    return crud.get_products(skip=skip, limit=limit)

@router.get("/{id}", response_model=ProductOut)
async def get_product(id: str = Path(..., alias='_id')):
    product = crud.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{id}", response_model=ProductOut)
async def update_product(id: str, product: ProductUpdate):
    updated_product = crud.update_product(id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{id}", status_code=204)
async def delete_product(id: str):
    if not crud.delete_product(id):
        raise HTTPException(status_code=404, detail="Product not found")
