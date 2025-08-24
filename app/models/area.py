from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Area(HashidMixin, db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamentos = db.relationship('Departamento', backref='area', lazy=True)
