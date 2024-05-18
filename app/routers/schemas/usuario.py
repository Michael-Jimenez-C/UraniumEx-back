from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nombres: str
    apellidos: str | None = None
    email: str


class UsuarioCreate(UsuarioBase):
    secret: str

class UsuarioLogin(BaseModel):
    email:str
    secret: str

class Usuario(UsuarioCreate):
    id: int

    class Config:
        from_attributes = True