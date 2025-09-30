from flask import Blueprint, request, jsonify

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/create', methods=['POST'])
def create_customer():
    from app.modules.customers.views import create_customer_view
    data = request.get_json()
    result = create_customer_view(data)
    return jsonify(result), 201

@customers_bp.route('/view/<int:id>', methods=['GET'])
def view_customer(id):
    from app.modules.customers.views import view_customer_view
    result = view_customer_view(id)
    return jsonify(result)

@customers_bp.route('/edit/<int:id>', methods=['PUT'])
def edit_customer(id):
    from app.modules.customers.views import edit_customer_view
    data = request.get_json()
    result = edit_customer_view(id, data)
    return jsonify(result)

@customers_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_customer(id):
    from app.modules.customers.views import delete_customer_view
    result = delete_customer_view(id)
    return jsonify(result)