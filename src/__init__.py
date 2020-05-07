from flask_restful import Api
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_jwt_extended import  JWTManager


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api = Api(app)
    db.init_app(app)
    JWTManager(app)

    # imports
    from src.controller.indexController import controller_index
    from src.controller.userController import controller_user
    from src.controller.authController import controller_auth
    app.register_blueprint(controller_index)
    app.register_blueprint(controller_user)
    app.register_blueprint(controller_auth)

    return app
