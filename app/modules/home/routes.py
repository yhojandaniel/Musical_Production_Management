from flask import Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return {"message": "Bienvenido al Gestor de Estudio de Grabacion"}, 200