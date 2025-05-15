from flask import Flask
from .config import Config
from .models.movie import db
from app.routes.movies_routes import movie_bp
from flask_cors import CORS


def create_app():
    """
    Create and configure the Flask application.

    Returns:
        app: A Flask application instance.
    """
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3000"])
    app.config.from_object(Config)
    
    app.register_blueprint(movie_bp, url_prefix="/api")

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
