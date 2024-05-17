from sqlalchemy.orm import Session
from routers.schemas.organizacion import Organizacion, OrganizacionCreate
from database.models.models import Organizacion as model

def getById(db : Session, organizacion_id: int):
    return db.query(model).get(organizacion_id)

def get(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def create(db: Session, organizacion: OrganizacionCreate):
    db_organizacion = model(nombre = organizacion.nombre, nombreWS = organizacion.nombreWS)
    db.add(db_organizacion)
    db.commit()
    db.refresh(db_organizacion)
    return db_organizacion

def delete(db : Session, organizacion_id: int):
    rows_deleted = db.query(model).where(model.id == organizacion_id).delete('auto')
    db.commit()
    return rows_deleted > 0

def update(db: Session, organizacion: Organizacion):
    db_organizacion = db.query(model).filter(model.id == organizacion.id).first()
    if db_organizacion:
        db_organizacion.nombre = organizacion.nombre or organizacion.nombre
        db_organizacion.nombreWS = organizacion.nombreWS or organizacion.nombreWS
    db.commit()
    return organizacion
