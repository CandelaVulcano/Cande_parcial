import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import current_app
from app import db

def create_simple_app(config_name='testing'):
    from flask import Flask
    from app.config import config
    
    app = Flask(__name__)
    config_class = config.get(config_name, config['default'])
    app.config.from_object(config_class)
    db.init_app(app)
    
    return app

from app.models.especialidad import Especialidad
from app.models.tipo_especialidad import TipoEspecialidad
from app.repositories.especialidad_repositorio import EspecialidadRepository

def nuevaEspecialidad(tipo_especialidad_id=None):
    especialidad = Especialidad()
    especialidad.nombre = "Especialidad 1"
    especialidad.observacion = "Observacion 1"
    especialidad.letra = "a"
    especialidad.tipo_especialidad_id = tipo_especialidad_id
    return especialidad

def nuevaEspecialidad2(tipo_especialidad_id=None):
    especialidad = Especialidad()
    especialidad.nombre = "Especialidad 2"
    especialidad.observacion = "Observacion 2"
    especialidad.letra = "b"
    especialidad.tipo_especialidad_id = tipo_especialidad_id
    return especialidad


class EspecialidadTestCase (unittest.TestCase):
    def setUp(self):
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.tipo_especialidad = TipoEspecialidad()
        self.tipo_especialidad.nombre = "Tipo de Especialidad de Prueba"
        self.tipo_especialidad.nivel = "Nivel de Prueba"
        db.session.add(self.tipo_especialidad)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_especialidad(self):
        especialidad = nuevaEspecialidad(self.tipo_especialidad.id)
        EspecialidadRepository.crear(especialidad)
        self._assert_especialidad(
            especialidad, "Especialidad 1", "Observacion 1", "a")

    def test_buscar_por_id(self):
        especialidad = nuevaEspecialidad(self.tipo_especialidad.id)
        EspecialidadRepository.crear(especialidad)
        encontrada = EspecialidadRepository.buscar_por_id(especialidad.id)
        self._assert_especialidad(
            encontrada, "Especialidad 1", "Observacion 1", "a")

    def test_buscar_todos(self):
        especialidad1 = nuevaEspecialidad(self.tipo_especialidad.id)
        especialidad2 = nuevaEspecialidad2(self.tipo_especialidad.id)
        EspecialidadRepository.crear(especialidad1)
        EspecialidadRepository.crear(especialidad2)
        especialidades = EspecialidadRepository.buscar_todos()
        self.assertIsNotNone(especialidades)
        self.assertEqual(len(especialidades), 2)

    def test_actualizar_especialidad(self):
        especialidad = nuevaEspecialidad(self.tipo_especialidad.id)
        EspecialidadRepository.crear(especialidad)
        especialidad.nombre = "Especialidad Actualizada"
        especialidad.letra = "z"
        especialidad.observacion = "Observacion Actualizada"
        EspecialidadRepository.actualizar(especialidad)
        encontrada = EspecialidadRepository.buscar_por_id(especialidad.id)
        self._assert_especialidad(
            encontrada, "Especialidad Actualizada", "Observacion Actualizada", "z")

    def test_borrar_especialidad(self):
        especialidad = nuevaEspecialidad(self.tipo_especialidad.id)
        EspecialidadRepository.crear(especialidad)
        EspecialidadRepository.borrar_por_id(especialidad.id)
        encontrada = EspecialidadRepository.buscar_por_id(especialidad.id)
        self.assertIsNone(encontrada)

    def _assert_especialidad(self, especialidad, nombre, observacion, letra):
        self.assertIsNotNone(especialidad)
        self.assertIsNotNone(especialidad.id)
        self.assertGreaterEqual(especialidad.id, 1)
        self.assertEqual(especialidad.nombre, nombre)
        self.assertEqual(especialidad.observacion, observacion)
        self.assertEqual(especialidad.letra, letra)


if __name__ == '__main__':
    unittest.main()
