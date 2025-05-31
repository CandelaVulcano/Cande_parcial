from app.models.grupo import Grupo
from app.repositories.grupo_repositorio import GrupoRepository

class GrupoService:
    @staticmethod
    def crear_grupo(grupo: Grupo):
        return GrupoRepository.crear(grupo)

    @staticmethod
    def buscar_por_id(id: int) -> Grupo:
        return GrupoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Grupo]:
        return GrupoRepository.buscar_todos()

    @staticmethod
    def actualizar_grupo(grupo: Grupo) -> Grupo:
        return GrupoRepository.actualizar(grupo)

    @staticmethod
    def borrar_por_id(id: int) -> Grupo:
        return GrupoRepository.borrar_por_id(id)
