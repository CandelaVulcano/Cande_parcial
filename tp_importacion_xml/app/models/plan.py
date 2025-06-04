from sqlalchemy import Column, Integer, String
from .base import Base

class Plan(Base):
    __tablename__ = 'planes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    especialidad = Column(Integer, nullable=False)
    plan = Column(Integer, unique=True, nullable=False)
    nombre = Column(String, nullable=True)
