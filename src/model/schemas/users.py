from flask_restful import fields

users_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'is_admin': fields.Boolean
}

users_fields_with_pass = {
    'id': fields.Integer,
    'username': fields.String,
    'is_admin': fields.Boolean,
    'password': fields.String
}