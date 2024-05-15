from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.routers.schemas.asociacion import Asociacion, AsociacionCreate
import app.database.crud.asociacion as crud
from app.database.connection import get_db

router = APIRouter(
    prefix="/asociacion",
    tags=["asociacion"],
    dependencies=[Depends(get_db)]
)


@router.get('')
async def getAsociaciones(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.obtenerAsociaciones(db,skip,limit)

@router.get('/{id}')
async def getAsociacionPorId(id: int, db: Session = Depends(get_db)):
    asociacion = crud.obtenerAsociacionPorId(db,id)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociacion no encontrada")
    return 

@router.post('')
async def postAsociacion(asociacion: AsociacionCreate, db: Session = Depends(get_db)):
    return crud.crearAsociacion(db, asociacion)

@router.put('')
async def putAsociacion(asociacion: Asociacion, db:Session = Depends(get_db)):
    return crud.actualizarAsociacion(db,asociacion)