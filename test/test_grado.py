import unittest
import os
import sys

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

from app.models.grado import Grado
from app.repositories.grado_repositorio import GradoRepository
from app import db


class GradoTestCase(unittest.TestCase):

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

    def test_grado_creation(self):
        grado = self.__nuevoGrado()
        self.assertIsNotNone(grado)
        self.assertEqual(grado.nombre, "Licenciatura")

    def test_crear_grado(self):
        grado = self.__nuevoGrado()
        GradoRepository.crear(grado)
        self.assertIsNotNone(grado)
        self.assertIsNotNone(grado.id)
        self.assertGreaterEqual(grado.id, 1)
        self.assertEqual(grado.nombre, "Licenciatura")

    def test_grado_busqueda(self):
        grado = self.__nuevoGrado()
        GradoRepository.crear(grado)
        grado_encontrado = GradoRepository.buscar_por_id(grado.id)
        self.assertIsNotNone(grado_encontrado)
        self.assertEqual(grado_encontrado.nombre, "Licenciatura")

    def test_buscar_grados(self):
        grado1 = self.__nuevoGrado()
        grado2 = self.__nuevoGrado("Maestría")
        GradoRepository.crear(grado1)
        GradoRepository.crear(grado2)
        grados = GradoRepository.buscar_todos()
        self.assertIsNotNone(grados)
        self.assertEqual(len(grados), 2)

    def test_actualizar_grado(self):
        grado = self.__nuevoGrado()
        GradoRepository.crear(grado)
        grado.nombre = "Doctorado"
        grado_actualizado = GradoRepository.actualizar(grado)
        self.assertEqual(grado_actualizado.nombre, "Doctorado")

    def test_borrar_grado(self):
        grado = self.__nuevoGrado()
        GradoRepository.crear(grado)
        resultado = GradoRepository.borrar_por_id(grado.id)
        self.assertIsNotNone(resultado)
        grado_borrado = GradoRepository.buscar_por_id(grado.id)
        self.assertIsNone(grado_borrado)

    def __nuevoGrado(self, nombre="Licenciatura"):
        grado = Grado()
        grado.nombre = nombre
        return grado


if __name__ == "__main__":
    unittest.main()
