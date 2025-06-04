from sqlalchemy import Column, Integer, String
from .base import Base

class Localidad(Base):
    __tablename__ = 'localidades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(Integer, unique=True, nullable=False)
    ciudad = Column(String, nullable=False)
    provincia = Column(String, nullable=False)
    pais_del_c = Column(String, nullable=False)
