from sqlalchemy.orm import Session
import DataSchemes as sch
import DataBaseManagement as model

import hashlib

def encodePassword(password: str) -> str:
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

def createUser(db: Session, user: sch.Usuario):
    db_user = model.Usuario(nombres = user.nombres, apellidos = user.apellidos, email=user.email, secret=encodePassword(user.secret))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def removeUserById(db : Session, user_id: int):
    pass

def PutUser(db: Session, user: sch.Usuario):
    db_user = db.query(model.Usuario).filter(model.Usuario.id == user.id).first()
    if db_user:
        db_user.nombres = user.nombres | db_user.nombres
        db_user.apellidos = user.apellidos | db_user.apellidos
        db_user.secret = encodePassword(user.secret) | db_user.secret
        db_user.email = user.email | db_user.email
    return user