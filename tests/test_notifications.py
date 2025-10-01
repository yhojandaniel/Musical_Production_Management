import unittest
from app import create_app
from app import mail
from unittest.mock import patch

class TestNotifications(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['MAIL_SUPPRESS_SEND'] = True  # No enviar correos reales en pruebas
        self.client = self.app.test_client()

    @patch('app.modules.notifications.views.mail.send')
    def test_send_email(self, mock_send):
        response = self.client.post('/notifications/send-email', json={
            'recipient': 'cliente@correo.com',
            'subject': 'Recordatorio de sesión',
            'body': 'Hola, tienes una sesión programada para mañana.'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Correo enviado exitosamente')
        mock_send.assert_called_once()

if __name__ == '__main__':
    unittest.main()