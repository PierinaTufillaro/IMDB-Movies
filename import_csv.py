import pandas as pd
from app import create_app
from app.models.movie import db, Movie

app = create_app()

with app.app_context():
    # Cargar el CSV
    df = pd.read_csv('IMDb_movies.csv')

    # Iterar sobre las filas
    for _, row in df.iterrows():
        movie = Movie(
            title=row.get('title'),
            imdb_title_id=row.get('imdb_title_id'),
            original_title=row.get('original_title'),
            year=row.get('year'),
            date_published=row.get('date_published'),
            genre=row.get('genre'),
            duration=row.get('duration'),
            country=row.get('country'),
            language=row.get('language'),
            director=row.get('director'),
            writer=row.get('writer'),
            production_company=row.get('production_company'),
            actors=row.get('actors'),
            description=row.get('description'),
            avg_vote=row.get('avg_vote'),
            votes=row.get('votes'),
            budget=row.get('budget'),
            usa_gross_income=row.get('usa_gross_income'),
            worldwide_gross_income=row.get('worldwide_gross_income'),
            metascore=row.get('metascore'),
            reviews_from_users=row.get('reviews_from_users'),
            reviews_from_critics=row.get('reviews_from_critics')
        )

        db.session.add(movie)

    db.session.commit()
    print("✅ Datos importados exitosamente.")
