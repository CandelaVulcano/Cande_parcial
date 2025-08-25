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

from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo

class CargoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
        
    def test_autoridad_creation(self):
        cargo = Cargo()
        cargo.categoria_cargo= CategoriaCargo()
        cargo.categoria_cargo.nombre= "Categoria 1"
        cargo.nombre= "Decano"
        cargo.puntos= 100
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.categoria_cargo)
        self.assertEqual(cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertEqual(cargo.nombre, "Decano")
        self.assertEqual(cargo.puntos, 100)
        
if __name__ == '__main__':
    unittest.main()








