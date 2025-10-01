# ESTE TEST SI FUNCIONA
# Archivo: tests/test_customers.py
# Pruebas unitarias para las rutas de clientes

import unittest
import json
from app import create_app
from app import db
from app.models.customer import Customer

class TestCustomers(unittest.TestCase):
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

    def test_create_customer(self):
        response = self.client.post('/customers/create', json={
            'name': 'Cliente de Prueba'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['message'], 'Cliente creado')

    def test_view_customer(self):
        # Primero creamos un cliente
        create_response = self.client.post('/customers/create', json={
            'name': 'Cliente de Prueba'
        })
        customer_id = create_response.get_json()['customer_id']

        # Luego lo consultamos
        response = self.client.get(f'/customers/view/{customer_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Cliente de Prueba')

    def test_edit_customer(self):
        # Creamos un cliente
        create_response = self.client.post('/customers/create', json={
            'name': 'Cliente Original'
        })
        customer_id = create_response.get_json()['customer_id']

        # Lo editamos
        response = self.client.put(f'/customers/edit/{customer_id}', json={
            'name': 'Cliente Editado'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], f'Cliente {customer_id} actualizado')

        # Verificamos que se haya actualizado
        view_response = self.client.get(f'/customers/view/{customer_id}')
        data = view_response.get_json()
        self.assertEqual(data['name'], 'Cliente Editado')

    def test_delete_customer(self):
        # Creamos un cliente
        create_response = self.client.post('/customers/create', json={
            'name': 'Cliente a Eliminar'
        })
        customer_id = create_response.get_json()['customer_id']

        # Lo eliminamos
        response = self.client.delete(f'/customers/delete/{customer_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], f'Cliente {customer_id} eliminado')

        # Verificamos que ya no exista
        view_response = self.client.get(f'/customers/view/{customer_id}')
        self.assertEqual(view_response.status_code, 404)  

if __name__ == '__main__':
    unittest.main()