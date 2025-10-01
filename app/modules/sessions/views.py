from app import db
from app.models.session import Session
from app.models.customer import Customer
from app.models.user import User

def create_session_view(data):
    date = data.get('date_session')
    customer_id = data.get('customer_id')
    created_by = data.get('created_by')

    customer = db.session.get(Customer, customer_id)
    user = db.session.get(User, created_by)
    if not customer or not user:
        return {"error": "Cliente o usuario no encontrado"}, 404

    session = Session(date_session=date, customer_id=customer_id, created_by=created_by)
    session.save()
    return {"message": "Sesión creada", "session_id": session.idsession}, 201

def view_session_view(id):
    session = db.session.get(Session, id)
    if session:
        return {
            "id": session.idsession,
            "date": session.date_session,
            "customer_id": session.customer_id,
            "created_by": session.created_by,
            "created_at": session.created_at.isoformat(),
            "updated_at": session.updated_at.isoformat()
        }, 200
    else:
        return {"error": "Sesión no encontrada"}, 404

def edit_session_view(id, data):
    session = db.session.get(Session, id)
    if session:
        session.date_session = data.get('date_session', session.date_session)
        session.customer_id = data.get('customer_id', session.customer_id)
        session.created_by = data.get('created_by', session.created_by)
        session.save()
        return {"message": f"Sesión {id} actualizada"}, 200
    else:
        return {"error": "Sesión no encontrada"}, 404

def delete_session_view(id):
    session = db.session.get(Session, id)
    if session:
        session.delete()
        return {"message": f"Sesión {id} eliminada"}, 200
    else:
        return {"error": "Sesión no encontrada"}, 404