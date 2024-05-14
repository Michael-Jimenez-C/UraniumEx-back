from pydantic import BaseModel

from app.routers.schemas.asociacion import Asociacion
from app.routers.schemas.inventario import Inventario



class OrganizacionBase(BaseModel):
    nombre: str
    nombreWS: str


class OrganizacionCreate(OrganizacionBase):
    pass


class Organizacion(OrganizacionBase):
    id: int
    asociaciones: list[Asociacion] = []
    inventarios: list[Inventario] = []

    class Config:
        from_attributes = True