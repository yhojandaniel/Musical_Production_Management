from app import db
from datetime import datetime, timezone

class Project(db.Model):
    __tablename__ = 'project'
    
    idproject = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(45), nullable=False)
    project_status = db.Column(db.String(45), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.idcustomer'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def create_project(self, name, status, customer_id):
        self.project_name = name
        self.project_status = status
        self.customer_id = customer_id
        db.session.add(self)
        db.session.commit()

    def get_project_by_id(self, id):
        return Project.query.get(id)

    def update_project(self, id, name, status):
        project = Project.query.get(id)
        if project:
            project.project_name = name
            project.project_status = status
            db.session.commit()
        return project

    def delete_project(self, id):
        project = Project.query.get(id)
        if project:
            db.session.delete(project)
            db.session.commit()