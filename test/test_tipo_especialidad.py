import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_simple_app(config_name='testing'):
    from flask import Flask
    from app.config import config
    
    app = Flask(__name__)
    config_class = config.get(config_name, config['default'])
    app.config.from_object(config_class)
    from app import db
    db.init_app(app)
    
    return app

from flask import current_app
from app.models.tipo_especialidad import TipoEspecialidad
from app.repositories.tipo_especialidad_repositorio import TipoEspecialidadRepositorio
from app import db


class TipoEspecialidadCase(unittest.TestCase):
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

    def test_tipo_especialidad_creation(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        self.assertIsNotNone(tipo_especialidad)
        self.assertEqual(tipo_especialidad.nombre, "Cardiología")
        self.assertEqual(tipo_especialidad.nivel, "Básico")

    def test_crear_tipo_especialidad(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        TipoEspecialidadRepositorio.crear(tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad.id)
        self.assertGreaterEqual(tipo_especialidad.id, 1)
        self.assertEqual(tipo_especialidad.nombre, "Cardiología")
        self.assertEqual(tipo_especialidad.nivel, "Básico")

    def test_tipo_especialidad_busqueda(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        TipoEspecialidadRepositorio.crear(tipo_especialidad)
        encontrado = TipoEspecialidadRepositorio.buscar_por_id(
            tipo_especialidad.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Cardiología")
        self.assertEqual(encontrado.nivel, "Básico")

    def test_buscar_tipos_especialidad(self):
        tipo_especialidad1 = self.__nuevoTipoEspecialidad("Cardiología")
        tipo_especialidad2 = self.__nuevoTipoEspecialidad("Neurología")
        TipoEspecialidadRepositorio.crear(tipo_especialidad1)
        TipoEspecialidadRepositorio.crear(tipo_especialidad2)
        tipos_especialidad = TipoEspecialidadRepositorio.buscar_todos()
        self.assertIsNotNone(tipos_especialidad)
        self.assertEqual(len(tipos_especialidad), 2)

    def test_actualizar_tipo_especialidad(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        TipoEspecialidadRepositorio.crear(tipo_especialidad)
        tipo_especialidad.nombre = "Cardiología Avanzada"
        tipo_especialidad.nivel = "Avanzado"
        tipo_especialidad_actualizado = TipoEspecialidadRepositorio.actualizar(
            tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad_actualizado)

    def test_borrar_tipo_especialidad(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        TipoEspecialidadRepositorio.crear(tipo_especialidad)

        borrado = TipoEspecialidadRepositorio.borrar_por_id(tipo_especialidad.id)
        self.assertIsNotNone(borrado)
        self.assertEqual(borrado.nombre, "Cardiología")
        self.assertEqual(borrado.nivel, "Básico")

        tipo_especialidad_borrado = TipoEspecialidadRepositorio.buscar_por_id(
            tipo_especialidad.id)
        self.assertIsNone(tipo_especialidad_borrado)

    def __nuevoTipoEspecialidad(self, nombre="Cardiología"):
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = nombre
        tipo_especialidad.nivel = "Básico"
        return tipo_especialidad


if __name__ == '__main__':
    unittest.main()