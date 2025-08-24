from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento(HashidMixin, db.Model):
    __tablename__ = 'tipos_documento'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(30), nullable=False, unique=True)
    alumnos = db.relationship(
        'Alumno', back_populates='tipo_documento', lazy=True)
