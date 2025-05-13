from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    """
    Represents a Movie in the database.
    
    Attributes:
        id (int): The primary key identifier for the movie.
        imdb_title_id (str): The unique IMDb identifier for the movie.
        title (str): The title of the movie.
        original_title (str): The original title of the movie.
        year (int): The release year of the movie.
        date_published (str): The date when the movie was published.
        genre (str): The genre of the movie.
        duration (str): The duration of the movie.
        country (str): The country where the movie was produced.
        language (str): The language of the movie.
        director (str): The director of the movie.
        writer (str): The writer of the movie.
        production_company (str): The production company of the movie.
        actors (str): The actors involved in the movie.
        description (str): A brief description of the movie.
        avg_vote (float): The average rating of the movie.
        votes (int): The number of votes the movie has received.
        budget (str): The budget of the movie.
        usa_gross_income (str): The gross income of the movie in the USA.
        worldwide_gross_income (str): The worldwide gross income of the movie.
        metascore (str): The metascore of the movie.
        reviews_from_users (str): Reviews from users.
        reviews_from_critics (str): Reviews from critics.
    """
    
    id = db.Column(db.Integer, primary_key=True)
    imdb_title_id = db.Column(db.String(100), unique=True, nullable=True)
    title = db.Column(db.String(200), nullable=False)
    original_title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer)
    date_published = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    duration = db.Column(db.String(100))
    country = db.Column(db.String(100))
    language = db.Column(db.String(100))
    director = db.Column(db.String(100))
    writer = db.Column(db.String(100))
    production_company = db.Column(db.String(100))
    actors = db.Column(db.String(100))
    description = db.Column(db.Text)
    avg_vote = db.Column(db.Float)
    votes = db.Column(db.Integer)
    budget = db.Column(db.String(100))
    usa_gross_income = db.Column(db.String(100))
    worldwide_gross_income = db.Column(db.String(100))
    metascore = db.Column(db.String(100))
    reviews_from_users = db.Column(db.String(100))
    reviews_from_critics = db.Column(db.String(100))

    def __repr__(self):
        """
        Return a string representation of the Movie object.
        
        Returns:
            str: A string representation of the Movie object with its title.
        """
        return f"<Movie {self.title}>"
