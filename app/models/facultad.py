from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Facultad(HashidMixin, db.Model):
    __tablename__ = 'facultades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    abreviatura = db.Column(db.String(10), nullable=False)
    directorio = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(10), nullable=False)
    codigo_postal = db.Column(db.String(10), nullable=True)
    ciudad = db.Column(db.String(50), nullable=True)
    domicilio = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    contacto = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    universidad_id = db.Column(db.Integer, db.ForeignKey(
        'universidades.id'), nullable=False)
    universidad = db.relationship('Universidad', back_populates='facultades')
    autoridades = db.relationship(
        'Autoridad', back_populates='facultad', lazy=True)
    departamentos = db.relationship(
        'Departamento', back_populates='facultad', lazy=True)
