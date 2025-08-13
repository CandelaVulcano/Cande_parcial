from flask import Blueprint, request, jsonify
from app.services.cursada_service import CursadaService
from app.resources.cursada_mapping import CursadaMapping

cursada_bp = Blueprint('cursada', __name__)
cursada_mapping = CursadaMapping()

@cursada_bp.route('/cursadas', methods=['GET'])
def read_all():
    cursadas = CursadaService.buscar_todos()
    return cursada_mapping.dump(cursadas, many=True), 200

@cursada_bp.route('/cursada/<int:id>', methods=['GET'])
def read_by_id(id):
    cursada = CursadaService.buscar_por_id(id)
    return cursada_mapping.dump(cursada), 200
