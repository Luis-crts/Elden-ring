from flask import Flask
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = 'clave_secreta_segura'
    register_routes(app)
    return app
