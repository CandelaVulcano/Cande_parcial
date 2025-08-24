from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class TipoEspecialidad(HashidMixin, db.Model):
    __tablename__ = 'tipos_especialidad'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.String(50), nullable=False)
    especialidades = db.relationship(
        'Especialidad', back_populates='tipo_especialidad', lazy=True)
