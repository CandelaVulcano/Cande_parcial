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

from app.models.facultad import Facultad
from app.repositories.facultad_repositorio import FacultadRepository
from app.models.universidad import Universidad
from app import db

class FacultadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.universidad = Universidad()
        self.universidad.nombre = "Universidad de Prueba"
        self.universidad.sigla = "UP"
        db.session.add(self.universidad)
        db.session.commit()

    def tearDown(self): 
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_facultad_creation(self):
        facultad = self.__nuevaFacultad()
        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias Exactas")
        self.assertEqual(facultad.abreviatura, "FCE")
        
    def test_crear_facultad(self):
        facultad = self.__nuevaFacultad()
        FacultadRepository.crear(facultad)
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.id)
        self.assertGreaterEqual(facultad.id, 1)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias Exactas")
        
    def test_facultad_busqueda(self):
        facultad = self.__nuevaFacultad()
        FacultadRepository.crear(facultad)
        encontrada = FacultadRepository.buscar_por_id(facultad.id)
        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada.nombre, "Facultad de Ciencias Exactas")
        self.assertEqual(encontrada.abreviatura, "FCE")
    
    def test_buscar_facultades(self):
        facultad1 = self.__nuevaFacultad()
        facultad2 = self.__nuevaFacultad()
        FacultadRepository.crear(facultad1)
        FacultadRepository.crear(facultad2)
        facultades = FacultadRepository.buscar_todos()
        self.assertIsNotNone(facultades)
        self.assertEqual(len(facultades), 2)
        
    def test_actualizar_facultad(self):
        facultad = self.__nuevaFacultad()
        FacultadRepository.crear(facultad)
        facultad.nombre = "Facultad de Ciencias Naturales"
        facultad_actualizada = FacultadRepository.actualizar_facultad(facultad)
        self.assertEqual(facultad_actualizada.nombre, "Facultad de Ciencias Naturales")
        
    def test_borrar_facultad(self):
        facultad = self.__nuevaFacultad()
        FacultadRepository.crear(facultad)
        FacultadRepository.borrar_por_id(facultad.id)
        facultad_borrada = FacultadRepository.buscar_por_id(facultad.id)
        self.assertIsNone(facultad_borrada)
        
    def __nuevaFacultad(self):
        facultad=Facultad()
        facultad.nombre = "Facultad de Ciencias Exactas"
        facultad.abreviatura = "FCE"
        facultad.directorio = "Ciencias Exactas"
        facultad.sigla = "FCE"
        facultad.codigo_postal = "12345"
        facultad.ciudad = "La Plata"
        facultad.domicilio = "Calle 123"
        facultad.telefono = "123456789"
        facultad.contacto = "Juan Perez"
        facultad.email ="abc@gmail.com"
        facultad.universidad_id = self.universidad.id
        return facultad

if __name__ == "__main__":
    unittest.main()
    