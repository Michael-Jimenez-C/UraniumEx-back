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


class StockBase(BaseModel):
    cantidad: int
    producto_id: int
    inventario_id: int


class StockCreate(StockBase):
    pass


class Stock(StockBase):
    id: int

    class Config:
        from_attributes = True


class InventarioBase(BaseModel):
    nombre: str
    ubicacion: str
    organizacion_id: int


class InventarioCreate(InventarioBase):
    pass


class Inventario(InventarioBase):
    id: int
    stocks: list[Stock] = []

    class Config:
        from_attributes = True


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


class CantidadFacturaBase(BaseModel):
    cantidad: int | None = None
    detalle: str | None = None
    factura_id: int
    producto_id: int


class CantidadFacturaCreate(CantidadFacturaBase):
    pass


class CantidadFactura(CantidadFacturaBase):
    id: int

    class Config:
        from_attributes = True


class ProductoBase(BaseModel):
    nombre: str
    precio: float


class ProductoCreate(ProductoBase):
    pass


class Producto(ProductoBase):
    id: int
    stocks: list[Stock] = []
    cantidad_facturas: list[CantidadFactura] = []

    class Config:
        from_attributes = True


class FacturaBase(BaseModel):
    cliente_id: int


class FacturaCreate(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int
    cantidad_facturas: list[CantidadFactura] = []

    class Config:
        from_attributes = True


class ClienteBase(BaseModel):
    nombre: str
    cedula: str
    direccion: str | None


class ClienteCreate(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int
    facturas: list[Factura] = []

    class Config:
        from_attributes = True
