from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from routers.schemas.asociacion import Asociacion, AsociacionCreate
import database.crud.asociacion as crud
from database.connection import get_db

router = APIRouter(
    prefix="/asociacion",
    tags=["asociacion"],
    dependencies=[Depends(get_db)]
)


@router.get('', response_model=list[AsociacionCreate])
async def getAsociaciones(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.get(db,skip,limit)

@router.get('/{id}', response_model=AsociacionCreate)
async def getAsociacionPorId(id: int, db: Session = Depends(get_db)):
    asociacion = crud.getById(db,id)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociacion no encontrada")
    return 

@router.post('')
async def postAsociacion(asociacion: AsociacionCreate, db: Session = Depends(get_db)):
    return crud.create(db, asociacion)

@router.put('')
async def putAsociacion(asociacion: Asociacion, db:Session = Depends(get_db)):
    return crud.update(db,asociacion)

@router.delete('/{id}', response_model=None)
async def delAsociacion(id:int, db: Session = Depends(get_db)):
    eliminado = crud.delete(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return eliminado