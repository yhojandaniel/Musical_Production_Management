from app.models.customer import Customer

def create_customer_view(data):
    name = data.get('name')
    customer = Customer(customer_name=name)
    customer.save()
    return {"message": "Cliente creado", "customer_id": customer.idcustomer}

def view_customer_view(id):
    customer = Customer.query.get(id)
    if customer:
        return {
            "id": customer.idcustomer,
            "name": customer.customer_name,
            "created_at": customer.created_at.isoformat(),
            "updated_at": customer.updated_at.isoformat()
        }
    else:
        return {"error": "Cliente no encontrado"}, 404

def edit_customer_view(id, data):
    customer = Customer.query.get(id)
    if customer:
        customer.customer_name = data.get('name', customer.customer_name)
        customer.save()
        return {"message": f"Cliente {id} actualizado"}
    else:
        return {"error": "Cliente no encontrado"}, 404

def delete_customer_view(id):
    customer = Customer.query.get(id)
    if customer:
        customer.delete()
        return {"message": f"Cliente {id} eliminado"}
    else:
        return {"error": "Cliente no encontrado"}, 404