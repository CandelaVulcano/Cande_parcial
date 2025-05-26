import unittest
from app.models.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_creacion_alumno(self):
        alumno = Alumno("Perez", "Juan", "12345678", "DNI", "2000-01-01", "M", 1001, "2018-03-01")
        self.assertEqual(alumno.nombre, "Juan")

if __name__ == '__main__':
    unittest.main()