from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(20), nullable=False)
    observacion = db.Column(db.String(200), nullable=True)
    orientaciones = db.relationship('Orientacion', back_populates='materia', lazy=True)