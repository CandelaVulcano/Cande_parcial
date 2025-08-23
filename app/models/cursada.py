from app import db

class Cursada(db.Model):
    __tablename__ = 'cursadas'
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    anio = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Cursada {self.id}>'
