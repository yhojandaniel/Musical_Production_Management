from flask import Blueprint

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/send', methods=['POST'])
def send_notification():
    pass

@notifications_bp.route('/view/<int:user_id>')
def view_notifications(user_id):
    pass

@notifications_bp.route('/schedule', methods=['POST'])
def schedule_reminder():
    pass