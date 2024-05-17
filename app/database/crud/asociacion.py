from sqlalchemy.orm import Session
from routers.schemas.asociacion import Asociacion, AsociacionCreate
from database.models.models import Asociacion as model


def getById(db : Session, asociacion_id: int):
    return db.query(model).get(asociacion_id)

def get(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def create(db: Session, asociacion: AsociacionCreate):
    db_asociacion = model(**asociacion.model_dump())
    db.add(db_asociacion)
    db.commit()
    db.refresh(db_asociacion)
    return db_asociacion

def delete(db : Session, asociacion_id: int):
    rows_deleted = db.query(model).where(model.Usuario.id == asociacion_id).delete('auto')
    db.commit()
    return rows_deleted > 0

def update(db: Session, asociacion: Asociacion):
    db_asociacion = db.query(model).filter(model.id == asociacion.id).first()
    if db_asociacion:
        db_asociacion.rol = asociacion.rol or db_asociacion.rol
        db_asociacion.organizacion_id = asociacion.organizacion_id or db_asociacion.organizacion_id
        db_asociacion.usuario_id = asociacion.usuario_id or db_asociacion.usuario_id
    db.commit()
    return asociacion