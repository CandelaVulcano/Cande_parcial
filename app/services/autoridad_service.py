from app.models.autoridad import Autoridad
from app.repositories.autoridad_repositorio import AutoridadRepository

class AutoridadService:
    @staticmethod
    def crear_autoridad(autoridad: Autoridad):
        return AutoridadRepository.crear(autoridad)

    @staticmethod
    def buscar_por_id(id: int) -> Autoridad:
        return AutoridadRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Autoridad]:
        return AutoridadRepository.buscar_todos()

    @staticmethod
    def actualizar_autoridad(autoridad: Autoridad) -> Autoridad:
        return AutoridadRepository.actualizar(autoridad)

    @staticmethod
    def borrar_por_id(id: int) -> Autoridad:
        return AutoridadRepository.borrar_por_id(id)
