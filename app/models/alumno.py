from dataclasses import dataclass
from app import db
from app.models.alumno_grupo import alumno_grupo
from flask_hashids import HashidMixin


@dataclass(init=False, repr=True, eq=True)
class Alumno(HashidMixin, db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apellido = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    nro_documento = db.Column(db.String(20), nullable=False)
    tipo_documento_id = db.Column(db.Integer, db.ForeignKey(
        'tipos_documento.id'), nullable=False)
    fecha_nacimiento = db.Column(db.String(20), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)  # “M” o “F”
    nro_legajo = db.Column(db.Integer, nullable=False)
    fecha_ingreso = db.Column(db.String(20), nullable=False)
    tipo_documento = db.relationship('TipoDocumento', back_populates='alumnos')
    grupos = db.relationship(
        'Grupo', secondary=alumno_grupo, back_populates='alumnos')
