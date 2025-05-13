from flask import Blueprint, jsonify
from app.models.movie import db, Movie

movie_bp = Blueprint('movie_bp', __name__)

def movie_to_dict(movie):
    return {
        'id': movie.id,
        'title': movie.title,
        'imdb_title_id': movie.imdb_title_id,
        'original_title': movie.original_title,
        'year': movie.year,
        'date_published': movie.date_published,
        'genre': movie.genre,
        'duration': movie.duration,
        'country': movie.country,
        'language': movie.language,
        'director': movie.director,
        'writer': movie.writer,
        'production_company': movie.production_company,
        'actors': movie.actors,
        'description': movie.description,
        'avg_vote': movie.avg_vote,
        'votes': movie.votes,
        'budget': movie.budget,
        'usa_gross_income': movie.usa_gross_income,
        'worldwide_gross_income': movie.worldwide_gross_income,
        'metascore': movie.metascore,
        'reviews_from_users': movie.reviews_from_users,
        'reviews_from_critics': movie.reviews_from_critics
    }

@movie_bp.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()  
    movies_list = [movie_to_dict(movie) for movie in movies]  
    return jsonify(movies_list)  

@movie_bp.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get_or_404(id)  
    return jsonify(movie_to_dict(movie)) 