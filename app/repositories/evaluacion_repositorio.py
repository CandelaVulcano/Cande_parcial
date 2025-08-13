from app.models.evaluacion import Evaluacion
from app import db

class EvaluacionRepository:
    @staticmethod
    def buscar_todos():
        return db.session.query(Evaluacion).all()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Evaluacion).filter_by(id=id).first()
