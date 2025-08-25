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
from app.models.tipo_documento import TipoDocumento
from app.repositories.tipo_documento_repositorio import TipoDocumentoRepositorio
from app import db

class TipoDocTestCase(unittest.TestCase):
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

    def test_crear_tipo_documento(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        TipoDocumentoRepositorio.crear(tipo_doc)
        self.assertIsNotNone(tipo_doc.id)
        tipo_doc_db = TipoDocumentoRepositorio.buscar_por_id(tipo_doc.id)
        self.assertEqual(tipo_doc_db.nombre, tipo_doc.nombre)

    def test_buscar_todos(self):
        tipo_doc1 = TipoDocumento(nombre="DNI")
        tipo_doc2 = TipoDocumento(nombre="Pasaporte")
        TipoDocumentoRepositorio.crear(tipo_doc1)
        TipoDocumentoRepositorio.crear(tipo_doc2)

        tipos_docs = TipoDocumentoRepositorio.buscar_todos()
        self.assertGreaterEqual(len(tipos_docs), 2)
        self.assertIn(tipo_doc1, tipos_docs)
        self.assertIn(tipo_doc2, tipos_docs)

    def test_buscar_documento_id(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        TipoDocumentoRepositorio.crear(tipo_doc)
        tipo_doc_db = TipoDocumentoRepositorio.buscar_por_id(tipo_doc.id)
        self.assertIsNotNone(tipo_doc_db)
        self.assertEqual(tipo_doc_db.nombre, tipo_doc.nombre)

    def test_actualizar_tipo_documento(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        TipoDocumentoRepositorio.crear(tipo_doc)
        tipo_doc.nombre = "DNI Actualizado"
        TipoDocumentoRepositorio.actualizar(tipo_doc)

        tipo_doc_db = TipoDocumentoRepositorio.buscar_por_id(tipo_doc.id)
        self.assertEqual(tipo_doc_db.nombre, "DNI Actualizado")

    def test_borrar_tipo_documento(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        TipoDocumentoRepositorio.crear(tipo_doc)
        TipoDocumentoRepositorio.borrar_por_id(tipo_doc.id)

        tipo_doc_db = TipoDocumentoRepositorio.buscar_por_id(tipo_doc.id)
        self.assertIsNone(tipo_doc_db)