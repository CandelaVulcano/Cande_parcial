from sqlalchemy import Column, Integer, String
from .base import Base

class Materia(Base):
    __tablename__ = 'materias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    especialidad = Column(Integer, nullable=False)
    plan = Column(Integer, nullable=False)
    materia = Column(Integer, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    ano = Column(Integer, nullable=True)
