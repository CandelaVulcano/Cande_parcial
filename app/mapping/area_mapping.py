from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.area import Area


class AreaMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nueva_area(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Area(**data)
