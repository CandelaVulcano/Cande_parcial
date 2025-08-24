from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Materia(HashidMixin, db.Model):
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(20), nullable=False)
    observacion = db.Column(db.String(200), nullable=True)
    departamento_id = db.Column(db.Integer, db.ForeignKey(
        'departamentos.id'), nullable=False)
    departamento = db.relationship('Departamento', back_populates='materias')
    orientaciones = db.relationship(
        'Orientacion', back_populates='materia', lazy=True)
