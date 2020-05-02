import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "agency"
database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "agency"
    database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres',
                                                    'localhost:5432',
                                                    database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)


class Movie(db.Model):
    # This Movie table uniquely lists all the movies that the agency involved.
    # There is a 1 to many relationships between Movie and Casting tables.
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    casting = db.relationship('Casting',
                              backref=db.backref('Movie', lazy=True))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Actor(db.Model):
    # This Actor table uniquely lists all the actors who belong to the agency.
    # There is a 1 to many relationships between Actor and Casting tables.
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    casting = db.relationship('Casting',
                              backref=db.backref('Actor', lazy=True,
                                                 cascade='all,delete'))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Casting(db.Model):
    # This Casting table is created for database normalization.
    __tablename__ = 'Casting'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id',
                                                   ondelete='CASCADE'))
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'))

    def __init__(self, actor_id, movie_id):
        self.actor_id = actor_id
        self.movie_id = movie_id

    def format(self):
        return {
            'id': self.id,
            'actor_id': self.actor_id,
            'movie_id': self.movie_id,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
