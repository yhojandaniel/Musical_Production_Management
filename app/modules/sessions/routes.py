from flask import Blueprint, request, jsonify

sessions_bp = Blueprint('sessions', __name__)

@sessions_bp.route('/create', methods=['POST'])
def create_session():
    from app.modules.sessions.views import create_session_view
    data = request.get_json()
    result = create_session_view(data)
    return jsonify(result), 201

@sessions_bp.route('/view/<int:id>', methods=['GET'])
def view_session(id):
    from app.modules.sessions.views import view_session_view
    result = view_session_view(id)
    return jsonify(result)

@sessions_bp.route('/edit/<int:id>', methods=['PUT'])
def edit_session(id):
    from app.modules.sessions.views import edit_session_view
    data = request.get_json()
    result = edit_session_view(id, data)
    return jsonify(result)

@sessions_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_session(id):
    from app.modules.sessions.views import delete_session_view
    result = delete_session_view(id)
    return jsonify(result)