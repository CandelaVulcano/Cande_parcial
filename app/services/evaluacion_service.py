from app.repositories.evaluacion_repositorio import EvaluacionRepository

class EvaluacionService:
    @staticmethod
    def buscar_todos():
        return EvaluacionRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(id: int):
        return EvaluacionRepository.buscar_por_id(id)
