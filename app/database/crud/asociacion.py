from sqlalchemy.orm import Session
from routers.schemas.asociacion import Asociacion, AsociacionCreate
from database.models.models import Asociacion as model


def obtenerAsociacionPorId(db : Session, asociacion_id: int):
    return db.query(model).get(asociacion_id)

def obtenerAsociaciones(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def crearAsociacion(db: Session, asociacion: AsociacionCreate):
    db_asociacion = model(**asociacion.model_dump())
    db.add(db_asociacion)
    db.commit()
    db.refresh(db_asociacion)
    return db_asociacion

def eliminarAsociacionPorId(db : Session, asociacion_id: int):
    return db.delete(model.Usuario).filter(model.Usuario.id == asociacion_id)

def actualizarAsociacion(db: Session, asociacion: Asociacion):
    db_asociacion = db.query(model).filter(model.id == asociacion.id).first()
    if db_asociacion:
        db_asociacion.rol = asociacion.rol
        db_asociacion.organizacion_id = asociacion.organizacion_id
        db_asociacion.usuario_id = asociacion.usuario_id
    return asociacion