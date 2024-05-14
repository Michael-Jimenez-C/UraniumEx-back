from pydantic import BaseModel

from app.routers.schemas.factura import Factura

class ClienteBase(BaseModel):
    nombre: str
    cedula: str
    direccion: str | None


class ClienteCreate(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int
    facturas: list[Factura] = []

    class Config:
        from_attributes = True
