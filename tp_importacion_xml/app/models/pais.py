from sqlalchemy import Column, Integer, String
from .base import Base

class Pais(Base):
    __tablename__ = 'paises'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pais = Column(Integer, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
