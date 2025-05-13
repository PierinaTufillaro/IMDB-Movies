from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
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
        return f'<Movie {self.title}>'
