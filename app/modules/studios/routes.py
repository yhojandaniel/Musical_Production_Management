from flask import Blueprint

studios_bp = Blueprint('studios', __name__)

@studios_bp.route('/list')
def list_studios():
    pass

@studios_bp.route('/view/<int:id>')
def view_studio(id):
    pass

@studios_bp.route('/create', methods=['GET', 'POST'])
def create_studio():
    pass

@studios_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_studio(id):
    pass