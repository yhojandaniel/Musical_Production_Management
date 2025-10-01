from app import db
from datetime import datetime, timezone
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    iduser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)  # Aumentar longitud por hash
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relación con sesiones creadas por este usuario
    sessions_created = db.relationship('Session', backref='created_by_user', lazy=True)
    
    # Flask-Login requiere que el campo id se llame 'id', así que mapeamos iduser a id
    def get_id(self):
        return str(self.iduser)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def create_user(self, username, password):
        # Cifrar la contraseña antes de guardar
        self.username = username
        self.password = generate_password_hash(password)
        self.save()

    def get_user_by_id(self, user_id):
        # Obtener un usuario por su ID
        return User.query.get(user_id)

    def get_user_by_username(self, username):
        # Buscar usuario por username (para login o validación)
        return User.query.filter_by(username=username).first()

    def authenticate_user(self, password):
        # Validar credenciales de usuario (password)
        return check_password_hash(self.password, password)