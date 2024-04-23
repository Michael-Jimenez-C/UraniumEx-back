from pydantic import BaseModel

class Usuario(BaseModel):
    nombres:str
    apellidos: str = None
    email: str
    secret: str

class Asociacion(BaseModel):
    rol: str
    usuario_id:int
    organizacion_id:int

class Organizacion(BaseModel):
    nombre: str
    nombreWS: str

class Inventario(BaseModel):
    nombres: str
    ubicacion: str

class Stock(BaseModel):
    cantidad: int
    producto_id:int
    inventario_id:int

class Producto(BaseModel):
    nombre: str
    precio_venta: float
    precio_compra: float

class Proveedor(BaseModel):
    nombre: str
    contacto: str = None
    producto_id: int

class CantidadFactura(BaseModel):
    cantidad:int
    detalle: str
    factura_id: int
    producto_id:int
    
class Cliente(BaseModel):
    nombre: str
    cedula: str
    direccion: str = None

class Factura(BaseModel):
    cliente_id:str