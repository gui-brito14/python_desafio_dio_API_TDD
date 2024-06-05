from fastapi import FastAPI
from app.api.product import router as product_router

app = FastAPI()

app.include_router(product_router, prefix="/products")

@app.on_event("startup")
async def startup():
    # Startup logic (like database connection) can be added here
    pass

@app.on_event("shutdown")
async def shutdown():
    # Shutdown logic can be added here
    pass
