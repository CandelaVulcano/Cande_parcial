from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.autoridad import Autoridad

class AutoridadMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    cargo = fields.String(
        required=True, validate=validate.Length(min=1, max=50))
    telefono = fields.String(
        required=False, validate=validate.Length(max=20))
    email = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    facultad_id = fields.Int(required=True)

    @post_load
    def nueva_autoridad(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Autoridad(**data)
