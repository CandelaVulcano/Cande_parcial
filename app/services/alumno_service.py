from app.models import Alumno
from app.repositories.alumno_repositorio import AlumnoRepository

class AlumnoService:
   
    @staticmethod
    def crear_alumno(alumno: Alumno):
        AlumnoRepository.crear(alumno)
    
    @staticmethod
    def buscar_por_id(id: int) -> Alumno:
        return AlumnoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Alumno]:
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_alumno(id: int, alumno: Alumno) -> Alumno:
        alumno_existente = AlumnoRepository.buscar_por_id(id)
        if not alumno_existente:
            return None
        alumno_existente.nombre = alumno.nombre
        alumno_existente.apellido = alumno.apellido
        alumno_existente.nro_documento = alumno.nro_documento
        alumno_existente.tipo_documento_id = alumno.tipo_documento_id
        alumno_existente.fecha_nacimiento = alumno.fecha_nacimiento
        alumno_existente.sexo = alumno.sexo
        alumno_existente.nro_legajo = alumno.nro_legajo
        alumno_existente.fecha_ingreso = alumno.fecha_ingreso
        return alumno_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Alumno:
        alumno = AlumnoRepository.buscar_por_id(id)
        if not alumno:
            return None
        return alumno