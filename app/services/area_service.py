from app.models.area import Area
from app.repositories.area_repositorio import AreaRepository

class AreaService:
    @staticmethod
    def crear_area(area: Area):
        return AreaRepository.crear(area)

    @staticmethod
    def buscar_por_id(id: int) -> Area:
        return AreaRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Area]:
        return AreaRepository.buscar_todos()

    @staticmethod
    def actualizar_area(area: Area) -> Area:
        return AreaRepository.actualizar(area)

    @staticmethod
    def borrar_por_id(id: int) -> Area:
        return AreaRepository.borrar_por_id(id)

