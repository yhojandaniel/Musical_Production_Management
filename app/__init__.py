from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar blueprints
    from app.modules.auth.routes import auth_bp
    from app.modules.bookings.routes import bookings_bp
    from app.modules.projects.routes import projects_bp
    from app.modules.clients.routes import clients_bp
    from app.modules.studios.routes import studios_bp
    from app.modules.notifications.routes import notifications_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(studios_bp)
    app.register_blueprint(notifications_bp)

    return app