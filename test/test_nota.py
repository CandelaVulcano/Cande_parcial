import os
import sys
import unittest
from unittest.mock import Mock, patch

# Añadir el directorio raíz del proyecto al path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.nota import Nota
from app.repositories.nota_repositorio import NotaRepository

class NotaTestCase(unittest.TestCase):

    @patch('app.repositories.nota_repositorio.db')
    def test_crear_nota(self, mock_db):
        # Configurar el mock
        nota = Nota()
        nota.valor = 8
        nota.inscripcion_id = 1
        mock_db.session.commit = Mock()
        
        # Ejecutar el método bajo prueba
        repo = NotaRepository()
        resultado = repo.crear(nota)
        
        # Verificar que se llamó a db.session.add con la nota
        mock_db.session.add.assert_called_once_with(nota)
        # Verificar que se llamó a db.session.commit
        mock_db.session.commit.assert_called_once()
        # Verificar que se devolvió la misma nota
        self.assertEqual(resultado, nota)

    @patch('app.repositories.nota_repositorio.db')
    def test_buscar_por_id(self, mock_db):
        # Configurar el mock
        nota = Nota()
        nota.id = 1
        nota.valor = 8
        nota.inscripcion_id = 1
        mock_db.session.query().filter_by().first.return_value = nota
        
        # Ejecutar el método bajo prueba
        repo = NotaRepository()
        resultado = repo.buscar_por_id(1)
        
        # Verificar que se llamó a db.session.query (no importa cuántas veces)
        mock_db.session.query.assert_called()
        # Verificar que se devolvió la nota esperada
        self.assertEqual(resultado.id, 1)
        self.assertEqual(resultado.valor, 8)
        self.assertEqual(resultado.inscripcion_id, 1)

    @patch('app.repositories.nota_repositorio.db')
    def test_buscar_todos(self, mock_db):
        # Configurar el mock
        nota1 = Nota()
        nota1.id = 1
        nota1.valor = 8
        nota1.inscripcion_id = 1
        
        nota2 = Nota()
        nota2.id = 2
        nota2.valor = 9
        nota2.inscripcion_id = 1
        
        mock_db.session.query().all.return_value = [nota1, nota2]
        
        # Ejecutar el método bajo prueba
        repo = NotaRepository()
        resultado = repo.buscar_todos()
        
        # Verificar que se llamó a db.session.query (no importa cuántas veces)
        mock_db.session.query.assert_called()
        # Verificar que se devolvió la lista esperada
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0].valor, 8)
        self.assertEqual(resultado[1].valor, 9)

    @patch('app.repositories.nota_repositorio.db')
    def test_actualizar_nota(self, mock_db):
        # Configurar el mock
        nota = Nota()
        nota.id = 1
        nota.valor = 8
        nota.inscripcion_id = 1
        
        nota_actualizada = Nota()
        nota_actualizada.id = 1
        nota_actualizada.valor = 10
        nota_actualizada.inscripcion_id = 1
        
        mock_db.session.merge.return_value = nota_actualizada
        mock_db.session.commit = Mock()
        
        # Ejecutar el método bajo prueba
        repo = NotaRepository()
        resultado = repo.actualizar(nota)
        
        # Verificar que se llamó a db.session.merge con la nota
        mock_db.session.merge.assert_called_once_with(nota)
        # Verificar que se llamó a db.session.commit
        mock_db.session.commit.assert_called_once()
        # Verificar que se devolvió la nota actualizada
        self.assertEqual(resultado.id, 1)
        self.assertEqual(resultado.valor, 10)
        self.assertEqual(resultado.inscripcion_id, 1)

    @patch('app.repositories.nota_repositorio.db')
    def test_borrar_nota(self, mock_db):
        # Configurar el mock
        nota = Nota()
        nota.id = 1
        nota.valor = 8
        nota.inscripcion_id = 1
        
        mock_db.session.query().filter_by().first.return_value = nota
        mock_db.session.delete = Mock()
        mock_db.session.commit = Mock()
        
        # Ejecutar el método bajo prueba
        repo = NotaRepository()
        resultado = repo.borrar_por_id(1)
        
        # Verificar que se llamó a db.session.delete con la nota
        mock_db.session.delete.assert_called_once_with(nota)
        # Verificar que se llamó a db.session.commit
        mock_db.session.commit.assert_called_once()
        # Verificar que se devolvió la nota eliminada
        self.assertEqual(resultado, nota)

    def test_validacion_nota(self):
        # Nota válida
        nota_valida = Nota()
        nota_valida.valor = 8
        nota_valida.inscripcion_id = 1
        self.assertEqual(nota_valida.valor, 8)
        
        # Nota sin valor (puede ser None según el modelo)
        nota_sin_valor = Nota()
        nota_sin_valor.inscripcion_id = 1
        self.assertIsNone(nota_sin_valor.valor)
        
        # Nota con valor fuera de rango (la validación se implementa en el servicio o controlador)
        nota_valor_invalido = Nota()
        nota_valor_invalido.valor = 15
        nota_valor_invalido.inscripcion_id = 1
        # Aquí solo verificamos que el modelo acepte el valor
        # La validación real debería ocurrir en el servicio o controlador
        self.assertEqual(nota_valor_invalido.valor, 15)


if __name__ == '__main__':
    unittest.main()
