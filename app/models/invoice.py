from app import db
from datetime import datetime, timezone

class Invoice(db.Model):
    __tablename__ = 'invoice'
    
    idinvoice = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(45), nullable=False)
    type = db.Column(db.Enum('factura', 'boleta'), nullable=False)
    payment_idpayment = db.Column(db.Integer, db.ForeignKey('payment.idpayment'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def create_invoice(self, number, type, payment_id):
        self.number = number
        self.type = type
        self.payment_idpayment = payment_id
        db.session.add(self)
        db.session.commit()

    def get_invoice_by_id(self, id):
        return Invoice.query.get(id)