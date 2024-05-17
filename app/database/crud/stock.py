from sqlalchemy.orm import Session
from routers.schemas.stock import Stock, StockBase
from database.models.models import Stock as model

def getById(db : Session, id: int):
    return db.query(model).get(id)

def get(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def create(db: Session, stock: StockBase):
    db_stock = model(**stock.model_dump())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def delete(db : Session, id: int):
    rows_deleted = db.query(model).where(model.id == id).delete('auto')
    db.commit()
    return rows_deleted > 0

def update(db: Session, stock: Stock):
    db_stock = db.query(model).filter(model.id == stock.id).first()
    if db_stock:
        db_stock.cantidad = stock.cantidad or stock.cantidad
        db_stock.producto_id = stock.producto_id or stock.producto_id
        db_stock.inventario_id = stock.inventario_id or stock.inventario_id
    db.commit()
    return stock
