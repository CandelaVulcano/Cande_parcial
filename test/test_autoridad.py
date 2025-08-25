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

from app.models.autoridad import Autoridad
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion

class AutoridadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
                
    def tearDown(self):
        self.app_context.pop()
        
    def test_autoridad_creation(self):
        autoridad = Autoridad()
        cargo = Cargo()
        tipo_dedicacion = TipoDedicacion()
        cargo.nombre= "Decano"
        cargo.puntos= 100
        self.__new_object(autoridad, cargo, tipo_dedicacion)
        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        self.assertIsNotNone(autoridad.cargo)
        self.assertEqual(autoridad.cargo.nombre, "Decano")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "abc@gmail.com")
        self.assertIsNotNone(autoridad.cargo.categoria_cargo)
        self.assertEqual(autoridad.cargo.categoria_cargo.nombre, "Categoria 1")

    def __new_object(self, autoridad, cargo, tipo_dedicacion):
        cargo.categoria_cargo= CategoriaCargo()
        cargo.categoria_cargo.nombre= "Categoria 1"
        cargo.tipo_dedicacion = tipo_dedicacion
        cargo.tipo_dedicacion.nombre = "Simple"
        cargo.tipo_dedicacion.observacion = "Observacion 1"
        autoridad.nombre = "Juan Perez"
        autoridad.cargo= cargo
        autoridad.telefono= "123456789"
        autoridad.email= "abc@gmail.com"
        
if __name__ == '__main__':
    unittest.main()
