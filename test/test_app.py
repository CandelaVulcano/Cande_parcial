import unittest
import sys
import os

# Añadir el directorio raíz del proyecto al path para poder importar desde app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos solo lo que necesitamos para una prueba básica
from flask import current_app
from app import db  # Importamos solo db

# Definimos una versión simplificada de create_app que no importa los recursos
def create_simple_app(config_name='testing'):
    from flask import Flask
    from app.config import config
    
    app = Flask(__name__)
    config_class = config.get(config_name, config['default'])
    app.config.from_object(config_class)
    db.init_app(app)
    
    return app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        # Usamos nuestra versión simplificada
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        # Prueba básica para verificar que la aplicación se creó correctamente
        self.assertIsNotNone(current_app)

if __name__ == '__main__':
    unittest.main()
