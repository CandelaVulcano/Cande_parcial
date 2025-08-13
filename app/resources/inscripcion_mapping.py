from marshmallow import Schema, fields
from app.models.inscripcion import Inscripcion

class InscripcionMapping(Schema):
    id = fields.Int()
    alumno_id = fields.Int()
    materia_id = fields.Int()
    fecha = fields.Date()
