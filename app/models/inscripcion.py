from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Inscripcion(db.Model):
    __tablename__ = 'inscripciones'
    id: int = db.Column(db.Integer, primary_key=True)
    alumno_id: int = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    materia_id: int = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    fecha: str = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Inscripcion {self.id}>'
