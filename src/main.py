from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    nombres:str
    apellidos: str = None
    email: str
    secret: str

class Organizacion(BaseModel):
    nombre: str
    nombreWS: str

class Inventario(BaseModel):
    nombres: str
    ubicacion: str

class Producto(BaseModel):
    nombre: str
    precio_venta: float
    precio_compra: float

class Proveedor(BaseModel):
    nombre: str
    contacto: str = None
    producto_id: int

class Cliente(BaseModel):
    nombre: str
    cedula: str
    direccion: str = None

class Factura(BaseModel):
    cliente_id:str

import mysql.connector as dbman


app = FastAPI()

@app.get('/productos/')
async def getProducts(jwt:str, organization:int, inventory: int) -> dict:
    db = dbman.connect(
        host="localhost",
        port=33060,
        user="root",
        password="secret"
    )
    cur = db.cursor()
    cur.execute('SELECT * FROM BDAP.CLIENTE')
    return None

@app.delete('/productos')
async def delProducts():
    pass

@app.post('/productos')
async def postProducts():
    return {"":""}

@app.put('/productos')
async def putProducts():
    pass
