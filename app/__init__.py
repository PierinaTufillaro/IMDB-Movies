from flask import Flask
from .config import Config
from .models.movie import db
from app.routes.movies_routes import movie_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(movie_bp, url_prefix='/api')

    db.init_app(app)

    with app.app_context():
        db.create_all()  

    return app
