from app.repositories.base import BaseRepository
from app.models.models import Product
from app.schemas.schemas import ProductCreate, ProductBase

class ProductRepository(BaseRepository[Product, ProductCreate, ProductBase]):
    pass

# app/repositories/cart.py
from app.repositories.base import BaseRepository
from app.models.models import CartItem
from app.schemas.schemas import CartItemCreate, CartItemBase
from sqlalchemy.orm import Session

class CartRepository(BaseRepository[CartItem, CartItemCreate, CartItemBase]):
    def get_by_cart_id(self, db: Session, cart_id: str):
        return db.query(self.model).filter(self.model.cart_id == cart_id).all()
