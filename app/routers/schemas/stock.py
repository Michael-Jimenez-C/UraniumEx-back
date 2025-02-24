from pydantic import BaseModel


class StockBase(BaseModel):
    cantidad: int
    producto_id: int
    inventario_id: int


class Stock(StockBase):
    id: int

    class Config:
        from_attributes = True