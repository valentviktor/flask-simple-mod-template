import os
from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from config.database import get_database_uri
from config.logging import setup_logging
from app.providers.extensions import login_manager, db, migrate
from app.providers.routes import register_routes
from app.models.user import User
from app.helpers import env
from datetime import datetime

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(base_dir, '..', '.env'))

    app = Flask(
        __name__, 
        template_folder=os.path.join(os.getcwd(), 'templates'),
        static_folder=os.path.join(os.getcwd(), 'static')
    )

    app.debug = os.getenv('APP_DEBUG', True)

    try:
        app.config['SECRET_KEY'] = os.getenv('APP_KEY')
        app.secret_key = os.getenv('APP_KEY')
        app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        CSRFProtect(app)

        db.init_app(app)
        migrate.init_app(app, db)
        login_manager.init_app(app)

        login_manager.login_view = 'auth.login'
        login_manager.login_message = "Silakan login terlebih dahulu."
        login_manager.login_message_category = "warning"

        @login_manager.user_loader
        def load_user(user_id):
            try:
                return User.query.get(int(user_id))
            except Exception as e:
                app.logger.error(f"Error loading user with ID {user_id}: {str(e)}")
                return None

        setup_logging(app)

        register_routes(app)

        @app.errorhandler(500)
        def internal_error(error):
            app.logger.exception("Internal server error occurred:")
            return "Internal Server Error", 500

        @app.errorhandler(Exception)
        def unhandled_exception(e):
            app.logger.exception("Unhandled Exception:")
            return "An unexpected error occurred", 500

        @app.context_processor
        def inject_env():
            return dict(env=env)
        
        @app.context_processor
        def inject_now():
            return {'now': datetime.utcnow()}
        
        @app.context_processor
        def inject_request():
            return dict(request=request)
        
        with app.app_context():
            db.create_all()
            from init import initialize_users
            initialize_users()


    except Exception as e:  
        app.logger.error(f"An error occurred during app initialization: {str(e)}")
        raise e

    return app
