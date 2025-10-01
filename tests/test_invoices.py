# ESTE TEST SI FUNCIONA
# Archivo: tests/test_invoices.py
# Pruebas unitarias para las rutas de facturas

import unittest
from app import create_app
from app import db

class TestInvoices(unittest.TestCase):
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

    def test_create_invoice(self):
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

        # Creamos factura
        invoice_response = self.client.post('/invoices/create', json={
            'number': 'F001',
            'type': 'factura',
            'payment_id': payment_id
        })
        self.assertEqual(invoice_response.status_code, 201)
        invoice_data = invoice_response.get_json()
        self.assertEqual(invoice_data['message'], 'Factura creada')

    def test_view_invoice(self):
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

        # Creamos factura
        invoice_response = self.client.post('/invoices/create', json={
            'number': 'F001',
            'type': 'factura',
            'payment_id': payment_id
        })
        self.assertEqual(invoice_response.status_code, 201)
        invoice_id = invoice_response.get_json()['invoice_id']

        # Consultamos factura
        view_response = self.client.get(f'/invoices/view/{invoice_id}')
        self.assertEqual(view_response.status_code, 200)
        view_data = view_response.get_json()
        self.assertEqual(view_data['number'], 'F001')

if __name__ == '__main__':
    unittest.main()