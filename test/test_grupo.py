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

from app.models.grupo import Grupo
from app.repositories.grupo_repositorio import GrupoRepository
from app import db

class AppTestCase(unittest.TestCase):

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
    
    def test_grupo_creation(self):
        grupo = self.__nuevoGrupo()
        self.assertIsNotNone(grupo)
        self.assertEqual(grupo.nombre, "Grupo1")
        self.assertIsNotNone(grupo.nombre) 

    def test_crear_grupo(self):
        grupo = self.__nuevoGrupo()
        GrupoRepository.crear(grupo)
        self.assertIsNotNone(grupo)
        self.assertIsNotNone(grupo.id)
        self.assertGreaterEqual(grupo.id, 1)
        self.assertEqual(grupo.nombre, "Grupo1")
        
    def test_grupo_busqueda(self):
        grupo = self.__nuevoGrupo()
        GrupoRepository.crear(grupo)
        grupo_encontrado = GrupoRepository.buscar_por_id(grupo.id)
        self.assertIsNotNone(grupo_encontrado)
        self.assertEqual(grupo_encontrado.nombre, "Grupo1")
    
    def test_buscar_grupos(self):
        grupo1 = self.__nuevoGrupo()
        grupo2 = self.__nuevoGrupo()
        GrupoRepository.crear(grupo1)
        GrupoRepository.crear(grupo2)
        grupos = GrupoRepository.buscar_todos()
        self.assertIsNotNone(grupos)
        self.assertEqual(len(grupos), 2)
        
    def test_actualizar_grupo(self):
        grupo = self.__nuevoGrupo()
        GrupoRepository.crear(grupo)
        grupo.nombre = "Grupo2"
        grupo_actualizado = GrupoRepository.actualizar(grupo)
        self.assertEqual(grupo_actualizado.nombre, "Grupo2")
        
    def test_borrar_grupo(self):
        grupo = self.__nuevoGrupo()
        GrupoRepository.crear(grupo)
        GrupoRepository.borrar_por_id(grupo.id)
        grupo_borrado = GrupoRepository.buscar_por_id(grupo.id)
        self.assertIsNone(grupo_borrado)

    def __nuevoGrupo(self):
        grupo = Grupo()
        grupo.nombre = "Grupo1"
        return grupo 
    
if __name__ == '__main__':
    unittest.main()