from app import db
from sqlalchemy import func
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'user'
    
    iduser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    last_login = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    # Relación con sesiones creadas por este usuario
    sessions_created = db.relationship('Session', backref='created_by_user', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def create_user(self):
        # Registrar un nuevo usuario (cliente, ingeniero, administrador)
        # Recibe: nombre, email, contraseña, rol
        # Guarda en la base de datos
        pass

    def get_user_by_id(self):
        # Obtener un usuario por su ID
        # Recibe: user_id
        # Retorna: objeto User o None
        pass

    def get_user_by_email(self):
        # Buscar usuario por email (para login o validación)
        # Recibe: email
        # Retorna: objeto User o None
        pass

    def authenticate_user(self):
        # Validar credenciales de usuario (email y contraseña)
        # Recibe: email, contraseña
        # Retorna: True si es válido, False si no
        pass