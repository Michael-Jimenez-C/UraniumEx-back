from pydantic import BaseModel
from app.routers.schemas.stock import Stock

class InventarioBase(BaseModel):
    nombre: str
    ubicacion: str
    organizacion_id: int


class InventarioCreate(InventarioBase):
    pass


class Inventario(InventarioBase):
    id: int
    stocks: list[Stock] = []

    class Config:
        from_attributes = True