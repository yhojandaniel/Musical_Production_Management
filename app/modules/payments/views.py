from app import db
from app.models.payment import Payment
from app.models.project import Project

def create_payment_view(data):
    amount = data.get('amount')
    method = data.get('method')
    project_id = data.get('project_id')

    project = db.session.get(Project, project_id)
    if not project:
        return {"error": "Proyecto no encontrado"}, 404

    payment = Payment(amount_payment=amount, payment_method=method, project_id=project_id)
    payment.save()
    return {"message": "Pago registrado", "payment_id": payment.idpayment}, 201

def view_payment_view(id):
    payment = db.session.get(Payment, id)
    if payment:
        return {
            "id": payment.idpayment,
            "amount": payment.amount_payment,
            "method": payment.payment_method,
            "project_id": payment.project_id,
            "created_at": payment.created_at.isoformat(),
            "updated_at": payment.updated_at.isoformat()
        }, 200
    else:
        return {"error": "Pago no encontrado"}, 404

def update_payment_status_view(id, data):
    payment = db.session.get(Payment, id)
    if payment:
        # Asumiendo que tienes un campo `status` en el modelo
        payment.status = data.get('status', payment.status)
        payment.save()
        return {"message": f"Estado del pago {id} actualizado"}, 200
    else:
        return {"error": "Pago no encontrado"}, 404

def list_payments_by_project_view(project_id):
    payments = Payment.query.filter_by(project_id=project_id).all()
    return [
        {
            "id": p.idpayment,
            "amount": p.amount_payment,
            "method": p.payment_method,
            "created_at": p.created_at.isoformat(),
            "updated_at": p.updated_at.isoformat()
        }
        for p in payments
    ], 200