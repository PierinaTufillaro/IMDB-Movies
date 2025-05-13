import unittest
from app import create_app, db
from app.models.movie import Movie

class MovieEndpointTestCase(unittest.TestCase):
    """
    Test case for the Movie API endpoints.
    """

    def setUp(self):
        """
        Set up the Flask test application and create an in-memory database.
        Adds two sample movies to the database.
        """
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            movie = Movie(
                imdb_title_id="tt1234567",
                title="Inception",
                original_title="Inception",
                year=2010
            )
            movie1 = Movie(
                imdb_title_id="tt7654321",
                title="Interstellar",
                original_title="Interstellar",
                year=2014
            )
            movie2 = Movie(
                imdb_title_id="tt7654322",
                title="Personal",
                original_title="Personal",
                year=2014
            )
                    
            db.session.add_all([movie, movie1, movie2])
            db.session.commit()
            
    def tearDown(self):
        """
        Tear down the database after each test.
        """
        with self.app.app_context():
            db.drop_all()

    def test_get_movie_that_exists_by_title(self):
        """
        Test retrieving a specific movie by its title.
        Should return one matching movie.
        """
        response = self.client.get('/api/movies?title=In')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        
    def test_get_movie_that_exists_by_title_case_insensitive(self):
        """
        Test retrieving a specific movie by its title.
        Should return one matching movie.
        """
        response = self.client.get('/api/movies?title=INCePtION')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Inception")
        
    def test_get_movie_that_not_exists_by_title(self):
        """
        Test retrieving a specific movie by its title.
        Should return none matching movie.
        """
        response = self.client.get('/api/movies?title=pat')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'No movies found with the given title')
        
    def test_get_movie_all_movies(self):
        """
        Test retrieving all movies when no title filter is applied.
        Should return all movies in the database.
        """
        response = self.client.get('/api/movies')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)        
        self.assertEqual(len(data), 3)

if __name__ == '__main__':
    unittest.main()
