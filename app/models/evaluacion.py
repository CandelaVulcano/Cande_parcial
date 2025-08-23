from app import db

class Evaluacion(db.Model):
    __tablename__ = 'evaluaciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Evaluacion {self.id}>'
