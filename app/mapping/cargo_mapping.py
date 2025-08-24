from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.cargo import Cargo

class CargoMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    puntos = fields.Integer(required=True)
    categoria_cargo_id = fields.Integer(required=True)
    tipo_dedicacion_id = fields.Integer(required=True)

    @post_load
    def nuevo_cargo(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Cargo(**data)
