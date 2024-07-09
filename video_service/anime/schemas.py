from marshmallow import Schema, fields, validate


class AnimeSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=4, max=120))
    description = fields.String(required=True)
    author = fields.String(required=True)
    create_at = fields.Date()
    genres = fields.List(fields.String(), required=True)
