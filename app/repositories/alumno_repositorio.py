from app.models.alumno import Alumno

class AlumnoRepository:
    def __init__(self):
        self.alumnos = []

    def agregar(self, alumno: Alumno):
        self.alumnos.append(alumno)

    def listar(self):
        return self.alumnos