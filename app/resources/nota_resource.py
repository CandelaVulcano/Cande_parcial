from flask import Blueprint, request, jsonify
from app.services.nota_service import NotaService
from app.resources.nota_mapping import NotaMapping

nota_bp = Blueprint('nota', __name__)
nota_mapping = NotaMapping()

@nota_bp.route('/notas', methods=['GET'])
def read_all():
    notas = NotaService.buscar_todos()
    return nota_mapping.dump(notas, many=True), 200

@nota_bp.route('/nota/<int:id>', methods=['GET'])
def read_by_id(id):
    nota = NotaService.buscar_por_id(id)
    return nota_mapping.dump(nota), 200
