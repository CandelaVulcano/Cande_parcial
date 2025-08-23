from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.cursada import Cursada

class CursadaMapping(Schema):
    id = fields.Int(dump_only=True)
    alumno_id = fields.Int(required=True)
    materia_id = fields.Int(required=True)
    anio = fields.Int(required=True, validate=validate.Range(min=1900, max=2100))

    @post_load
    def nueva_cursada(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Cursada(**data)
