from flask import Blueprint

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/create', methods=['GET', 'POST'])
def create_booking():
    pass

@bookings_bp.route('/view/<int:id>')
def view_booking(id):
    pass

@bookings_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_booking(id):
    pass

@bookings_bp.route('/delete/<int:id>')
def delete_booking(id):
    pass