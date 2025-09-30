from app import db
from datetime import datetime, timezone

class Payment(db.Model):
    __tablename__ = 'payment'
    
    idpayment = db.Column(db.Integer, primary_key=True)
    amount_payment = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(45), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.idproject'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def create_payment(self, amount, method, project_id):
        self.amount_payment = amount
        self.payment_method = method
        self.project_id = project_id
        db.session.add(self)
        db.session.commit()

    def get_payment_by_id(self, id):
        return Payment.query.get(id)

    def update_payment_status(self, id, new_status):
        payment = Payment.query.get(id)
        if payment:
            # Aquí asumimos que tienes un campo `status` en el modelo
            payment.status = new_status
            db.session.commit()
        return payment