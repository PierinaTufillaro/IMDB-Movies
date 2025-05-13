from flask import Blueprint, jsonify, request
from app.models.movie import db, Movie

movie_bp = Blueprint("movie_bp", __name__)


def movie_to_dict(movie):
    """
    Convert a Movie object to a dictionary representation.

    Args:
        movie (Movie): A Movie instance.

    Returns:
        dict: A dictionary containing the movie's attributes.
    """

    return {
        "id": movie.id,
        "title": movie.title,
        "imdb_title_id": movie.imdb_title_id,
        "original_title": movie.original_title,
        "date_published": movie.date_published,
        "genre": movie.genre,
        "duration": movie.duration,
        "country": movie.country,
        "language": movie.language,
        "director": movie.director,
        "writer": movie.writer,
        "production_company": movie.production_company,
        "actors": movie.actors,
        "description": movie.description,
        "avg_vote": movie.avg_vote,
        "votes": movie.votes,
        "budget": movie.budget,
        "usa_gross_income": movie.usa_gross_income,
        "worldwide_gross_income": movie.worldwide_gross_income,
        "metascore": movie.metascore,
        "reviews_from_users": movie.reviews_from_users,
        "reviews_from_critics": movie.reviews_from_critics,
    }


@movie_bp.route("/movies", methods=["GET"])
def get_movies_by_title():
    """
    GET endpoint to retrieve movies based on a partial title match.

    Query Parameters:
        title (str, optional): A substring to search for in movie titles.
                               If not provided, all movies are returned.

    Returns:
        Response: A JSON list of movies if found, or an error message with
                  a 404 status code if no matching movies are found.
    """

    title_query = request.args.get("title")

    if title_query:
        movies = Movie.query.filter(Movie.title.ilike(f"%{title_query}%")).all()
        if not movies:
            return jsonify({"error": "No movies found with the given title"}), 404
    else:
        movies = Movie.query.all()

    movies_list = [movie_to_dict(m) for m in movies]
    return jsonify(movies_list)
