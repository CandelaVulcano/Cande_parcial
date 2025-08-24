from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixmin

@dataclass(init=False, repr=True, eq=True)
class Grado(HashidMixmin, db.Model):
    __tablename__ = 'grados'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
