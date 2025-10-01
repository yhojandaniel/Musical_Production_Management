from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Ruta a la que redirige si no está logueado

    from app.models.user import User
    from app.models.customer import Customer
    from app.models.session import Session
    from app.models.project import Project
    from app.models.payment import Payment
    from app.models.invoice import Invoice

    # Registrar blueprints
    from app.modules.auth.routes import auth_bp
    from app.modules.customers.routes import customers_bp
    from app.modules.sessions.routes import sessions_bp
    from app.modules.projects.routes import projects_bp
    from app.modules.payments.routes import payments_bp
    from app.modules.invoices.routes import invoices_bp
    from app.modules.notifications.routes import notifications_bp
    from app.modules.home.routes import home_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(sessions_bp, url_prefix='/sessions')
    app.register_blueprint(projects_bp, url_prefix='/projects')
    app.register_blueprint(payments_bp, url_prefix='/payments')
    app.register_blueprint(invoices_bp, url_prefix='/invoices')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(home_bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))