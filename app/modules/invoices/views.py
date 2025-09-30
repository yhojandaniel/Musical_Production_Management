from app.models.invoice import Invoice
from app.models.payment import Payment

def create_invoice_view(data):
    number = data.get('number')
    type = data.get('type')
    payment_id = data.get('payment_id')

    payment = Payment.query.get(payment_id)
    if not payment:
        return {"error": "Pago no encontrado"}, 404

    invoice = Invoice(number=number, type=type, payment_idpayment=payment_id)
    invoice.save()
    return {"message": "Factura creada", "invoice_id": invoice.idinvoice}

def view_invoice_view(id):
    invoice = Invoice.query.get(id)
    if invoice:
        return {
            "id": invoice.idinvoice,
            "number": invoice.number,
            "type": invoice.type,
            "payment_id": invoice.payment_idpayment,
            "created_at": invoice.created_at.isoformat(),
            "updated_at": invoice.updated_at.isoformat()
        }
    else:
        return {"error": "Factura no encontrada"}, 404