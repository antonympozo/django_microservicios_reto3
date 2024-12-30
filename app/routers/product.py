from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.schemas import ProductCreate, ProductResponse
from app.services.product import ProductService
from app.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}},
)

product_service = ProductService()

@router.post("/", response_model=ProductResponse, 
    summary="Create a new product",
    description="Create a new product with all the information: name, price, quantity and category")
async def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new product with the following information:

    - **name**: Name of the product
    - **price**: Price of the product (must be greater than 0)
    - **quantity**: Available quantity (must be greater than or equal to 0)
    - **category**: Product category
    """
    return product_service.create_product(db, product)

@router.get("/", response_model=List[ProductResponse],
    summary="Get all products",
    description="Get a list of all products with pagination support")
async def read_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get all products with pagination:

    - **skip**: Number of products to skip (default: 0)
    - **limit**: Maximum number of products to return (default: 100)
    """
    products = product_service.get_products(db, skip=skip, limit=limit)
    return products

@router.get("/{product_id}", response_model=ProductResponse,
    summary="Get a specific product",
    description="Get a specific product by its ID")
async def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Get a specific product by its ID:

    - **product_id**: ID of the product to retrieve
    """
    return product_service.get_product(db, product_id)

@router.put("/{product_id}", response_model=ProductResponse,
    summary="Update a product",
    description="Update a product's information by its ID")
async def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    """
    Update a product with the following information:

    - **product_id**: ID of the product to update
    - **name**: New name of the product
    - **price**: New price of the product
    - **quantity**: New quantity
    - **category**: New category
    """
    return product_service.update_product(db, product_id, product)

@router.delete("/{product_id}",
    summary="Delete a product",
    description="Delete a product by its ID")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product by its ID:

    - **product_id**: ID of the product to delete
    """
    product_service.delete_product(db, product_id)
    return {"message": "Product deleted successfully"}
