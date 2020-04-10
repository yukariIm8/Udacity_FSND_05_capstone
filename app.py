import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)

'''
GET /actors
'''
  @app.route('/actors', methods=['GET'])
  def get_actors():
    """Retrieve all actors."""

    actors = Actors.query.all()
    
    if actors is None:
      abort(404, 'There is no actors data.')

    actors_format = [actor.format() for actor in actors]

    return jsonify({
      'success': True,
      'actors': actors_format
    }), 200

  '''
  GET /movies
  '''
  @app.route('/movies', methods=['GET'])
  def get_movies():
    """Retrieve all movies."""
    movies = Movies.query.all()
    if movies is None:
      abort(404, 'There is no movies data.')

    movies_format = [movie.format() for movie in movies]

    return jsonify({
      'success': True,
      'movies': movies_format
    }), 200

'''
DELETE /actors
'''
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  def delete_actor(actor_id):
    """Delete an actor."""
    actor = Actors.query.get(actor_id)

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
        'delete': actor_id
      }), 200
      db.session.close()

  '''
  DELETE /movies
  '''
  @app.route('/movies/<int:movie_id', methods=['DELETE'])
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
        'delete': movie_id
      }), 200
      db.session.close()

  '''
  POST /actors
  '''
  @app.route('/actors', methods=['POST'])
  def create_actor():
    """Create a new actor."""
    try:
      if request.method != 'POST':
        abort(405)

      data = request.get_json()
      new_name = data.get('name')
      new_age = data.get('age')
      new_gender = data.get('gender')

      actor = Actor(name=new_name, age=new_age, gender=new_gender)
      actor.insert()
    except:
      db.session.rollback()
      abort(422)
    finally:
      return jsonify({
        'success': True,
        'actors': actor.format()
      }), 200
      db.session.close()

  '''
  POST /movies
  '''
  @app.route('/movies', methods=['POST'])
  def create_movie():
    """Create a new movie."""
    try:
      if request.method != 'POST':
        abort(405)

      data request.get_json()
      new_title = data.get('title')
      new_release = data.get('release')
      new_actors = data.getlist('actors')

      movie = Movie(title=new_title, release=new_release, actors=new_actors)
      movie.insert()
    except:
      db.session.rollback()
      abort(422)
    finally:
      return jsonify({
        'success': True,
        'movies': movie.format()
      }), 200
      db.session.close()

  '''
  PATCH /actors
  '''
  @app.route('/actor/<int:actor_id>', methods=['PATCH'])
  def update_actor(actor_id):
    """Update the actor's info."""
    data = request.get_json()
    name = data.get('name')
    gender = data.get('gender')
    age = data.get('age')

    actor = Actors.query.get(actor_id)
    if actor is None:
      abort(404, 'There is no such an actor.')

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
        'actor': actor.format()
      }), 200
      db.session.close()

  '''
  PATCH /movies
  '''
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  def update_movie(movie_id):
    """Update the movie's info."""

    data = request.get_json()
    title = data.get('title')
    release = data.get('release')
    actors = data.getlist('actors')

    movie = Movie.query.get(movie_id)
    if movie is None:
      abort(404, 'There is no such a movie.')
    
    try:
      movie.title = title
      movie.release = release
      movie.actors = actors
      movie.update()
    except:
      db.session.rollback()
      abort(422)
    finally:
      return jsonify({
        'success': True,
        'movie': movie.format() 
      }), 200
      db.session.close()

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)