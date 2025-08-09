from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.alumno import Alumno


class AlumnoMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=50))
    apellido = fields.String(
        required=True, validate=validate.Length(min=1, max=50))
    nro_documento = fields.String(
        required=True, validate=validate.Length(min=1, max=20))
    tipo_documento_id = fields.Integer(required=True)
    fecha_nacimiento = fields.String(
        required=True, validate=validate.Length(min=1, max=20))
    sexo = fields.String(
        required=True, validate=validate.OneOf(['M', 'F']))
    nro_legajo = fields.Integer(required=True)
    fecha_ingreso = fields.String(
        required=True, validate=validate.Length(min=1, max=20))

    @post_load
    def nuevo_alumno(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Alumno(**data)
