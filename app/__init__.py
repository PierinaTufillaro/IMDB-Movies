from flask import Flask
from .config import Config
from .models.movie import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # 🔥 Esto crea la base y las tablas

    return app
