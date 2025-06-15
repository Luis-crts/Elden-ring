# app/__init__.py
from flask import Flask

app = Flask(__name__)

from app import routes  # importa las rutas después de crear la app
