from app.repositories.cart import CartRepository
from app.models.models import CartItem
from sqlalchemy.orm import Session
from fastapi import HTTPException

class CartService:
    def __init__(self):
        self.repository = CartRepository(CartItem)

    def create_cart_item(self, db: Session, cart_item_data):
        return self.repository.create(db, cart_item_data)

    def get_cart_items(self, db: Session, cart_id: str):
        return self.repository.get_by_cart_id(db, cart_id)

    def update_cart_item(self, db: Session, item_id: int, cart_item_data):
        cart_item = self.repository.get_by_id(db, item_id)
        if not cart_item:
            raise HTTPException(status_code=404, detail="Cart item not found")
        return self.repository.update(db, cart_item, cart_item_data)

    def delete_cart_item(self, db: Session, item_id: int):
        cart_item = self.repository.get_by_id(db, item_id)
        if not cart_item:
            raise HTTPException(status_code=404, detail="Cart item not found")
        return self.repository.delete(db, item_id)