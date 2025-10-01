from app import db
from app.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user

def login_view(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return {"message": "Login exitoso", "user_id": user.iduser}, 200
    else:
        return {"error": "Credenciales inválidas"}, 401

def register_view(data):
    username = data.get('username')
    password = data.get('password')

    hashed_password = generate_password_hash(password)
    user = User(username=username, password=hashed_password)
    user.save()
    login_user(user)  # Opcional: loguear automáticamente al registrar
    return {"message": "Usuario registrado", "user_id": user.iduser}, 201

def logout_view():
    logout_user()
    return {"message": "Logout exitoso"}, 200