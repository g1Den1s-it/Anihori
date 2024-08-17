from marshmallow import Schema, fields, validate


class AnimeSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=4, max=120))
    description = fields.String(required=True)
    authors = fields.List(fields.String(), required=True)
    create_at = fields.Date()
    genres = fields.List(fields.String(), required=True)


class SeriesSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=4, max=44))
    anime = fields.Integer(required=True)
    position = fields.Integer(required=True)
