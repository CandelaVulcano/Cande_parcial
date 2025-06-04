from sqlalchemy import Column, Integer, String
from .base import Base

class Facultad(Base):
    __tablename__ = 'facultades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    facultad = Column(Integer, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
