from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.departamento import Departamento

class DepartamentoMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    facultad_id = fields.Int(required=True)
    area_id = fields.Int(allow_none=True)

    @post_load
    def nuevo_departamento(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Departamento(**data)
