import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor, Casting, db

def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resource={r"/api.*": {"origin": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow_Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Contorl-Allow_Methods',
                             'GET,POST,PATCH,DELETE')
        return response

    @app.route('/')
    def hello():
      return jsonify({'message': 'hello'})


    '''
    Movie
    '''
    @app.route('/movies', methods=['GET'])
    def get_movies():
        """Retrieve all movies."""
        movies = Movie.query.all()

        if movies is None:
            abort(404, 'There is no movie data.')

        movies_format = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': movies_format
        }), 200

    @app.route('/movies', methods=['POST'])
    def create_movie():
        """Create a new movie."""
        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            title = data.get('title')
            release_date = data.get('release_date')

            new_movie = Movie(title=title, release_date=release_date)
            new_movie.insert()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'new_movie': new_movie.format()
            }), 200
            db.session.close()

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def update_movie(movie_id):
        """Update the movie's info."""
        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404, 'There is no such a movie.')

        data = request.get_json()
        title = data.get('title')
        release_date = data.get('release_date')

        try:
            movie.title = title
            movie.release_date = release_date
            movie.update()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'updated_movie': movie.format()
            }), 200
            db.session.close()

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):
        """Delete a movie."""
        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404, 'There is no such a movie.')

        try:
            movie.delete()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'deleted_movie': movie_id
            }), 200
            db.session.close()

    '''
    Actor
    '''
    @app.route('/actors', methods=['GET'])
    def get_actors():
        """Retrieve all actors."""
        actors = Actor.query.all()

        if actors is None:
            abort(404, 'There is no actor data.')

        actors_format = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors_format
        }), 200

    @app.route('/actors', methods=['POST'])
    def create_actor():
        """Create a new actor."""
        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            name = data.get('name')
            age = data.get('age')
            gender = data.get('gender')

            new_actor = Actor(name=name, age=age, gender=gender)
            new_actor.insert()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'new_actor': new_actor.format()
            }), 200
            db.session.close()

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def update_actor(actor_id):
        """Update the actor's info."""
        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404, 'There is no such an actor.')

        data = request.get_json()
        name = data.get('name')
        gender = data.get('gender')
        age = data.get('age')

        try:
            actor.name = name
            actor.gender = gender
            actor.age = age
            actor.update()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'updated_actor': actor.format()
            }), 200
            db.session.close()

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def delete_actor(actor_id):
        """Delete an actor."""
        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404, 'There is no such an actor.')

        try:
            actor.delete()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'deleted_actor': actor_id
            }), 200
            db.session.close()

    '''
    Casting
    '''
    @app.route('/casting', methods=['GET'])
    def get_casting():
        """Retrieve all casting information."""
        casting = Casting.query.all()

        if casting is None:
            abort(404, 'There is no castin info.')

        casting_format = [cast.format() for cast in casting]

        return jsonify({
            'success': True,
            'casting': casting_format
        }), 200

    @app.route('/casting', methods=['POST'])
    def create_casting():
        """Create a new actor."""
        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            actor_id = data.get('actor_id')
            movie_id = data.get('movie_id')

            new_casting = Casting(actor_id=actor_id, movie_id=movie_id)
            new_casting.insert()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'new_casting': new_casting.format()
            }), 200
            db.session.close()

    @app.route('/casting/<int:casting_id>', methods=['PATCH'])
    def update_casting(casting_id):
        """Update the casting's info."""
        casting = Casting.query.get(casting_id)

        if casting is None:
            abort(404, 'There is no such a casting.')

        data = request.get_json()
        actor_id = data.get('actor_id')
        movie_id = data.get('movie_id')

        try:
            casting.actor_id = actor_id
            casting.movie_id = movie_id
            casting.update()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'updated_casting': casting.format()
            }), 200
            db.session.close()

    @app.route('/casting/<int:casting_id>', methods=['DELETE'])
    def delete_casting(casting_id):
        """Delete a casting."""
        casting = Casting.query.get(casting_id)

        if casting is None:
            abort(404, 'There is no such a casting.')

        try:
            casting.delete()
        except:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'deleted_casting': casting_id
            }), 200
            db.session.close()

    '''
    Error Handling
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(500)
    def internal_sever_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
