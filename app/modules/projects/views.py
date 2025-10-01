from app import db
from app.models.project import Project
from app.models.customer import Customer

def create_project_view(data):
    name = data.get('name')
    status = data.get('status')
    customer_id = data.get('customer_id')

    customer = db.session.get(Customer, customer_id)
    if not customer:
        return {"error": "Cliente no encontrado"}, 404

    project = Project(project_name=name, project_status=status, customer_id=customer_id)
    project.save()
    return {"message": "Proyecto creado", "project_id": project.idproject}, 201

def view_project_view(id):
    project = db.session.get(Project, id)
    if project:
        return {
            "id": project.idproject,
            "name": project.project_name,
            "status": project.project_status,
            "customer_id": project.customer_id,
            "created_at": project.created_at.isoformat(),
            "updated_at": project.updated_at.isoformat()
        }, 200
    else:
        return {"error": "Proyecto no encontrado"}, 404

def edit_project_view(id, data):
    project = db.session.get(Project, id)
    if project:
        project.project_name = data.get('name', project.project_name)
        project.project_status = data.get('status', project.project_status)
        project.customer_id = data.get('customer_id', project.customer_id)
        project.save()
        return {"message": f"Proyecto {id} actualizado"}, 200
    else:
        return {"error": "Proyecto no encontrado"}, 404

def delete_project_view(id):
    project = db.session.get(Project, id)
    if project:
        project.delete()
        return {"message": f"Proyecto {id} eliminado"}, 200
    else:
        return {"error": "Proyecto no encontrado"}, 404