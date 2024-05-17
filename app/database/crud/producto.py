from sqlalchemy.orm import Session
from routers.schemas.producto import Producto, ProductoBase
from database.models.models import Producto as model

def getById(db : Session, producto_id: int):
    return db.query(model).get(producto_id)

def get(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def create(db: Session, producto: ProductoBase):
    db_producto = model(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def delete(db : Session, producto_id: int):
    rows_deleted = db.query(model).where(model.id == producto_id).delete('auto')
    db.commit()
    return rows_deleted > 0

def update(db: Session, producto: Producto):
    db_producto = db.query(model).filter(model.id == producto.id).first()
    if db_producto:
        db_producto.nombre = producto.nombre or producto.nombre
        db_producto.precio_venta = producto.precio_venta or producto.precio_venta
        db_producto.precio_compra = producto.precio_compra or producto.precio_compra
    db.commit()
    return producto
