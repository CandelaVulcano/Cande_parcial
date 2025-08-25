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
from app.models.plan import Plan
from app.models.orientacion import Orientacion
from app.repositories.plan_repositorio import PlanRepository
from app.repositories.orientacion_repositorio import OrientacionRepository
from app import db

class PlanTestCase(unittest.TestCase):
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

    def test_plan_creation(self):
        plan = self.__nuevoPlan()
        self.assertIsNotNone(plan)
        self.assertEqual(plan.nombre, "Plan 2023")
        self.assertEqual(plan.fecha_inicio, "2023-01-01")
        self.assertEqual(plan.fecha_fin, "2027-12-31")
        self.assertEqual(plan.observacion, "Plan de estudios actualizado")

    def test_crear_plan(self):
        plan = self.__nuevoPlan()
        PlanRepository.crear(plan)
        self.assertIsNotNone(plan)
        self.assertIsNotNone(plan.id)
        self.assertGreaterEqual(plan.id, 1)
        self.assertEqual(plan.nombre, "Plan 2023")

    def test_plan_busqueda(self):
        plan = self.__nuevoPlan()
        PlanRepository.crear(plan)
        plan_encontrado = PlanRepository.buscar_por_id(plan.id)
        self.assertIsNotNone(plan_encontrado)
        self.assertEqual(plan_encontrado.nombre, "Plan 2023")

    def test_buscar_planes(self):
        plan1 = self.__nuevoPlan()
        plan2 = self.__nuevoPlan("Plan 2024")
        PlanRepository.crear(plan1)
        PlanRepository.crear(plan2)
        planes = PlanRepository.buscar_todos()
        self.assertIsNotNone(planes)
        self.assertEqual(len(planes), 2)

    def test_actualizar_plan(self):
        plan = self.__nuevoPlan()
        PlanRepository.crear(plan)
        plan.nombre = "Plan Modificado"
        plan.observacion = "Observación actualizada"
        plan_actualizado = PlanRepository.actualizar(plan)
        self.assertEqual(plan_actualizado.nombre, "Plan Modificado")
        self.assertEqual(plan_actualizado.observacion,
                         "Observación actualizada")

    def test_borrar_plan(self):
        plan = self.__nuevoPlan()
        PlanRepository.crear(plan)
        PlanRepository.borrar_por_id(plan.id)
        plan_borrado = PlanRepository.buscar_por_id(plan.id)
        self.assertIsNone(plan_borrado)

    def test_plan_con_orientacion(self):
        from app.models.universidad import Universidad
        from app.models.facultad import Facultad
        from app.models.departamento import Departamento
        from app.models.tipo_especialidad import TipoEspecialidad
        from app.models.especialidad import Especialidad
        from app.models.materia import Materia
        
        universidad = Universidad()
        universidad.nombre = "Universidad de Prueba"
        universidad.sigla = "UP"
        db.session.add(universidad)
        db.session.commit()
        
        facultad = Facultad()
        facultad.nombre = "Facultad de Prueba"
        facultad.abreviatura = "FP"
        facultad.directorio = "dir_prueba"
        facultad.sigla = "FDP"
        facultad.email = "facultad@test.com"
        facultad.universidad_id = universidad.id
        db.session.add(facultad)
        db.session.commit()
        
        departamento = Departamento()
        departamento.nombre = "Departamento de Prueba"
        departamento.facultad_id = facultad.id
        db.session.add(departamento)
        db.session.commit()
        
        materia = Materia()
        materia.nombre = "Materia de Prueba"
        materia.codigo = "MP001"
        materia.departamento_id = departamento.id
        db.session.add(materia)
        db.session.commit()
        
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = "Tipo Especialidad de Prueba"
        tipo_especialidad.nivel = "Nivel de Prueba"
        db.session.add(tipo_especialidad)
        db.session.commit()
        
        especialidad = Especialidad()
        especialidad.nombre = "Especialidad de Prueba"
        especialidad.tipo_especialidad_id = tipo_especialidad.id
        db.session.add(especialidad)
        db.session.commit()
        
        orientacion = Orientacion()
        orientacion.nombre = "Orientación de Prueba"
        orientacion.especialidad_id = especialidad.id
        orientacion.plan_id = 1 
        orientacion.materia_id = materia.id
        OrientacionRepository.crear(orientacion)

        plan = self.__nuevoPlan()
        PlanRepository.crear(plan)
        
        orientacion.plan_id = plan.id
        OrientacionRepository.actualizar(orientacion)

        plan_encontrado = PlanRepository.buscar_por_id(plan.id)
        self.assertIsNotNone(plan_encontrado)

    def __nuevoPlan(self, nombre="Plan 2023"):
        plan = Plan()
        plan.nombre = nombre
        plan.fecha_inicio = "2023-01-01"
        plan.fecha_fin = "2027-12-31"
        plan.observacion = "Plan de estudios actualizado"
        return plan

if __name__ == "__main__":
    unittest.main()