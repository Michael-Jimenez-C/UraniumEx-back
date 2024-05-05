from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True)
    nombres = Column(String)
    apellidos = Column(String)
    email = Column(String, unique=True, index=True)
    secret = Column(String)
