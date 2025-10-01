from app import db
from datetime import datetime, timezone

class Customer(db.Model):
    __tablename__ = 'customer'
    
    idcustomer = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relaciones
    sessions = db.relationship('Session', backref='customer', lazy=True)
    projects = db.relationship('Project', backref='customer', lazy=True)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Aquí van las funciones que antes estaban con `pass`
    def create_customer(self, name):
        self.customer_name = name
        db.session.add(self)
        db.session.commit()

    def get_customer_by_id(self, id):
        return Customer.query.get(id)

    def update_customer(self, id, name):
        customer = Customer.query.get(id)
        if customer:
            customer.customer_name = name
            db.session.commit()
        return customer

    def delete_customer(self, id):
        customer = Customer.query.get(id)
        if customer:
            db.session.delete(customer)
            db.session.commit()