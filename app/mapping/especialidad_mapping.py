from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.especialidad import Especialidad

class EspecialidadMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    letra = fields.String(validate=validate.Length(max=5), allow_none=True)
    observacion = fields.String(
        validate=validate.Length(max=200), allow_none=True)
    tipo_especialidad_id = fields.Int(required=True)

    @post_load
    def nueva_especialidad(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Especialidad(**data)
