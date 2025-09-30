from app.models.project import Project
from app.models.customer import Customer

def create_project_view(data):
    name = data.get('name')
    status = data.get('status')
    customer_id = data.get('customer_id')

    customer = Customer.query.get(customer_id)
    if not customer:
        return {"error": "Cliente no encontrado"}, 404

    project = Project(project_name=name, project_status=status, customer_id=customer_id)
    project.save()
    return {"message": "Proyecto creado", "project_id": project.idproject}

def view_project_view(id):
    project = Project.query.get(id)
    if project:
        return {
            "id": project.idproject,
            "name": project.project_name,
            "status": project.project_status,
            "customer_id": project.customer_id,
            "created_at": project.created_at.isoformat(),
            "updated_at": project.updated_at.isoformat()
        }
    else:
        return {"error": "Proyecto no encontrado"}, 404

def edit_project_view(id, data):
    project = Project.query.get(id)
    if project:
        project.project_name = data.get('name', project.project_name)
        project.project_status = data.get('status', project.project_status)
        project.customer_id = data.get('customer_id', project.customer_id)
        project.save()
        return {"message": f"Proyecto {id} actualizado"}
    else:
        return {"error": "Proyecto no encontrado"}, 404

def delete_project_view(id):
    project = Project.query.get(id)
    if project:
        project.delete()
        return {"message": f"Proyecto {id} eliminado"}
    else:
        return {"error": "Proyecto no encontrado"}, 404