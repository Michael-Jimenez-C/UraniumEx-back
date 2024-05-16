from pydantic import BaseModel

from .cantidad_factura import CantidadFactura

class FacturaBase(BaseModel):
    cliente_id: int


class FacturaCreate(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int
    cantidad_facturas: list[CantidadFactura] = []

    class Config:
        from_attributes = True