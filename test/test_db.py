import os
import sys
import unittest
from sqlalchemy import text

# Añadir el directorio raíz del proyecto al path para poder importar desde app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db

# Definimos una versión simplificada de create_app que no importa los recursos
def create_simple_app(config_name='testing'):
    from flask import Flask
    from app.config import config
    
    app = Flask(__name__)
    config_class = config.get(config_name, config['default'])
    app.config.from_object(config_class)
    db.init_app(app)
    
    return app


class ConnectionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # test connection to db
    def test_db_connection(self):
        result = db.session.query(text("'Hello world'")).one()
        self.assertEqual(result[0], 'Hello world')
    
if __name__ == '__main__':
    unittest.main()
