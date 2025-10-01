from flask import Blueprint, request, jsonify
from flask_login import login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    from app.modules.auth.views import login_view
    data = request.get_json()
    result, status_code = login_view(data)
    return jsonify(result), status_code

@auth_bp.route('/register', methods=['POST'])
def register():
    from app.modules.auth.views import register_view
    data = request.get_json()
    result, status_code = register_view(data)
    return jsonify(result), status_code

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    from app.modules.auth.views import logout_view
    result, status_code = logout_view()
    return jsonify(result), status_code