from flask import Blueprint

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/create', methods=['GET', 'POST'])
def create_client():
    pass

@clients_bp.route('/view/<int:id>')
def view_client(id):
    pass

@clients_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_client(id):
    pass

@clients_bp.route('/delete/<int:id>')
def delete_client(id):
    pass