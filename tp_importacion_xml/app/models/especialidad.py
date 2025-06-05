from sqlalchemy import Column, Integer, String
from .base import Base

class Especialidad(Base):
    __tablename__ = 'especialidades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    especialidad = Column(Integer, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
