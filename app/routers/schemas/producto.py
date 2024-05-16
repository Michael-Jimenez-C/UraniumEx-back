from pydantic import BaseModel

from app.routers.schemas.stock import Stock
from app.routers.schemas.cantidad_factura import CantidadFactura


class ProductoBase(BaseModel):
    nombre: str
    precio: float


class ProductoCreate(ProductoBase):
    pass


class Producto(ProductoBase):
    id: int
    stocks: list[Stock] = []
    cantidad_facturas: list[CantidadFactura] = []

    class Config:
        from_attributes = True