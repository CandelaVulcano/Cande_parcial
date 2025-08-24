from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.tipo_dedicacion import TipoDedicacion

class TipoDedicacionMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    observacion = fields.String(
        required=False, validate=validate.Length(max=200))

    @post_load
    def nuevo_tipo_dedicacion(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return TipoDedicacion(**data)
