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

from app.models.orientacion import Orientacion
from app.repositories.orientacion_repositorio import OrientacionRepository
from app.models.tipo_especialidad import TipoEspecialidad
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.departamento import Departamento
from app.models.materia import Materia
from app.models.facultad import Facultad
from app import db

class AppTestCase(unittest.TestCase): 

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_simple_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        from app.models.universidad import Universidad
        self.universidad = Universidad()
        self.universidad.nombre = "Universidad de Prueba"
        self.universidad.sigla = "UP"
        db.session.add(self.universidad)
        db.session.commit()
        
        self.facultad = Facultad()
        self.facultad.nombre = "Facultad de Prueba"
        self.facultad.abreviatura = "FP"
        self.facultad.directorio = "dir_prueba"
        self.facultad.sigla = "FDP"
        self.facultad.email = "facultad@test.com"
        self.facultad.universidad_id = self.universidad.id
        db.session.add(self.facultad)
        db.session.commit()
        
        self.departamento = Departamento()
        self.departamento.nombre = "Departamento de Prueba"
        self.departamento.facultad_id = self.facultad.id
        db.session.add(self.departamento)
        db.session.commit()
        
        self.materia = Materia()
        self.materia.nombre = "Materia de Prueba"
        self.materia.codigo = "MP001"
        self.materia.departamento_id = self.departamento.id
        db.session.add(self.materia)
        db.session.commit()
        
        self.plan = Plan()
        self.plan.nombre = "Plan de Prueba"
        self.plan.fecha_inicio = "2023-01-01"
        db.session.add(self.plan)
        db.session.commit()
        
        self.tipo_especialidad = TipoEspecialidad()
        self.tipo_especialidad.nombre = "Tipo Especialidad de Prueba"
        self.tipo_especialidad.nivel = "Nivel de Prueba"
        db.session.add(self.tipo_especialidad)
        db.session.commit()
        
        self.especialidad = Especialidad()
        self.especialidad.nombre = "Especialidad de Prueba"
        self.especialidad.tipo_especialidad_id = self.tipo_especialidad.id
        db.session.add(self.especialidad)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_orientacion_creation(self):
        orientacion = self.__nuevoOrientacion()
        self.assertIsNotNone(orientacion)
        self.assertEqual(orientacion.nombre, "Orientacion1")
        self.assertIsNotNone(orientacion.nombre)

    def test_crear_orientacion(self):
        orientacion = self.__nuevoOrientacion()
        OrientacionRepository.crear(orientacion)
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.id)
        self.assertGreaterEqual(orientacion.id, 1)
        self.assertEqual(orientacion.nombre, "Orientacion1")

    def test_orientacion_busqueda(self):
        orientacion = self.__nuevoOrientacion()
        OrientacionRepository.crear(orientacion)
        orientacion_encontrada = OrientacionRepository.buscar_por_id(orientacion.id)
        self.assertIsNotNone(orientacion_encontrada)
        self.assertEqual(orientacion_encontrada.nombre, "Orientacion1")
    
    def test_buscar_orientaciones(self):
        orientacion1 = self.__nuevoOrientacion()
        orientacion2 = self.__nuevoOrientacion()
        OrientacionRepository.crear(orientacion1)
        OrientacionRepository.crear(orientacion2)
        orientaciones = OrientacionRepository.buscar_todos()
        self.assertIsNotNone(orientaciones)
        self.assertEqual(len(orientaciones), 2)
        
    def test_actualizar_orientacion(self):
        orientacion = self.__nuevoOrientacion()
        OrientacionRepository.crear(orientacion)
        orientacion.nombre = "Orientacion2"
        orientacion_actualizada = OrientacionRepository.actualizar(orientacion)
        self.assertEqual(orientacion_actualizada.nombre, "Orientacion2")

    def test_borrar_orientacion(self):
        orientacion = self.__nuevoOrientacion()
        OrientacionRepository.crear(orientacion)
        OrientacionRepository.borrar_por_id(orientacion.id)
        orientacion_borrada = OrientacionRepository.buscar_por_id(orientacion.id)
        self.assertIsNone(orientacion_borrada)


    def __nuevoOrientacion(self):
        orientacion = Orientacion()
        orientacion.nombre = "Orientacion1"
        orientacion.especialidad_id = self.especialidad.id
        orientacion.plan_id = self.plan.id
        orientacion.materia_id = self.materia.id
        return orientacion    
        