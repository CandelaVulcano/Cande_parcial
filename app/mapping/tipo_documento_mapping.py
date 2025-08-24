from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.tipo_documento import TipoDocumento

class TipoDocumentoMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=30))

    @post_load
    def nuevo_tipo_documento(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return TipoDocumento(**data)
