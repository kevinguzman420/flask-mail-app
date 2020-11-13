from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS #

from itsdangerous import URLSafeTimedSerializer

login_manager = LoginManager()
mail = Mail()
migrate = Migrate()
db = SQLAlchemy()

def create_app(settings_module):
    app = Flask(__name__)

    app.config.from_object(settings_module)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    CORS(app, support_credentials=True)

    from .public import public_bp
    from .auth import auth_bp
    from .user import user_bp
    from .admin import admin_bp
    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    return app

