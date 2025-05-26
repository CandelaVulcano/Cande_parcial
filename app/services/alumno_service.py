from app.repositories.alumno_repositorio import AlumnoRepository
from app.models.alumno import Alumno

class AlumnoService:
    def __init__(self, repo: AlumnoRepository):
        self.repo = repo

    def crear_alumno(self, **kwargs):
        alumno = Alumno(**kwargs)
        self.repo.agregar(alumno)
        return alumno