from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas.inventario import Inventario, InventarioBase
from database.crud import Inventario as crud
from database.connection import get_db

router = APIRouter(
    prefix="/inventario",
    tags=["inventario"],
)

@router.get('')
async def get(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.get(db,skip,limit)

@router.get('/{id}')
async def getPorId(id: int, db: Session = Depends(get_db)):
    inventario = crud.getById(db,id)
    if not inventario:
        raise HTTPException(status_code=404, detail="Inventario no encontrada")
    return inventario

@router.post('')
async def post(inventario: InventarioBase, db: Session = Depends(get_db)):
    return crud.create(db, inventario)

@router.put('')
async def put(inventario: Inventario, db:Session = Depends(get_db)):
    return crud.update(db,inventario)

@router.delete('/{id}', response_model=None)
async def delOrg(id:int, db: Session = Depends(get_db)):
    eliminado = crud.delete(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Inventario no encontrada")
    return eliminado