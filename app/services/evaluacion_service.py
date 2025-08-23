from app.repositories.evaluacion_repositorio import EvaluacionRepository
from app.models.evaluacion import Evaluacion
from app import db

class EvaluacionService:
    @staticmethod
    def buscar_todos():
        return EvaluacionRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(id: int):
        return EvaluacionRepository.buscar_por_id(id)

    @staticmethod
    def crear(data):
        nueva_evaluacion = Evaluacion(**data)
        db.session.add(nueva_evaluacion)
        db.session.commit()
        return nueva_evaluacion

    @staticmethod
    def actualizar(id: int, data):
        evaluacion = EvaluacionRepository.buscar_por_id(id)
        if not evaluacion:
            return None
        for key, value in data.items():
            setattr(evaluacion, key, value)
        db.session.commit()
        return evaluacion

    @staticmethod
    def borrar_por_id(id: int):
        evaluacion = EvaluacionRepository.buscar_por_id(id)
        if not evaluacion:
            return None
        db.session.delete(evaluacion)
        db.session.commit()
        return evaluacion
