from pydantic import BaseModel
from .asociacion import Asociacion


class UsuarioBase(BaseModel):
    nombres: str
    apellidos: str | None = None
    email: str


class UsuarioCreate(UsuarioBase):
    secret: str


class Usuario(UsuarioCreate):
    id: int
    asociaciones: list[Asociacion] = []

    class Config:
        from_attributes = True