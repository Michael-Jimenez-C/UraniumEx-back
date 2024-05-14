from sqlalchemy.orm import Session
import DataSchemes as sch
import DataBaseManagement as model

import hashlib

def encodePassword(password: str) -> str | None:
    if not password:
        return None
    h = hashlib.new('sha512_256')
    h.update(bytes(password, encoding="utf-8"))
    return h.hexdigest()



def getUserbyId(db : Session, user_id: int):
    return db.query(model.Usuario).filter(model.Usuario.id == user_id).first()

def getUserByEmail(db : Session, email: int):
    return db.query(model.Usuario).filter(model.Usuario.email == email).first()

def getUsers(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model.Usuario).offset(skip).limit(limit).all()

def createUser(db: Session, user: sch.UsuarioCreate):
    db_user = model.Usuario(nombres = user.nombres, apellidos = user.apellidos, email=user.email, secret=encodePassword(user.secret))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def removeUserById(db : Session, user_id: int):
    rows_deleted = db.query(model.Usuario).where(model.Usuario.id == user_id).delete('auto')
    db.commit()
    return rows_deleted > 0

def putUser(db: Session, user: sch.Usuario):
    db_user = db.query(model.Usuario).filter(model.Usuario.id == user.id).first()
    if db_user:
        db_user.nombres = user.nombres | db_user.nombres
        db_user.apellidos = user.apellidos | db_user.apellidos
        db_user.secret = encodePassword(user.secret) | db_user.secret
        db_user.email = user.email | db_user.email
    return user


def obtenerAsociacionPorId(db : Session, asociacion_id: int):
    return db.query(model.Asociacion).get(asociacion_id)

def obtenerAsociaciones(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model.Asociacion).offset(skip).limit(limit).all()

def crearAsociacion(db: Session, asociacion: sch.AsociacionCreate):
    db_asociacion = model.Asociacion(**asociacion.model_dump())
    db.add(db_asociacion)
    db.commit()
    db.refresh(db_asociacion)
    return db_asociacion

def eliminarAsociacionPorId(db : Session, asociacion_id: int):
    return db.delete(model.Usuario).filter(model.Usuario.id == asociacion_id)

def actualizarAsociacion(db: Session, asociacion: sch.Asociacion):
    db_asociacion = db.query(model.Asociacion).filter(model.Asociacion.id == asociacion.id).first()
    if db_asociacion:
        db_asociacion.rol = asociacion.rol
        db_asociacion.organizacion_id = asociacion.organizacion_id
        db_asociacion.usuario_id = asociacion.usuario_id
    return asociacion

def obtenerOrganizacionPorId(db : Session, organizacion_id: int):
    return db.query(model.Organizacion).get(organizacion_id)

def obtenerOrganizaciones(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model.Organizacion).offset(skip).limit(limit).all()

def crearOrganizacion(db: Session, organizacion: sch.OrganizacionCreate):
    db_organizacion = model.Organizacion(nombre = organizacion.nombre, nombreWS = organizacion.nombreWS)
    db.add(db_organizacion)
    db.commit()
    db.refresh(db_organizacion)
    return db_organizacion

def eliminarOrganizacionPorId(db : Session, organizacion_id: int):
    return db.delete(model.Organizacion).filter(model.Organizacion.id == organizacion_id)

def actualizarOrganizacion(db: Session, asociacion: sch.Organizacion):
    db_organizacion = db.query(model.Organizacion).filter(model.Organizacion.id == asociacion.id).first()
    if db_organizacion:
        db_organizacion.nombre = asociacion.nombre
        db_organizacion.nombreWS = asociacion.nombreWS
    return asociacion
