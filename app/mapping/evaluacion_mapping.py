from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.evaluacion import Evaluacion

class EvaluacionMapping(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    fecha = fields.Date(required=True)

    @post_load
    def nueva_evaluacion(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Evaluacion(**data)
