import unittest
from app import create_app
from app import db

class TestSessions(unittest.TestCase):
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

    def test_create_session(self):
        # Creamos cliente
        customer_response = self.client.post('/customers/create', json={
            'name': 'Cliente Prueba'
        })
        self.assertEqual(customer_response.status_code, 201)
        customer_id = customer_response.get_json()['customer_id']

        # Creamos usuario
        auth_response = self.client.post('/auth/register', json={
            'username': 'testuser_sessions',
            'password': '123456'
        })
        self.assertEqual(auth_response.status_code, 201)
        user_id = auth_response.get_json()['user_id']

        # Creamos sesión
        session_response = self.client.post('/sessions/create', json={
            'date_session': '2025-04-10',
            'customer_id': customer_id,
            'created_by': user_id
        })
        self.assertEqual(session_response.status_code, 201)
        session_data = session_response.get_json()
        self.assertEqual(session_data['message'], 'Sesión creada')

    def test_view_session(self):
        # Creamos cliente
        customer_response = self.client.post('/customers/create', json={
            'name': 'Cliente Prueba'
        })
        self.assertEqual(customer_response.status_code, 201)
        customer_id = customer_response.get_json()['customer_id']

        # Creamos usuario
        auth_response = self.client.post('/auth/register', json={
            'username': 'testuser_sessions2',
            'password': '123456'
        })
        self.assertEqual(auth_response.status_code, 201)
        user_id = auth_response.get_json()['user_id']

        # Creamos sesión
        session_response = self.client.post('/sessions/create', json={
            'date_session': '2025-04-10',
            'customer_id': customer_id,
            'created_by': user_id
        })
        self.assertEqual(session_response.status_code, 201)
        session_id = session_response.get_json()['session_id']

        # Consultamos sesión
        view_response = self.client.get(f'/sessions/view/{session_id}')
        self.assertEqual(view_response.status_code, 200)
        view_data = view_response.get_json()
        self.assertEqual(view_data['date'], '2025-04-10')

if __name__ == '__main__':
    unittest.main()