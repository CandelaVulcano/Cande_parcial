import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.alumno import Alumno
from app.services.alumno_service import AlumnoService
from app.repositories.alumno_repositorio import AlumnoRepository

from metodos_de_prueba import crear_alumno, crear_tipo_documento

class AlumnoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.tipo_documento_dni = crear_tipo_documento(nombre="DNI")
        db.session.add(self.tipo_documento_dni)
        db.session.commit()
        self.tipo_documento_dni_id = self.tipo_documento_dni.id

        self.tipo_documento_pasaporte = crear_tipo_documento(nombre="Pasaporte")
        db.session.add(self.tipo_documento_pasaporte)
        db.session.commit()
        self.tipo_documento_pasaporte_id = self.tipo_documento_pasaporte.id

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_creacion_instancia_alumno(self):
        """Verifica que se puede crear una instancia de Alumno correctamente."""
        alumno = crear_alumno(
            apellido="Perez",
            nombre="Juan",
            nro_documento="12345678",
            tipo_documento_id=self.tipo_documento_dni_id,
            sexo="M"
        )
        self.assertIsNotNone(alumno)
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Perez")
        self.assertEqual(alumno.nro_documento, "12345678")
        self.assertEqual(alumno.tipo_documento_id, self.tipo_documento_dni_id)
        self.assertEqual(alumno.sexo, "M")

    def test_crear_alumno_persistencia(self):
        """Verifica que un alumno puede ser creado y persistido en la DB."""
        alumno = crear_alumno(
            apellido="Gomez",
            nombre="Maria",
            nro_documento="87654321",
            tipo_documento_id=self.tipo_documento_pasaporte_id,
            sexo="F"
        )
        alumno_creado = AlumnoRepository.crear(alumno)

        self.assertIsNotNone(alumno_creado.id)
        self.assertEqual(alumno_creado.nombre, "Maria")

        alumno_recuperado = AlumnoRepository.buscar_por_id(alumno_creado.id)
        self.assertIsNotNone(alumno_recuperado)
        self.assertEqual(alumno_recuperado.nombre, "Maria")
        self.assertEqual(alumno_recuperado.tipo_documento_id, self.tipo_documento_pasaporte_id)

    def test_buscar_todos_alumnos(self):
        """Verifica que se pueden buscar todos los alumnos."""
        alumno1 = crear_alumno(nombre="Ana", apellido="Lopez", nro_documento="111", tipo_documento_id=self.tipo_documento_dni_id)
        alumno2 = crear_alumno(nombre="Pedro", apellido="Diaz", nro_documento="222", tipo_documento_id=self.tipo_documento_dni_id)
        
        AlumnoRepository.crear(alumno1)
        AlumnoRepository.crear(alumno2)

        alumnos = AlumnoRepository.buscar_todos()
        self.assertEqual(len(alumnos), 2)
        self.assertIn(alumno1, alumnos)
        self.assertIn(alumno2, alumnos)

    def test_actualizar_alumno(self):
        """Verifica que un alumno puede ser actualizado."""
        alumno = crear_alumno(nombre="Original", apellido="Apellido", nro_documento="333", tipo_documento_id=self.tipo_documento_dni_id)
        AlumnoRepository.crear(alumno)

        alumno.nombre = "Actualizado"
        alumno.sexo = "F"
        alumno_actualizado = AlumnoRepository.actualizar(alumno)

        self.assertEqual(alumno_actualizado.nombre, "Actualizado")
        self.assertEqual(alumno_actualizado.sexo, "F")
        
        alumno_recuperado = AlumnoRepository.buscar_por_id(alumno.id)
        self.assertEqual(alumno_recuperado.nombre, "Actualizado")
        self.assertEqual(alumno_recuperado.sexo, "F")

    def test_borrar_alumno(self):
        """Verifica que un alumno puede ser borrado."""
        alumno = crear_alumno(nombre="ParaBorrar", apellido="Apellido", nro_documento="444", tipo_documento_id=self.tipo_documento_dni_id)
        AlumnoRepository.crear(alumno)
        alumno_id = alumno.id

        eliminado = AlumnoRepository.borrar_por_id(alumno_id)
        self.assertIsNotNone(eliminado)

        alumno_recuperado = AlumnoRepository.buscar_por_id(alumno_id)
        self.assertIsNone(alumno_recuperado)

if __name__ == '__main__':
    unittest.main()
