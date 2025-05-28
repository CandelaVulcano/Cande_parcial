from dataclasses import dataclass
from app import db
from app.models.alumno_grupo import alumno_grupo

@dataclass(init=False, repr=True, eq=True)
class Grupo(db.Model):
    __tablename__ = 'grupos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    alumnos = db.relationship('Alumno', secondary=alumno_grupo, back_populates='grupos')