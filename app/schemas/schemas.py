from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., example="Laptop", description="Nombre del producto")
    price: float = Field(..., gt=0, example=999.99, description="Precio del producto")
    quantity: int = Field(..., ge=0, example=10, description="Cantidad disponible")
    category: str = Field(..., example="Electronics", description="Categoría del producto")

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CartItemBase(BaseModel):
    product_id: int = Field(..., example=1, description="ID del producto")
    quantity: int = Field(..., gt=0, example=2, description="Cantidad a comprar")
    cart_id: str = Field(..., example="cart123", description="ID del carrito")

class CartItemCreate(CartItemBase):
    pass

class CartItemResponse(CartItemBase):
    id: int

    class Config:
        orm_mode = True
