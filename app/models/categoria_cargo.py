from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class CategoriaCargo(HashidMixin, db.Model):
    __tablename__ = 'categorias_cargo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    cargos = db.relationship(
        'Cargo', back_populates='categoria_cargo', lazy=True)
