from flask_mail import Message
from app import mail

def send_email_view(data):
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')

    msg = Message(subject=subject, recipients=[recipient], body=body)
    try:
        mail.send(msg)
        return {"message": "Correo enviado exitosamente"}, 200
    except Exception as e:
        return {"error": f"Error al enviar correo: {str(e)}"}, 500