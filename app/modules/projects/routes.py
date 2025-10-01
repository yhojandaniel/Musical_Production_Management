from flask import Blueprint, request, jsonify

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/create', methods=['POST'])
def create_project():
    from app.modules.projects.views import create_project_view
    data = request.get_json()
    result, status_code = create_project_view(data)
    return jsonify(result), status_code

@projects_bp.route('/view/<int:id>', methods=['GET'])
def view_project(id):
    from app.modules.projects.views import view_project_view
    result, status_code = view_project_view(id)
    return jsonify(result), status_code

@projects_bp.route('/edit/<int:id>', methods=['PUT'])
def edit_project(id):
    from app.modules.projects.views import edit_project_view
    data = request.get_json()
    result, status_code = edit_project_view(id, data)
    return jsonify(result), status_code

@projects_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_project(id):
    from app.modules.projects.views import delete_project_view
    result, status_code = delete_project_view(id)
    return jsonify(result), status_code