from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Autoridad(HashidMixin, db.Model):
    __tablename__ = 'autoridades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    facultad_id = db.Column(db.Integer, db.ForeignKey(
        'facultades.id'), nullable=False)
    facultad = db.relationship('Facultad', back_populates='autoridades')
