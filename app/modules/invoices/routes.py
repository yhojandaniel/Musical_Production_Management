from flask import Blueprint, request, jsonify

invoices_bp = Blueprint('invoices', __name__)

@invoices_bp.route('/create', methods=['POST'])
def create_invoice():
    from app.modules.invoices.views import create_invoice_view
    data = request.get_json()
    result, status_code = create_invoice_view(data)
    return jsonify(result), status_code

@invoices_bp.route('/view/<int:id>', methods=['GET'])
def view_invoice(id):
    from app.modules.invoices.views import view_invoice_view
    result, status_code = view_invoice_view(id)
    return jsonify(result), status_code