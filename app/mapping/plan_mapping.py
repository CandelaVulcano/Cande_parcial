from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.plan import Plan

class PlanMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    fecha_inicio = fields.String(
        required=True, validate=validate.Length(min=1, max=20))
    fecha_fin = fields.String(
        required=False, allow_none=True, validate=validate.Length(max=20))
    observacion = fields.String(
        required=False, allow_none=True, validate=validate.Length(max=200))

    @post_load
    def nuevo_plan(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Plan(**data)
