import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={"name": "Test Product", "quantity": 10, "price": 100.0, "status": "available"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Product"

def test_list_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_product():
    response = client.post("/products/", json={"name": "Test Product", "quantity": 10, "price": 100.0, "status": "available"})
    product_id = response.json()["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

def test_update_product():
    response = client.post("/products/", json={"name": "Test Product", "quantity": 10, "price": 100.0, "status": "available"})
    product_id = response.json()["id"]
    response = client.put(f"/products/{product_id}", json={"name": "Updated Product"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"

def test_delete_product():
    response = client.post("/products/", json={"name": "Test Product", "quantity": 10, "price": 100.0, "status": "available"})
    product_id = response.json()["id"]
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 204
