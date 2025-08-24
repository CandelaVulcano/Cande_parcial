from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.inscripcion import Inscripcion

class InscripcionMapping(Schema):
    id = fields.Int(dump_only=True)
    alumno_id = fields.Int(required=True)
    materia_id = fields.Int(required=True)
    fecha = fields.Date(required=True)

    @post_load
    def nuevo_inscripcion(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Inscripcion(**data)
