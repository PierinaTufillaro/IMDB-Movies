from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from app import routes  # Fix import statement
    app.register_blueprint(routes.main)

    return app
