from src import db
from flask import current_app
from flask_bcrypt import Bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False)

    def __init__(self, username, password, is_admin):
        bcrypt = Bcrypt(current_app)
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.is_admin = is_admin
    
    def compare_password(self, password):
        bcrypt = Bcrypt(current_app)
        return bcrypt.check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<User: {self.username}'