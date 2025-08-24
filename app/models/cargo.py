from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Cargo(HashidMixin, db.Model):
    __tablename__ = 'cargos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    puntos = db.Column(db.Integer, nullable=False)
    categoria_cargo_id = db.Column(db.Integer, db.ForeignKey(
        'categorias_cargo.id'), nullable=False)
    tipo_dedicacion_id = db.Column(db.Integer, db.ForeignKey(
        'tipos_dedicacion.id'), nullable=False)
    categoria_cargo = db.relationship(
        'CategoriaCargo', back_populates='cargos')
    tipo_dedicacion = db.relationship(
        'TipoDedicacion', back_populates='cargos')
