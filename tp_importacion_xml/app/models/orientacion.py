from sqlalchemy import Column, Integer, String
from .base import Base

class Orientacion(Base):
    __tablename__ = 'orientaciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    especialidad = Column(Integer, nullable=False)
    plan = Column(Integer, nullable=False)
    orientacion = Column(Integer, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
