# ESTE TEST SI FUNCIONA
# Archivo: tests/test_auth.py
# Pruebas unitarias para las rutas de autenticación

import unittest
from app import create_app
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.create_all()

    def test_register_user(self):
        response = self.client.post('/auth/register', json={
            'username': 'testuser1',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['message'], 'Usuario registrado')

    def test_login_user(self):
        # Primero registramos un usuario
        self.client.post('/auth/register', json={
            'username': 'testuser2',
            'password': '123456'
        })

        # Luego intentamos login
        response = self.client.post('/auth/login', json={
            'username': 'testuser2',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Login exitoso')

if __name__ == '__main__':
    unittest.main()