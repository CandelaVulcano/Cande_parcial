from app.models import Facultad
from app.repositories.facultad_repositorio import FacultadRepository

class FacultadService:
   
    @staticmethod
    def crear_facultad(facultad: Facultad):
        FacultadRepository.crear(facultad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Facultad:
        return FacultadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Facultad]:
        return FacultadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_facultad(id: int, facultad: Facultad) -> Facultad:
        facultad_existente = FacultadRepository.buscar_por_id(id)
        if not facultad_existente:
            return None
        facultad_existente.nombre = facultad.nombre
        facultad_existente.abreviatura = facultad.abreviatura
        facultad_existente.directorio = facultad.directorio
        facultad_existente.sigla = facultad.sigla
        facultad_existente.codigo_postal = facultad.codigo_postal
        facultad_existente.ciudad = facultad.ciudad
        facultad_existente.domicilio = facultad.domicilio
        facultad_existente.telefono = facultad.telefono
        facultad_existente.contacto = facultad.contacto
        return facultad_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Facultad:
        facultad = FacultadRepository.buscar_por_id(id)
        if not facultad:
            return None
        return facultad