from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from database.crud import usuario as crud
from .schemas.usuario import Usuario, UsuarioCreate, UsuarioBase
from database.connection import get_db
from dependencies import create_access_token

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
)

@router.get('', response_model=list[UsuarioBase])
async def getUsuarios(skip:int = 0, limit:int = 100,db: Session = Depends(get_db)):
    return crud.get(db,skip,limit)

@router.get('/{id}', response_model=UsuarioBase)
async def getUsuario(id:int, db: Session = Depends(get_db)):
    user = crud.getById(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post('')
async def signIn(user: UsuarioCreate, db: Session = Depends(get_db)):
    user = crud.create(db, user = user)
    return create_access_token({'n':user.nombres, 'a':user.apellidos},timedelta(minutes=30))

@router.put('', response_model=None)
async def putUsuario(user: Usuario, db: Session = Depends(get_db)):
    return crud.update(db,user)

@router.delete('/{id}', response_model=None)
async def delUsuario(id:int, db: Session = Depends(get_db)):
    eliminado = crud.delete(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return eliminado