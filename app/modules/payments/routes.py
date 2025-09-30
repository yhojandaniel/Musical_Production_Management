from flask import Blueprint, request, jsonify

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/create', methods=['POST'])
def create_payment():
    from app.modules.payments.views import create_payment_view
    data = request.get_json()
    result = create_payment_view(data)
    return jsonify(result), 201

@payments_bp.route('/view/<int:id>', methods=['GET'])
def view_payment(id):
    from app.modules.payments.views import view_payment_view
    result = view_payment_view(id)
    return jsonify(result)

@payments_bp.route('/update-status/<int:id>', methods=['PUT'])
def update_payment_status(id):
    from app.modules.payments.views import update_payment_status_view
    data = request.get_json()
    result = update_payment_status_view(id, data)
    return jsonify(result)

@payments_bp.route('/list-by-project/<int:project_id>', methods=['GET'])
def list_payments_by_project(project_id):
    from app.modules.payments.views import list_payments_by_project_view
    result = list_payments_by_project_view(project_id)
    return jsonify(result)