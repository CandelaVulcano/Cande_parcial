from marshmallow import Schema, fields
from app.models.alumno import Alumno


class AlumnoMapping(Schema):
    id = fields.Int()
    nombre = fields.Str()
    apellido = fields.Str()

    # Incompleto
