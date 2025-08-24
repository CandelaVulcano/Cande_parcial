from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.orientacion import Orientacion

class OrientacionMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    especialidad_id = fields.Integer(required=True)
    plan_id = fields.Integer(required=True)
    materia_id = fields.Integer(required=True)

    @post_load
    def nueva_orientacion(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Orientacion(**data)
