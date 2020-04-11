import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "agency"
database_path = "postgres://umumsiroaumutk:172bca5062ebb16d10626718c623a7970cd4927d7adddc414c1307c0edaeccd8@ec2-3-211-48-92.compute-1.amazonaws.com:5432/ddu1m1p19j96k7"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# Implement Movies with attributes title and release date.

class Movies(db.Model):
    __tablename__ = 'Movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    release = db.Column(db.DateTime())
    actors = db.Column(db.ARRAY(db.Integer), db.ForeignKey('Actors.id'))

    def __init__(self, title, release, actors):
        self.title = title
        self.release = release
        self.actors = actors

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release,
            'actors': self.actors
        }

# Actors with attributes name, age and gender.

class Actors(db.Model):
    __tablename__ = 'Actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    movies = db.relationship('Movies', backref=db.backref('Actors', lazy=True))

    def __init__(self, name, age, gender, movies):
        self.name = name
        self.age = age
        self.gender = gender
        self.movies = movies

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies': self.movies
        }
