from pydantic import BaseModel


class CantidadFacturaBase(BaseModel):
    cantidad: int | None = None
    detalle: str | None = None
    factura_id: int
    producto_id: int


class CantidadFacturaCreate(CantidadFacturaBase):
    pass


class CantidadFactura(CantidadFacturaBase):
    id: int

    class Config:
        from_attributes = True