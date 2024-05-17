from pydantic import BaseModel

from .asociacion import Asociacion
from .inventario import Inventario



class OrganizacionBase(BaseModel):
    nombre: str
    nombreWS: str


class OrganizacionCreate(OrganizacionBase):
    pass


class Organizacion(OrganizacionBase):
    id: int

    class Config:
        from_attributes = True