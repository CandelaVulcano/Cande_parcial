from marshmallow import Schema, fields
from app.models.nota import Nota

class NotaMapping(Schema):
    id = fields.Int()
    valor = fields.Float()
    inscripcion_id = fields.Int()
