from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Especialidad(HashidMixin, db.Model):
    __tablename__ = 'especialidades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String(5), nullable=True)
    observacion = db.Column(db.String(200), nullable=True)
    tipo_especialidad_id = db.Column(db.Integer, db.ForeignKey(
        'tipos_especialidad.id'), nullable=False)
    tipo_especialidad = db.relationship(
        'TipoEspecialidad', back_populates='especialidades')
    orientaciones = db.relationship(
        'Orientacion', back_populates='especialidad', lazy=True)
