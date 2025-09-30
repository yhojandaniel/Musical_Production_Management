from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    from app.modules.auth.views import login_view
    data = request.get_json()
    result = login_view(data)
    return jsonify(result)

@auth_bp.route('/register', methods=['POST'])
def register():
    from app.modules.auth.views import register_view
    data = request.get_json()
    result = register_view(data)
    return jsonify(result), 201

@auth_bp.route('/logout', methods=['POST'])
def logout():
    from app.modules.auth.views import logout_view
    result = logout_view()
    return jsonify(result)