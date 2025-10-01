from app.models.customer import Customer
from app import db

def create_customer_view(data):
    name = data.get('name')
    customer = Customer(customer_name=name)
    customer.save()
    return {"message": "Cliente creado", "customer_id": customer.idcustomer}, 201

def view_customer_view(id):
    customer = db.session.get(Customer, id)
    if customer:
        return {
            "id": customer.idcustomer,
            "name": customer.customer_name,
            "created_at": customer.created_at.isoformat(),
            "updated_at": customer.updated_at.isoformat()
        }, 200
    else:
        return {"error": "Cliente no encontrado"}, 404

def edit_customer_view(id, data):
    customer = db.session.get(Customer, id)
    if customer:
        customer.customer_name = data.get('name', customer.customer_name)
        customer.save()
        return {"message": f"Cliente {id} actualizado"}, 200
    else:
        return {"error": "Cliente no encontrado"}, 404

def delete_customer_view(id):
    customer = db.session.get(Customer, id)
    if customer:
        customer.delete()
        return {"message": f"Cliente {id} eliminado"}, 200
    else:
        return {"error": "Cliente no encontrado"}, 404