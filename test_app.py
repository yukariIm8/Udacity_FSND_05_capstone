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
    def test_get_movies(self):
        """Test all movies are retrieved."""
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_movies_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().get('/movie')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_create_movie(self):
        """Test a movie is created."""
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_movie_fail(self):
        """Test 405 is sent when a wrong URL is given."""
        res = self.client().post('/movies/1', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'method not allowed')

    def test_update_movie(self):
        """Test the movie is updated."""
        res = self.client().patch('/movies/6', json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_movie_fail(self):
        """Test 404 is sent when an invalid movie's id is given."""
        res = self.client().patch('/movies/10000', json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_movie(self):
        """Test the movie is deleted."""
        res = self.client().delete('/movies/4')
        data = json.loads(res.data)
        question = Movie.query.get(4)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_movie'], 4)
        self.assertIsNone(question)

    def test_delete_movie_fail(self):
        """Test 404 is sent when an invalid movie's id is given."""
        res = self.client().delete('/movies/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    '''
    Actor
    '''
    def test_get_actors(self):
        """Test all actors are retrieved."""
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_actors_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().get('/actor')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_create_actor(self):
        """Test an actor is created."""
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_actor_fail(self):
        """Test 405 is sent when a wrong URL is given."""
        res = self.client().post('/movies/1', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'method not allowed')

    def test_update_actor(self):
        """Test the actor is updated."""
        res = self.client().patch('/actors/8', json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_actor_fail(self):
        """Test 404 is sent when an invalid actor's id is given."""
        res = self.client().patch('/actors/10000', json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_actor(self):
        """Test the actor is deleted."""
        res = self.client().delete('/actors/3')
        data = json.loads(res.data)
        actor = Actor.query.get(3)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_actor'], 3)
        self.assertIsNone(actor)

    def test_delete_actor_fail(self):
        """Test 404 is sent when an invalid actor's id is given."""
        res = self.client().delete('/actors/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    '''
    Casting
    '''
    def test_get_casting(self):
        """Test all casting are retrieved."""
        res = self.client().get('/casting')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_casting_fail(self):
        """Test 404 is sent when a wrong URL is given."""
        res = self.client().get('/castin')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_create_casting(self):
        """Test a casting is created."""
        res = self.client().post('/casting', json=self.new_casting)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_casting_fail(self):
        """Test 405 is sent when a wrong URL is given."""
        res = self.client().post('/casting/1', json=self.new_casting)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'method not allowed')

    def test_update_casting(self):
        """Test the casting is updated."""
        res = self.client().patch('/casting/1', json=self.update_casting)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_casting_fail(self):
        """Test 404 is sent when an invalid casting's id is given."""
        res = self.client().patch('/casting/10000', json=self.update_casting)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_casting(self):
        """Test the casting is deleted."""
        res = self.client().delete('/casting/3')
        data = json.loads(res.data)
        casting = Casting.query.get(3)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_casting'], 3)
        self.assertIsNone(casting)

    def test_delete_casting_fail(self):
        """Test 404 is sent when an invalid casting's id is given."""
        res = self.client().delete('/casting/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
