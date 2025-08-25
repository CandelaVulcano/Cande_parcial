import unittest
import os
import sys
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import current_app
def create_simple_app(config_name='testing'):
    from flask import Flask
    from app.config import config
    
    app = Flask(__name__)
    config_class = config.get(config_name, config['default'])
    app.config.from_object(config_class)
    from app import db
    db.init_app(app)
    
    return app

from app import db
from app.models.inscripcion import Inscripcion
from app.repositories.inscripcion_repositorio import InscripcionRepository

class InscripcionTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def __nuevaInscripcion(self, alumno_id=1, materia_id=1, fecha=None):
        ins = Inscripcion()
        ins.alumno_id = alumno_id
        ins.materia_id = materia_id
        ins.fecha = fecha or datetime.date.today()
        return ins

    def test_inscripcion_creation(self):
        ins = self.__nuevaInscripcion()
        self.assertIsNotNone(ins)
        self.assertEqual(ins.alumno_id, 1)
        self.assertEqual(ins.materia_id, 1)
        self.assertIsNotNone(ins.fecha)

    def test_crear_inscripcion(self):
        ins = self.__nuevaInscripcion()
        InscripcionRepository.crear(ins)
        self.assertIsNotNone(ins.id)
        encontrada = InscripcionRepository.buscar_por_id(ins.id)
        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada.alumno_id, ins.alumno_id)

    def test_buscar_todos_inscripciones(self):
        ins1 = self.__nuevaInscripcion(alumno_id=1, materia_id=1)
        ins2 = self.__nuevaInscripcion(alumno_id=2, materia_id=2)
        InscripcionRepository.crear(ins1)
        InscripcionRepository.crear(ins2)
        todas = InscripcionRepository.buscar_todos()
        self.assertIsNotNone(todas)
        self.assertEqual(len(todas), 2)
        self.assertIn(ins1, todas)
        self.assertIn(ins2, todas)

    def test_actualizar_inscripcion(self):
        ins = self.__nuevaInscripcion(alumno_id=1, materia_id=1)
        InscripcionRepository.crear(ins)
        ins.alumno_id = 42
        actualizado = InscripcionRepository.actualizar(ins)
        self.assertIsNotNone(actualizado)
        self.assertEqual(actualizado.alumno_id, 42)
        desde_db = InscripcionRepository.buscar_por_id(ins.id)
        self.assertEqual(desde_db.alumno_id, 42)

    def test_borrar_inscripcion(self):
        ins = self.__nuevaInscripcion()
        InscripcionRepository.crear(ins)
        borrado = InscripcionRepository.borrar_por_id(ins.id)
        self.assertIsNotNone(borrado)
        encontrado = InscripcionRepository.buscar_por_id(ins.id)
        self.assertIsNone(encontrado)

if __name__ == '__main__':
    unittest.main()