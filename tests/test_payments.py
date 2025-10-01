import unittest
from app import create_app
from app import db

class TestPayments(unittest.TestCase):
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

    def test_create_payment(self):
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

        # Creamos pago
        payment_response = self.client.post('/payments/create', json={
            'amount': 100.0,
            'method': 'tarjeta',
            'project_id': project_id
        })
        self.assertEqual(payment_response.status_code, 201)
        payment_data = payment_response.get_json()
        self.assertEqual(payment_data['message'], 'Pago registrado')

    def test_view_payment(self):
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

        # Creamos pago
        payment_response = self.client.post('/payments/create', json={
            'amount': 100.0,
            'method': 'tarjeta',
            'project_id': project_id
        })
        self.assertEqual(payment_response.status_code, 201)
        payment_id = payment_response.get_json()['payment_id']

        # Consultamos pago
        view_response = self.client.get(f'/payments/view/{payment_id}')
        self.assertEqual(view_response.status_code, 200)
        view_data = view_response.get_json()
        self.assertEqual(view_data['amount'], 100.0)

if __name__ == '__main__':
    unittest.main()