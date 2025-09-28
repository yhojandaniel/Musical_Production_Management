from flask import Blueprint

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/create', methods=['GET', 'POST'])
def create_project():
    pass

@projects_bp.route('/view/<int:id>')
def view_project(id):
    pass

@projects_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    pass

@projects_bp.route('/delete/<int:id>')
def delete_project(id):
    pass