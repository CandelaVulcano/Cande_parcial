from app.models import Cargo
from app.repositories.cargo_repositorio import CargoRepository

class CargoService:
    @staticmethod
    def crear_cargo(cargo: Cargo):
        CargoRepository.crear(cargo)
    
    @staticmethod
    def buscar_por_id(id: int) -> Cargo:
        return CargoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Cargo]:
        return CargoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_cargo(id: int, cargo: Cargo) -> Cargo:
        cargo_existente = CargoRepository.buscar_por_id(id)
        if not cargo_existente:
            return None
        cargo_existente.nombre = cargo.nombre
        cargo_existente.puntos = cargo.puntos
        cargo_existente.categoria_cargo_id = cargo.categoria_cargo_id
        cargo_existente.tipo_dedicacion_id = cargo.tipo_dedicacion_id
        return cargo_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Cargo:
        cargo = CargoRepository.buscar_por_id(id)
        if not cargo:
            return None
        return cargo  
        