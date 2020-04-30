from flask_restful import fields

users_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'is_admin': fields.Boolean
}