from pydantic import BaseModel

class InventarioBase(BaseModel):
    nombre: str
    ubicacion: str
    organizacion_id: int

class Inventario(InventarioBase):
    id: int

    class Config:
        from_attributes = True
        