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
from app.models.tipo_dedicacion import TipoDedicacion
from app import db

class TipoDedicacionTestCase(unittest.TestCase):
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
        
    def test_tipodedicacion_creation(self):
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre= "Simple"
        tipo_dedicacion.observacion = "Observacion 1"
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Simple")
        self.assertIsNotNone(tipo_dedicacion.observacion)
        self.assertEqual(tipo_dedicacion.observacion, "Observacion 1")
        
if __name__ == '__main__':
    unittest.main()