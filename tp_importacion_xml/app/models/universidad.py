from sqlalchemy import Column, Integer, String
from .base import Base

class Universidad(Base):
    __tablename__ = 'universidades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    universida = Column(Integer, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
