from pydantic import BaseModel

   
class UsuarioGet(BaseModel):
    nombres:str
    apellidos: str = None
    email: str

class UsuarioC(UsuarioGet):
    secret:str

class Usuario(UsuarioC):
    id: int

    class Config:
        orm_mode = True