from pydantic import BaseModel

   
class UsuarioGet(BaseModel):
    nombres:str
    apellidos: str = None
    email: str

class UsuarioCreate(UsuarioGet):
    secret:str

class Usuario(UsuarioCreate):
    id: int

    class Config:
        orm_mode = True