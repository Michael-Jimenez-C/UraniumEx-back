from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas.organizacion import Organizacion, OrganizacionCreate
from database.crud import organizacion as crud
from database.connection import get_db

router = APIRouter(
    prefix="/organizacion",
    tags=["organizacion"],
)

@router.get('')
async def get(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.get(db,skip,limit)

@router.get('/{id}')
async def getPorId(id: int, db: Session = Depends(get_db)):
    organizacion = crud.getById(db,id)
    if not organizacion:
        raise HTTPException(status_code=404, detail="Organizacion no encontrada")
    return organizacion

@router.post('')
async def post(organizacion: OrganizacionCreate, db: Session = Depends(get_db)):
    return crud.create(db, organizacion)

@router.put('')
async def put(organizacion: Organizacion, db:Session = Depends(get_db)):
    return crud.update(db,organizacion)

@router.delete('/{id}', response_model=None)
async def delOrg(id:int, db: Session = Depends(get_db)):
    eliminado = crud.delete(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Organizacion no encontrada")
    return eliminado