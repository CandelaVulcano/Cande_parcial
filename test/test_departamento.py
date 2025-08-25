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

from app.models.departamento import Departamento
from app.models.facultad import Facultad
from app.models.universidad import Universidad

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.universidad = Universidad()
        self.universidad.nombre = "Universidad Nacional de Prueba"
        self.universidad.sigla = "UNP"
        db.session.add(self.universidad)
        db.session.commit()
        
        self.facultad = Facultad()
        self.facultad.nombre = "Facultad de Pruebas"
        self.facultad.abreviatura = "FP"
        self.facultad.directorio = "pruebas"
        self.facultad.sigla = "FP"
        self.facultad.email = "fp@unp.edu.ar"
        self.facultad.universidad_id = self.universidad.id
        db.session.add(self.facultad)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_departamento_creation(self):
        departamento = Departamento()
        departamento.nombre = "Secretaria"
        departamento.descripcion = "Secretaria de la empresa"
        departamento.facultad_id = self.facultad.id 
        db.session.add(departamento)
        db.session.commit()
        self.assertIsNotNone(departamento) 
        self.assertEqual(departamento.nombre, "Secretaria") 
        self.assertIsNotNone(departamento.nombre)
        self.assertEqual(departamento.descripcion, "Secretaria de la empresa") 
        self.assertIsNotNone(departamento.descripcion) 
        self.assertIsInstance(departamento.id, int)
        self.assertGreater(departamento.id, 0)
    
    def test_crear_departamento(self):
        departamento = Departamento()
        departamento.nombre = "oficina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        departamento.facultad_id = self.facultad.id 
        db.session.add(departamento)
        db.session.commit()
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.id)
        self.assertGreaterEqual(departamento.id, 1)
        self.assertEqual(departamento.nombre, "oficina de alumnos")
    
    def test_buscar_por_id(self):
        departamento = Departamento()
        departamento.nombre = "oficina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        departamento.facultad_id = self.facultad.id 
        db.session.add(departamento)
        db.session.commit()
        encontrado = Departamento.query.get(departamento.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "oficina de alumnos")

    def test_buscar_todos(self):
        departamento1 = Departamento()
        departamento1.nombre = "oficina de alumnos"
        departamento1.descripcion = "oficina de alumnos de la facultad de ingenieria"
        departamento1.facultad_id = self.facultad.id  
        db.session.add(departamento1)
        
        departamento2 = Departamento()
        departamento2.nombre = "oficina de profesores"
        departamento2.descripcion = "oficina de profesores de la facultad de ingenieria"
        departamento2.facultad_id = self.facultad.id 
        db.session.add(departamento2)
        
        db.session.commit()
        
        departamentos = Departamento.query.all()
        self.assertEqual(len(departamentos), 2)
        self.assertIn(departamento1, departamentos)
        self.assertIn(departamento2, departamentos)

    def test_actualizar_departamento(self):
        departamento = Departamento()
        departamento.nombre = "oficina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        departamento.facultad_id = self.facultad.id  
        db.session.add(departamento)
        db.session.commit()
        
        departamento.nombre = "oficina de alumnos"
        db.session.commit()
        
        actualizado = Departamento.query.get(departamento.id)
        self.assertEqual(actualizado.nombre, "oficina de alumnos")

    def test_borrar_departamento(self):
        departamento = Departamento()
        departamento.nombre = "oficina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        departamento.facultad_id = self.facultad.id 
        db.session.add(departamento)
        db.session.commit()
        
        db.session.delete(departamento)
        db.session.commit()
        
        encontrado = Departamento.query.get(departamento.id)
        self.assertIsNone(encontrado)
    
    def __nuevoDepartamento(self):
        departamento = Departamento()
        departamento.nombre = "oficina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        departamento.facultad_id = self.facultad.id
        return departamento

    def __nuevoDepartamento2(self):
        departamento2 = Departamento()
        departamento2.nombre = "oficina de profesores"
        departamento2.descripcion = "oficina de profesores de la facultad de ingenieria"
        departamento2.facultad_id = self.facultad.id
        return departamento2
    
    def __nuevoDepartamento3(self):
        departamento3 = Departamento()
        departamento3.nombre = "oficina de administracion"
        departamento3.descripcion = "oficina de administracion de la facultad de ingenieria"
        departamento3.facultad_id = self.facultad.id
        return departamento3

if __name__ == '__main__':
    unittest.main()