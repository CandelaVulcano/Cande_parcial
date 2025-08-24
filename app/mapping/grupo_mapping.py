from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.grupo import Grupo

class GrupoMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nuevo_grupo(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Grupo(**data)
