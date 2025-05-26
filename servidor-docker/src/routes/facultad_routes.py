from flask import Blueprint, jsonify, request
from app.models.facultad import Facultad
from app.services.facultad_service import FacultadService
from ..auth import auth  # Cambiado de src.auth a importación relativa

facultad_bp = Blueprint('facultad', __name__, url_prefix='/api/facultades')

@facultad_bp.route('', methods=['GET'])
@auth.login_required
def get_facultades():
    """Obtiene todas las facultades"""
    facultades = FacultadService.buscar_todos()
    return jsonify([{
        'id': f.id,
        'nombre': f.nombre,
        'abreviatura': f.abreviatura,
        'directorio': f.directorio,
        'sigla': f.sigla,
        'codigo_postal': f.codigo_postal,
        'ciudad': f.ciudad,
        'domicilio': f.domicilio,
        'telefono': f.telefono,
        'contacto': f.contacto,
        'email': f.email
    } for f in facultades])

@facultad_bp.route('/<int:id>', methods=['GET'])
@auth.login_required
def get_facultad(id):
    """Obtiene una facultad por id"""
    facultad = FacultadService.buscar_por_id(id)
    if not facultad:
        return jsonify({'message': 'Facultad no encontrada'}), 404
    
    return jsonify({
        'id': facultad.id,
        'nombre': facultad.nombre,
        'abreviatura': facultad.abreviatura,
        'directorio': facultad.directorio,
        'sigla': facultad.sigla,
        'codigo_postal': facultad.codigo_postal,
        'ciudad': facultad.ciudad,
        'domicilio': facultad.domicilio,
        'telefono': facultad.telefono,
        'contacto': facultad.contacto,
        'email': facultad.email
    })