import os
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.nota import Nota
from app.repositories.nota_repositorio import NotaRepository

class NotaTestCase(unittest.TestCase):

    @patch('app.repositories.nota_repositorio.db')
    def test_crear_nota(self, mock_db):
        nota = Nota()
        nota.valor = 8
        nota.inscripcion_id = 1
        mock_db.session.commit = Mock()
        
        repo = NotaRepository()
        resultado = repo.crear(nota)
        
        mock_db.session.add.assert_called_once_with(nota)
        mock_db.session.commit.assert_called_once()
        self.assertEqual(resultado, nota)

    @patch('app.repositories.nota_repositorio.db')
    def test_buscar_por_id(self, mock_db):
        nota = Nota()
        nota.id = 1
        nota.valor = 8
        nota.inscripcion_id = 1
        mock_db.session.query().filter_by().first.return_value = nota
        
        repo = NotaRepository()
        resultado = repo.buscar_por_id(1)
        
        mock_db.session.query.assert_called()
        self.assertEqual(resultado.id, 1)
        self.assertEqual(resultado.valor, 8)
        self.assertEqual(resultado.inscripcion_id, 1)

    @patch('app.repositories.nota_repositorio.db')
    def test_buscar_todos(self, mock_db):
        nota1 = Nota()
        nota1.id = 1
        nota1.valor = 8
        nota1.inscripcion_id = 1
        
        nota2 = Nota()
        nota2.id = 2
        nota2.valor = 9
        nota2.inscripcion_id = 1
        
        mock_db.session.query().all.return_value = [nota1, nota2]
        
        repo = NotaRepository()
        resultado = repo.buscar_todos()
        
        mock_db.session.query.assert_called()
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0].valor, 8)
        self.assertEqual(resultado[1].valor, 9)

    @patch('app.repositories.nota_repositorio.db')
    def test_actualizar_nota(self, mock_db):
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
        
        repo = NotaRepository()
        resultado = repo.actualizar(nota)
        
        mock_db.session.merge.assert_called_once_with(nota)
        mock_db.session.commit.assert_called_once()
        self.assertEqual(resultado.id, 1)
        self.assertEqual(resultado.valor, 10)
        self.assertEqual(resultado.inscripcion_id, 1)

    @patch('app.repositories.nota_repositorio.db')
    def test_borrar_nota(self, mock_db):
        nota = Nota()
        nota.id = 1
        nota.valor = 8
        nota.inscripcion_id = 1
        
        mock_db.session.query().filter_by().first.return_value = nota
        mock_db.session.delete = Mock()
        mock_db.session.commit = Mock()
        
        repo = NotaRepository()
        resultado = repo.borrar_por_id(1)
        
        mock_db.session.delete.assert_called_once_with(nota)
        mock_db.session.commit.assert_called_once()
        self.assertEqual(resultado, nota)

    def test_validacion_nota(self):
        nota_valida = Nota()
        nota_valida.valor = 8
        nota_valida.inscripcion_id = 1
        self.assertEqual(nota_valida.valor, 8)
        
        nota_sin_valor = Nota()
        nota_sin_valor.inscripcion_id = 1
        self.assertIsNone(nota_sin_valor.valor)
        
        nota_valor_invalido = Nota()
        nota_valor_invalido.valor = 15
        nota_valor_invalido.inscripcion_id = 1
        
        self.assertEqual(nota_valor_invalido.valor, 15)

if __name__ == '__main__':
    unittest.main()