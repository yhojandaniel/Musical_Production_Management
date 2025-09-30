from app.models.user import User
from werkzeug.security import check_password_hash

def login_view(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # Aquí puedes usar Flask-Login para manejar la sesión
        return {"message": "Login exitoso", "user_id": user.iduser}
    else:
        return {"error": "Credenciales inválidas"}, 401

def register_view(data):
    username = data.get('username')
    password = data.get('password')

    user = User(username=username, password=password)
    user.save()
    return {"message": "Usuario registrado", "user_id": user.iduser}

def logout_view():
    # Aquí puedes usar Flask-Login para cerrar sesión
    return {"message": "Logout exitoso"}