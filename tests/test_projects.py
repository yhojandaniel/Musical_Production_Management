import unittest
from app import create_app
from app import db

class TestProjects(unittest.TestCase):
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

    def test_create_project(self):
        # Creamos cliente
        customer_response = self.client.post('/customers/create', json={
            'name': 'Cliente Prueba'
        })
        self.assertEqual(customer_response.status_code, 201)
        customer_id = customer_response.get_json()['customer_id']

        # Creamos proyecto
        project_response = self.client.post('/projects/create', json={
            'name': 'Proyecto Prueba',
            'status': 'activo',
            'customer_id': customer_id
        })
        self.assertEqual(project_response.status_code, 201)
        project_data = project_response.get_json()
        self.assertEqual(project_data['message'], 'Proyecto creado')

    def test_view_project(self):
        # Creamos cliente
        customer_response = self.client.post('/customers/create', json={
            'name': 'Cliente Prueba'
        })
        self.assertEqual(customer_response.status_code, 201)
        customer_id = customer_response.get_json()['customer_id']

        # Creamos proyecto
        project_response = self.client.post('/projects/create', json={
            'name': 'Proyecto Prueba',
            'status': 'activo',
            'customer_id': customer_id
        })
        self.assertEqual(project_response.status_code, 201)
        project_id = project_response.get_json()['project_id']

        # Consultamos proyecto
        view_response = self.client.get(f'/projects/view/{project_id}')
        self.assertEqual(view_response.status_code, 200)
        view_data = view_response.get_json()
        self.assertEqual(view_data['name'], 'Proyecto Prueba')

if __name__ == '__main__':
    unittest.main()