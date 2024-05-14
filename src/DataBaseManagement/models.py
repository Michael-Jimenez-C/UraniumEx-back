from sqlalchemy import VARCHAR, Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(VARCHAR(45), nullable=False)
    apellidos = Column(VARCHAR(45), nullable=True)
    email = Column(VARCHAR(45), unique=True, nullable=False)
    secret = Column(VARCHAR(45), nullable=False)

    asociaciones = relationship("Asociacion", back_populates="usuario")


class Asociacion(Base):
    __tablename__ = "asociacion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(VARCHAR(10), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    organizacion_id = Column(Integer, ForeignKey("organizacion.id"))

    usuario = relationship("Usuario", back_populates="asociaciones")
    organizacion = relationship("Organizacion", back_populates="asociaciones")


class Organizacion(Base):
    __tablename__ = "organizacion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(VARCHAR(45), nullable=False)
    nombreWS = Column(VARCHAR(45), nullable=False)

    asociaciones = relationship("Asociacion", back_populates="organizacion")
    inventarios = relationship("Inventario", back_populates="organizacion")


class Inventario(Base):
    __tablename__ = "inventario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(VARCHAR(45), nullable=False)
    ubicacion = Column(VARCHAR(45), nullable=False)
    organizacion_id = Column(Integer, ForeignKey("organizacion.id"))

    organizacion = relationship("Organizacion", back_populates="inventarios")
    stocks = relationship("Stock", back_populates="inventario")


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cantidad = Column(Integer, nullable=False)

    producto_id = Column(Integer, ForeignKey("producto.id"))
    inventario_id = Column(Integer, ForeignKey("inventario.id"))

    producto = relationship("Producto", back_populates="stocks")
    inventario = relationship("Inventario", back_populates="stocks")


class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(VARCHAR(45), nullable=False)
    precio = Column(Float, nullable=False)

    stocks = relationship("Stock", back_populates="producto")
    cantidad_facturas = relationship("CantidadFactura", back_populates="producto")


class CantidadFactura(Base):
    __tablename__ = "cantidadfactura"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cantidad = Column(Integer, nullable=True)
    detalle = Column(VARCHAR(45), nullable=True)
    factura_id = Column(Integer, ForeignKey("factura.id"))
    producto_id = Column(Integer, ForeignKey("producto.id"))

    factura = relationship("Factura", back_populates="cantidad_facturas")
    producto = relationship("Producto", back_populates="cantidad_facturas")


class Factura(Base):
    __tablename__ = "factura"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))

    cliente = relationship("Cliente", back_populates="facturas")
    cantidad_facturas = relationship("CantidadFactura", back_populates="factura")


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(VARCHAR(45), nullable=False)
    cedula = Column(VARCHAR(10), nullable=False)
    direccion = Column(VARCHAR(45), nullable=True)

    facturas = relationship("Factura", back_populates="cliente")
