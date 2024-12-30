# app/main.py
from fastapi import FastAPI
from app.routers import product, cart
from app.database import engine, Base

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI(
    title="Store API",
    description="API para gestionar productos y carritos de compra",
    version="2.0.0",
    openapi_tags=[
        {
            "name": "Products",
            "description": "Operaciones con productos: crear, leer, actualizar y eliminar",
        },
        {
            "name": "Shopping Cart",
            "description": "Operaciones con el carrito de compras: añadir, actualizar y eliminar items",
        },
    ],
)

# Ruta raíz
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Bienvenido a la API de la tienda",
        "endpoints": {
            "documentación": "/docs",
            "documentación alternativa": "/redoc",
            "productos": "/products/",
            "carrito": "/cart/items/"
        },
        "versión": "2.0.0"
    }

# Incluir los routers
app.include_router(product.router)
app.include_router(cart.router)

# Iniciar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)