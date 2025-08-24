from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.materia import Materia

class MateriaMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    codigo = fields.String(
        required=True, validate=validate.Length(min=1, max=20))
    observacion = fields.String(
        validate=validate.Length(max=200), allow_none=True)
    departamento_id = fields.Integer(required=True)

    @post_load
    def nueva_materia(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Materia(**data)
