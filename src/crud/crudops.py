from sqlalchemy.orm import Session
import DataSchemes as sch
import DataBaseManagement as model

import hashlib


def getUserbyId(db : Session, user_id: int):
    return db.query(model.Usuario).filter(model.Usuario.id == user_id).first()

def getUserByEmail(db : Session, email: int):
    return db.query(model.Usuario).filter(model.Usuario.email == email).first()

def getUsers(db : Session, skip: int = 0, limit: int = 100):
    return db.query(model.Usuario).offset(skip).limit(limit).all()

def createUser(db: Session, user: sch.Usuario):
    h = hashlib.new('sha512_256')
    h.update(bytes(user.secret, encoding="utf-8"))
    hashedpassword = h.hexdigest()
    db_user = model.Usuario(nombres = user.nombres, apellidos = user.apellidos, email=user.email, secret=hashedpassword)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def removeUserById(db : Session, user_id: int):
    pass