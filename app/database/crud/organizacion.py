from sqlalchemy.orm import Session
from app.routers.schemas.organizacion import Organizacion, OrganizacionCreate
from app.database.models.models import Organizacion as model

def obtenerOrganizacionPorId(db : Session, organizacion_id: int):
    return db.query(model).get(organizacion_id)

def obtenerOrganizaciones(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def crearOrganizacion(db: Session, organizacion: OrganizacionCreate):
    db_organizacion = model(nombre = organizacion.nombre, nombreWS = organizacion.nombreWS)
    db.add(db_organizacion)
    db.commit()
    db.refresh(db_organizacion)
    return db_organizacion

def eliminarOrganizacionPorId(db : Session, organizacion_id: int):
    return db.delete(model).filter(model.id == organizacion_id)

def actualizarOrganizacion(db: Session, asociacion: Organizacion):
    db_organizacion = db.query(model).filter(model.id == asociacion.id).first()
    if db_organizacion:
        db_organizacion.nombre = asociacion.nombre
        db_organizacion.nombreWS = asociacion.nombreWS
    return asociacion
