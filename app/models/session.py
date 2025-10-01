from app import db
from datetime import datetime, timezone

class Session(db.Model):
    __tablename__ = 'session'
    
    idsession = db.Column(db.Integer, primary_key=True)
    date_session = db.Column(db.String(45), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.idcustomer'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.iduser'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def create_session(self, date, customer_id, created_by):
        self.date_session = date
        self.customer_id = customer_id
        self.created_by = created_by
        db.session.add(self)
        db.session.commit()

    def get_session_by_id(self, id):
        return Session.query.get(id)

    def update_session(self, id, date, customer_id, created_by):
        session = Session.query.get(id)
        if session:
            session.date_session = date
            session.customer_id = customer_id
            session.created_by = created_by
            db.session.commit()
        return session

    def delete_session(self, id):
        session = Session.query.get(id)
        if session:
            db.session.delete(session)
            db.session.commit()