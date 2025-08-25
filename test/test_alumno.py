import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_creacion_alumno(self):
        alumno = Alumno()
        alumno.apellido = "Perez"
        alumno.nombre = "Juan"
        alumno.nro_documento = "12345678"
        alumno.tipo_documento_id = 1
        alumno.fecha_nacimiento = "2000-01-01"
        alumno.sexo = "M"
        alumno.nro_legajo = 1001
        alumno.fecha_ingreso = "2018-03-01"
        self.assertEqual(alumno.nombre, "Juan")

if __name__ == '__main__':
    unittest.main()