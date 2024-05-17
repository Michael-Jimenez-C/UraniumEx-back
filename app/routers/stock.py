from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas.stock import Stock, StockBase
from database.crud import stock as crud
from database.connection import get_db

router = APIRouter(
    prefix="/stock",
    tags=["stock"],
)

@router.get('')
async def get(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.get(db,skip,limit)

@router.get('/{id}')
async def getPorId(id: int, db: Session = Depends(get_db)):
    stock = crud.getById(db,id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock no encontrada")
    return stock

@router.post('')
async def post(stock: StockBase, db: Session = Depends(get_db)):
    return crud.create(db, stock)

@router.put('')
async def put(stock: Stock, db:Session = Depends(get_db)):
    return crud.update(db,stock)

@router.delete('/{id}', response_model=None)
async def delete(id:int, db: Session = Depends(get_db)):
    eliminado = crud.delete(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Stock no encontrada")
    return eliminado