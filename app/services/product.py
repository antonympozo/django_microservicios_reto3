from app.repositories.product import ProductRepository
from app.models.models import Product
from sqlalchemy.orm import Session
from fastapi import HTTPException

class ProductService:
    def __init__(self):
        self.repository = ProductRepository(Product)

    def create_product(self, db: Session, product_data):
        return self.repository.create(db, product_data)

    def get_product(self, db: Session, product_id: int):
        product = self.repository.get_by_id(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def get_products(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.get_all(db, skip=skip, limit=limit)

    def update_product(self, db: Session, product_id: int, product_data):
        product = self.get_product(db, product_id)
        return self.repository.update(db, product, product_data)

    def delete_product(self, db: Session, product_id: int):
        product = self.get_product(db, product_id)
        return self.repository.delete(db, product_id)