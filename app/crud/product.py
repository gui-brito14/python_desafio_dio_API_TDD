from pymongo import MongoClient
from bson import ObjectId
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from typing import List, Optional
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['product_db']
collection = db['products']

def create_product(product: ProductCreate) -> Product:
    new_product = product.dict()
    new_product['created_at'] = new_product['updated_at'] = datetime.utcnow()
    result = collection.insert_one(new_product)
    return Product(**new_product, id=str(result.inserted_id))

def get_product(product_id: str) -> Optional[Product]:
    product = collection.find_one({'_id': ObjectId(product_id)})
    if product:
        return Product(**product)
    return None

def get_products(skip: int = 0, limit: int = 10) -> List[Product]:
    products = collection.find().skip(skip).limit(limit)
    return [Product(**prod) for prod in products]

def update_product(product_id: str, product: ProductUpdate) -> Optional[Product]:
    update_data = {k: v for k, v in product.dict().items() if v is not None}
    update_data['updated_at'] = datetime.utcnow()
    result = collection.update_one({'_id': ObjectId(product_id)}, {'$set': update_data})
    if result.matched_count:
        return get_product(product_id)
    return None

def delete_product(product_id: str) -> bool:
    result = collection.delete_one({'_id': ObjectId(product_id)})
    return result.deleted_count > 0
