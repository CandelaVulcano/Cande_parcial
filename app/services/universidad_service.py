from app.models.universidad import Universidad
from app.repositories.universidad_repositorio import UniversidadRepository

class UniversidadService:
    @staticmethod
    def crear_universidad(universidad: Universidad):
        return UniversidadRepository.crear(universidad)

    @staticmethod
    def buscar_por_id(id: int) -> Universidad:
        return UniversidadRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Universidad]:
        return UniversidadRepository.buscar_todos()

    @staticmethod
    def actualizar_universidad(universidad: Universidad) -> Universidad:
        return UniversidadRepository.actualizar(universidad)

    @staticmethod
    def borrar_por_id(id: int) -> Universidad:
        return UniversidadRepository.borrar_por_id(id)
