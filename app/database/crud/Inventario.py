from sqlalchemy.orm import Session
from routers.schemas.inventario import Inventario, InventarioBase
from database.models.models import Inventario as model


def getById(db : Session, inventario_id: int):
    return db.query(model).get(inventario_id)

def get(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def create(db: Session, inventario: InventarioBase):
    db_inventario = model(**inventario.model_dump())
    db.add(db_inventario)
    db.commit()
    db.refresh(db_inventario)
    return db_inventario

def delete(db : Session, inventario_id: int):
    rows_deleted = db.query(model).where(model.id == inventario_id).delete('auto')
    db.commit()
    return rows_deleted > 0

def update(db: Session, inventario: Inventario):
    db_inventario = db.query(model).filter(model.id == inventario.id).first()
    if db_inventario:
        db_inventario.nombre = inventario.nombre or db_inventario.nombre
        db_inventario.ubicacion = inventario.ubicacion or db_inventario.ubicacion
        db_inventario.organizacion_id = inventario.organizacion_id or db_inventario.organizacion_id
    db.commit()
    return inventario