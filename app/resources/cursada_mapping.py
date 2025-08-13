from marshmallow import Schema, fields
from app.models.cursada import Cursada

class CursadaMapping(Schema):
    id = fields.Int()
    alumno_id = fields.Int()
    materia_id = fields.Int()
    anio = fields.Int()
