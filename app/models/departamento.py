from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Departamento(HashidMixin, db.Model):
    __tablename__ = 'departamentos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    facultad_id = db.Column(db.Integer, db.ForeignKey(
        'facultades.id'), nullable=False)
    facultad = db.relationship('Facultad', back_populates='departamentos')
    materias = db.relationship(
        'Materia', back_populates='departamento', lazy=True)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=True)
