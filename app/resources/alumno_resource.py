from flask import Blueprint
from app.services.alumno_service import AlumnoService
from app.models.alumno import Alumno
from app.mapping.alumno_mapping import AlumnoMapping

alumno_bp = Blueprint('alumno', __name__)
alumno_mapping = AlumnoMapping()


@alumno_bp.route('/alumnos', methods=['GET'])
def read_all():
    alumnos = AlumnoService.buscar_todos()
    return alumno_mapping.dump(alumnos, many=True), 200


@alumno_bp.route('/alumno/<int:id>', methods=['GET'])
def read_by_id(id: int):
    alumno = AlumnoService.buscar_por_id(id)
    return alumno_mapping.dump(alumno), 200
