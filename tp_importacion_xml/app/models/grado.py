from sqlalchemy import Column, Integer, String
from .base import Base

class Grado(Base):
    __tablename__ = 'grados'
    id = Column(Integer, primary_key=True, autoincrement=True)
    grado = Column(Integer, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
