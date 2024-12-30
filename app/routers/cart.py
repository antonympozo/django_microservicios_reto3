from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.schemas import CartItemCreate, CartItemResponse
from app.services.cart import CartService
from app.database import get_db

router = APIRouter(
    prefix="/cart",
    tags=["Shopping Cart"],
    responses={404: {"description": "Not found"}},
)

cart_service = CartService()

@router.post("/items/", response_model=CartItemResponse,
    summary="Add item to cart",
    description="Add a new item to the shopping cart")
async def create_cart_item(
    cart_item: CartItemCreate,
    db: Session = Depends(get_db)
):
    """
    Add a new item to the shopping cart:

    - **product_id**: ID of the product to add
    - **quantity**: Quantity to add (must be greater than 0)
    - **cart_id**: ID of the shopping cart
    """
    return cart_service.create_cart_item(db, cart_item)

@router.get("/{cart_id}/items/", response_model=List[CartItemResponse],
    summary="Get cart items",
    description="Get all items in a specific shopping cart")
async def read_cart_items(cart_id: str, db: Session = Depends(get_db)):
    """
    Get all items in a specific shopping cart:

    - **cart_id**: ID of the shopping cart to retrieve items from
    """
    return cart_service.get_cart_items(db, cart_id)

@router.put("/items/{item_id}", response_model=CartItemResponse,
    summary="Update cart item",
    description="Update a specific item in the shopping cart")
async def update_cart_item(
    item_id: int,
    cart_item: CartItemCreate,
    db: Session = Depends(get_db)
):
    """
    Update a specific item in the shopping cart:

    - **item_id**: ID of the cart item to update
    - **product_id**: New product ID
    - **quantity**: New quantity
    - **cart_id**: Cart ID
    """
    return cart_service.update_cart_item(db, item_id, cart_item)

@router.delete("/items/{item_id}",
    summary="Delete cart item",
    description="Delete a specific item from the shopping cart")
async def delete_cart_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific item from the shopping cart:

    - **item_id**: ID of the cart item to delete
    """
    cart_service.delete_cart_item(db, item_id)
    return {"message": "Cart item deleted successfully"}
