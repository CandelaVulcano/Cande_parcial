from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.tipo_especialidad import TipoEspecialidad

class TipoEspecialidadMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    nivel = fields.String(
        required=True, validate=validate.Length(min=1, max=50))

    @post_load
    def nuevo_tipo_especialidad(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return TipoEspecialidad(**data)
