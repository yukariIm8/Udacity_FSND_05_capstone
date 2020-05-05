import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor, Casting, db
import datetime


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.casting_assistant = os.getenv('CASTING_ASSISTANT')
        self.casting_director = os.getenv('CASTING_DIRECTOR')
        self.executive_producer = os.getenv('EXECUTIVE_PRODUCER')
        self.database_name = "agency_test"
        self.database_path = "postgres://{}:{}@{}/{}"\
            .format('postgres', 'postgres', 'localhost:5432',
                    self.database_name)
        setup_db(self.app, self.database_path)
        db.create_all()


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie = {
            'title': 'The Incredible Hulk',
            'release_date': datetime.date(2008, 6, 8),
        }

        self.update_movie = {
            'title': 'The Incredible Hulk',
            'release_date': datetime.date(2050, 6, 8),
        }

        self.new_actor = {
            'name': 'Edward Norton',
            'age': 50,
            'gender': 'male',
        }

        self.update_actor = {
            'name': 'Edward Norto',
            'age': 100,
            'gender': 'male',
        }

        self.new_casting = {
            'actor_id': 8,
            'movie_id': 1,
        }

        self.update_casting = {
            'actor_id': 1,
            'movie_id': 2,
        }

    def tearDown(self):
        """Executed after reach test."""
        pass

    '''
    Movie
    '''
    def test_get_movies_casting_assistant(self):
        """Test all movies are retrieved."""
        res = self.client().get('/movies',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_movies_casting_director(self):
        """Test all movies are retrieved."""
        res = self.client().get('/movies',headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_movies_executive_producer(self):
        """Test all movies are retrieved."""
        res = self.client().get('/movies',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_movies_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_get_movies_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().get('/movie',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_movie_casting_assistant_fail(self):
        """Test 401 is sent when a new movie is created by a casting assistant."""
        res = self.client().post('/movies',headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_create_new_movie_casting_director_fail(self):
        """Test 401 is sent when a new movie is created by a casting director."""
        res = self.client().post('/movies',headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_create_new_movie_executive_producer(self):
        """Test a movie is created."""
        res = self.client().post('/movies',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_movie_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().post('/movies',json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_create_new_movie_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().post('/movie',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_update_movie_casting_assistant_fail(self):
        """Test 401 is sent when a movie is updated by a casting assistant."""
        res = self.client().patch('/movies/5',headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.update_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_update_movie_casting_director(self):
        """Test a movie is updated."""
        res = self.client().patch('/movies/5',headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.update_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie_executive_producer(self):
        """Test a movie is updated."""
        res = self.client().patch('/movies/6',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.update_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().patch('/movies/6',json=self.update_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_update_movie_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().patch('/movies/1000',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.update_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_movie_casting_assistant_fail(self):
        """Test 401 is sent when a movie is deleted by a casting assistant."""
        res = self.client().delete('/movies/4',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        movie = Movie.query.get(4)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_delete_movie_casting_director_fail(self):
        """Test 401 is sent when a movie is deleted by a casting director."""
        res = self.client().delete('/movies/4',headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        movie = Movie.query.get(4)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_delete_movie_executive_producer(self):
        """Test a movie is deleted."""
        res = self.client().delete('/movies/4',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        movie = Movie.query.get(4)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_movie'], 4)
        self.assertIsNone(movie)

    def test_delete_movie_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().delete('/movies/5')
        data = json.loads(res.data)
        movie = Movie.query.get(5)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_delete_movie_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().delete('/movies/1000',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        movie = Movie.query.get(1000)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')
    
    '''
    Actor
    '''
    def test_get_actors_casting_assistant(self):
        """Test all actors are retrieved."""
        res = self.client().get('/actors',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_actors_casting_director(self):
        """Test all actors are retrieved."""
        res = self.client().get('/actors',headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_actors_executive_producer(self):
        """Test all actors are retrieved."""
        res = self.client().get('/actors',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_actors_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_get_actors_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().get('/actor',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_actor_casting_assistant_fail(self):
        """Test 401 is sent when a new actor is created by a casting assistant."""
        res = self.client().post('/actors',headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_create_new_actor_casting_director(self):
        """Test a actor is created."""
        res = self.client().post('/actors',headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_actor_executive_producer(self):
        """Test a actor is created."""
        res = self.client().post('/actors',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_actor_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().post('/actors',json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_create_new_actor_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().post('/actor',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_update_actor_casting_assistant_fail(self):
        """Test 401 is sent when an actor is updated by a casting assistant."""
        res = self.client().patch('/actors/5',headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.update_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_update_actor_casting_director(self):
        """Test an actor is updated."""
        res = self.client().patch('/actors/6',headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.update_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor_executive_producer(self):
        """Test a actor is updated."""
        res = self.client().patch('/actors/7',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.update_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().patch('/actors/7',json=self.update_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_update_actor_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().patch('/actors/1000',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.update_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_actor_casting_assistant_fail(self):
        """Test 401 is sent when an actor is deleted by a casting assistant."""
        res = self.client().delete('/actors/4',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        actor = Actor.query.get(4)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_delete_actor_casting_director(self):
        """Test an actor is deleted."""
        res = self.client().delete('/actors/4',headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        actor = Actor.query.get(4)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_actor'], 4)
        self.assertIsNone(actor)

    def test_delete_actor_executive_producer(self):
        """Test an actor is deleted."""
        res = self.client().delete('/actors/5',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        actor = Actor.query.get(5)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_actor'], 5)
        self.assertIsNone(actor)

    def test_delete_actor_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().delete('/actors/5')
        data = json.loads(res.data)
        actor = Actor.query.get(5)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_delete_actor_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().delete('/actors/1000',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        actor = Actor.query.get(1000)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')
    
    '''
    Casting
    '''
    def test_get_casting_casting_assistant(self):
        """Test all castings are retrieved."""
        res = self.client().get('/casting',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_casting_casting_director(self):
        """Test all castings are retrieved."""
        res = self.client().get('/casting',headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_casting_executive_producer(self):
        """Test all castings are retrieved."""
        res = self.client().get('/casting',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_casting_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().get('/casting')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_get_casting_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().get('/cast',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_casting_casting_assistant_fail(self):
        """Test 401 is sent when a new casting is created by a casting assistant."""
        res = self.client().post('/casting',headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.new_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_create_new_casting_casting_director(self):
        """Test a casting is created."""
        res = self.client().post('/casting',headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_casting_executive_producer(self):
        """Test a casting is created."""
        res = self.client().post('/casting',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_casting_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().post('/casting',json=self.new_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_create_new_casting_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().post('/cast',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_update_casting_casting_assistant_fail(self):
        """Test 401 is sent when a casting is updated by a casting assistant."""
        res = self.client().patch('/casting/5',headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.update_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_update_casting_casting_director(self):
        """Test a casting is updated."""
        res = self.client().patch('/casting/6',headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.update_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_casting_executive_producer(self):
        """Test a casting is updated."""
        res = self.client().patch('/casting/7',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.update_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_casting_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().patch('/casting/7',json=self.update_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_update_casting_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().patch('/casting/1000',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.update_casting)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_casting_casting_assistant_fail(self):
        """Test 401 is sent when a casting is deleted by a casting assistant."""
        res = self.client().delete('/casting/4',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        casting = Casting.query.get(4)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_delete_casting_casting_director(self):
        """Test a casting is deleted."""
        res = self.client().delete('/casting/4',headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        casting = Casting.query.get(4)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_casting'], 4)
        self.assertIsNone(casting)

    def test_delete_casting_executive_producer(self):
        """Test a casting is deleted."""
        res = self.client().delete('/casting/5',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        casting = Casting.query.get(5)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_casting'], 5)
        self.assertIsNone(casting)

    def test_delete_casting_unauthorized_fail(self):
        """Test 401 is sent when the appropriate token is not given."""
        res = self.client().delete('/casting/5')
        data = json.loads(res.data)
        casting = Casting.query.get(5)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_delete_casting_wrong_URL_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().delete('/casting/1000',headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        casting = Casting.query.get(1000)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
