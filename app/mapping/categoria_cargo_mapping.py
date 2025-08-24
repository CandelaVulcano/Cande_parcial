from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.categoria_cargo import CategoriaCargo

class CategoriaCargoMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nueva_categoria_cargo(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return CategoriaCargo(**data)
