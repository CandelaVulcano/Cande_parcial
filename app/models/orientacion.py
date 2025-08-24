from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Orientacion(HashidMixin, db.Model):
    __tablename__ = 'orientaciones'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad_id = db.Column(db.Integer, db.ForeignKey(
        'especialidades.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey(
        'materias.id'), nullable=False)
    especialidad = db.relationship(
        'Especialidad', back_populates='orientaciones')
    plan = db.relationship('Plan', back_populates='orientaciones')
    materia = db.relationship('Materia', back_populates='orientaciones')
