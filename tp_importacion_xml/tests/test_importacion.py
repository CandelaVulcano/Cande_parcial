import unittest
from app.models import Pais, Localidad, Grado, Facultad, Universidad, Materia, Especialidad, Orientacion, Plan
from app.repositories.session import get_session

class TestImportacionDatos(unittest.TestCase):
    def setUp(self):
        self.session = get_session()

    def tearDown(self):
        self.session.close()

    def test_paises_importados(self):
        paises = self.session.query(Pais).all()
        self.assertGreater(len(paises), 0, "No se importaron países")

    def test_localidades_importadas(self):
        localidades = self.session.query(Localidad).all()
        self.assertGreater(len(localidades), 0, "No se importaron localidades")

    def test_grados_importados(self):
        grados = self.session.query(Grado).all()
        self.assertGreater(len(grados), 0, "No se importaron grados")

    def test_facultades_importadas(self):
        facultades = self.session.query(Facultad).all()
        self.assertGreater(len(facultades), 0, "No se importaron facultades")

    def test_universidades_importadas(self):
        universidades = self.session.query(Universidad).all()
        self.assertGreater(len(universidades), 0, "No se importaron universidades")

    def test_materias_importadas(self):
        materias = self.session.query(Materia).all()
        self.assertGreater(len(materias), 0, "No se importaron materias")

    def test_especialidades_importadas(self):
        especialidades = self.session.query(Especialidad).all()
        self.assertGreater(len(especialidades), 0, "No se importaron especialidades")

    def test_orientaciones_importadas(self):
        orientaciones = self.session.query(Orientacion).all()
        self.assertGreater(len(orientaciones), 0, "No se importaron orientaciones")

    def test_planes_importados(self):
        planes = self.session.query(Plan).all()
        self.assertGreater(len(planes), 0, "No se importaron planes")

if __name__ == '__main__':
    unittest.main()
