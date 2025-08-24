from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Plan(HashidMixin, db.Model):
    __tablename__ = 'planes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.String(20), nullable=False)
    fecha_fin = db.Column(db.String(20), nullable=True)
    observacion = db.Column(db.String(200), nullable=True)
    orientaciones = db.relationship(
        'Orientacion', back_populates='plan', lazy=True)
