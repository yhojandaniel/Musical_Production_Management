from flask import Blueprint, request, jsonify

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/send-email', methods=['POST'])
def send_email():
    from app.modules.notifications.views import send_email_view
    data = request.get_json()
    result = send_email_view(data)
    return jsonify(result)