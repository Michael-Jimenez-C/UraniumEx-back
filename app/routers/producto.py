from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas.producto import Producto, ProductoBase
from database.crud import producto as crud
from database.connection import get_db

router = APIRouter(
    prefix="/producto",
    tags=["producto"],
)

@router.get('')
async def get(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.get(db,skip,limit)

@router.get('/{id}')
async def getPorId(id: int, db: Session = Depends(get_db)):
    producto = crud.getById(db,id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrada")
    return producto

@router.post('')
async def post(producto: ProductoBase, db: Session = Depends(get_db)):
    return crud.create(db, producto)

@router.put('')
async def put(producto: Producto, db:Session = Depends(get_db)):
    return crud.update(db,producto)

@router.delete('/{id}', response_model=None)
async def delOrg(id:int, db: Session = Depends(get_db)):
    eliminado = crud.delete(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrada")
    return eliminado