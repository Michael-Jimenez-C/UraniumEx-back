from pydantic import BaseModel


class AsociacionBase(BaseModel):
    rol: str


class AsociacionCreate(AsociacionBase):
    usuario_id: int
    organizacion_id: int
    pass


class Asociacion(AsociacionCreate):
    id: int

    class Config:
        from_attributes = True
