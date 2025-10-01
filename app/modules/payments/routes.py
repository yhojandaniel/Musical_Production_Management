from flask import Blueprint, request, jsonify

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/create', methods=['POST'])
def create_payment():
    from app.modules.payments.views import create_payment_view
    data = request.get_json()
    result, status_code = create_payment_view(data)
    return jsonify(result), status_code

@payments_bp.route('/view/<int:id>', methods=['GET'])
def view_payment(id):
    from app.modules.payments.views import view_payment_view
    result, status_code = view_payment_view(id)
    return jsonify(result), status_code

@payments_bp.route('/update-status/<int:id>', methods=['PUT'])
def update_payment_status(id):
    from app.modules.payments.views import update_payment_status_view
    data = request.get_json()
    result, status_code = update_payment_status_view(id, data)
    return jsonify(result), status_code

@payments_bp.route('/list-by-project/<int:project_id>', methods=['GET'])
def list_payments_by_project(project_id):
    from app.modules.payments.views import list_payments_by_project_view
    result, status_code = list_payments_by_project_view(project_id)
    return jsonify(result), status_code