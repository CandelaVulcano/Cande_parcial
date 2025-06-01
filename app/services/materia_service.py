from app.models import Materia
from app.repositories.materia_repositorio import MateriaRepository

class MateriaService:
   
    @staticmethod
    def crear_materia(materia: Materia):
        MateriaRepository.crear(materia)
    
    @staticmethod
    def buscar_por_id(id: int) -> Materia:
        return MateriaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Materia]:
        return MateriaRepository.buscar_todos()
    
    @staticmethod
    def actualizar_materia(id: int, materia: Materia) -> Materia:
        materia_existente = MateriaRepository.buscar_por_id(id)
        if not materia_existente:
            return None
        materia_existente.nombre = materia.nombre
        materia_existente.codigo = materia.codigo
        materia_existente.observacion = materia.observacion
        materia_existente.departamento_id = materia.departamento_id
        return materia_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Materia:
        materia = MateriaRepository.buscar_por_id(id)
        if not materia:
            return None
        return materia