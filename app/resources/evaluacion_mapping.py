from marshmallow import Schema, fields
from app.models.evaluacion import Evaluacion

class EvaluacionMapping(Schema):
    id = fields.Int()
    nombre = fields.Str()
    fecha = fields.Date()
