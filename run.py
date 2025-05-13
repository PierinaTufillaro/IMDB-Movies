from app import create_app
from app.routes.movies_routes import movie_bp

app = create_app()

app.register_blueprint(movie_bp, url_prefix='/api')  

if __name__ == '__main__':
    app.run(debug=True)
