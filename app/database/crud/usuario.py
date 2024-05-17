from sqlalchemy.orm import Session
from routers.schemas.usuario import Usuario, UsuarioCreate
from database.models.models import Usuario as model

import hashlib

def encodePassword(password: str) -> str | None:
    if not password:
        return None
    h = hashlib.new('sha512_256')
    h.update(bytes(password, encoding="utf-8"))
    return h.hexdigest()



def getById(db : Session, user_id: int):
    return db.query(model).filter(model.id == user_id).first()

def getByEmail(db : Session, email: int):
    return db.query(model).filter(model.email == email).first()

def get(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def create(db: Session, user: UsuarioCreate):
    db_user = model(nombres = user.nombres, apellidos = user.apellidos, email=user.email, secret=encodePassword(user.secret))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete(db : Session, user_id: int):
    rows_deleted = db.query(model).where(model.id == user_id).delete('auto')
    db.commit()
    return rows_deleted > 0

def update(db: Session, user: Usuario):
    db_user = db.query(model).filter(model.id == user.id).first()
    if db_user:
        db_user.nombres = user.nombres or db_user.nombres
        db_user.apellidos = user.apellidos or db_user.apellidos
        db_user.secret = encodePassword(user.secret) or db_user.secret
        db_user.email = user.email or db_user.email
        db.commit()
        return True
    return False