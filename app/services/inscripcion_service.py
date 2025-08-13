from app.repositories.inscripcion_repositorio import InscripcionRepository

class InscripcionService:
    @staticmethod
    def buscar_todos():
        return InscripcionRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(id: int):
        return InscripcionRepository.buscar_por_id(id)

    @staticmethod
    def crear(inscripcion):
        return InscripcionRepository.crear(inscripcion)

    @staticmethod
    def actualizar(inscripcion):
        return InscripcionRepository.actualizar(inscripcion)

    @staticmethod
    def borrar_por_id(id: int):
        return InscripcionRepository.borrar_por_id(id)
