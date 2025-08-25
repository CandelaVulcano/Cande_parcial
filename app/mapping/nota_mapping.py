from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.nota import Nota

class NotaMapping(Schema):
    id = fields.Int(dump_only=True)
    valor = fields.Float(required=True, validate=validate.Range(min=1, max=10))
    inscripcion_id = fields.Int(required=True)

    @post_load
    def nueva_nota(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Nota(**data)
