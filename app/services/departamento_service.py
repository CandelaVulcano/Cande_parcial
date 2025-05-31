from app.models.departamento import Departamento
from app.repositories.departamento_repositorio import DepartamentoRepository

class DepartamentoService:
    @staticmethod
    def crear_departamento(departamento: Departamento):
        return DepartamentoRepository.crear(departamento)

    @staticmethod
    def buscar_por_id(id: int) -> Departamento:
        return DepartamentoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Departamento]:
        return DepartamentoRepository.buscar_todos()

    @staticmethod
    def actualizar_departamento(departamento: Departamento) -> Departamento:
        return DepartamentoRepository.actualizar(departamento)

    @staticmethod
    def borrar_por_id(id: int) -> Departamento:
        return DepartamentoRepository.borrar_por_id(id)
