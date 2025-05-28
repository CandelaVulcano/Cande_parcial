from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Grado(db.Model):
    __tablename__ = 'grados'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)