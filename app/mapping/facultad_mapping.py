from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.facultad import Facultad

class FacultadMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    abreviatura = fields.String(
        required=True, validate=validate.Length(min=1, max=10))
    directorio = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    sigla = fields.String(
        required=True, validate=validate.Length(min=1, max=10))
    codigo_postal = fields.String(
        validate=validate.Length(max=10), allow_none=True)
    ciudad = fields.String(validate=validate.Length(max=50), allow_none=True)
    domicilio = fields.String(
        validate=validate.Length(max=100), allow_none=True)
    telefono = fields.String(validate=validate.Length(max=20), allow_none=True)
    contacto = fields.String(
        validate=validate.Length(max=100), allow_none=True)
    email = fields.String(required=True, validate=validate.Length(max=100))
    universidad_id = fields.Integer(required=True)

    @post_load
    def nueva_facultad(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Facultad(**data)
