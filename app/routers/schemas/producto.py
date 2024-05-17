from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    precio_venta: float
    precio_compra: float


class Producto(ProductoBase):
    id: int

    class Config:
        from_attributes = True