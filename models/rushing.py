import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import os

db = SQLAlchemy()

class Rushing(db.Model):
    __tablename__ = 'rushing'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String) 
    games_played = db.Column(db.Integer)
    rushing_attempts = db.Column(db.Integer)
    rushing_yards = db.Column(db.Integer)
    rushing_tds = db.Column(db.Integer)
    rushing_over_20 = db.Column(db.Integer)
    rushing_over_40 = db.Column(db.Integer)
    fumbles = db.Column(db.Integer)
    birth_place = db.Column(db.String)
    birth_date = db.Column(db.String)
    college =db.Column(db.String)
    experience = db.Column(db.String)
    height = db.Column(db.String)
    weight = db.Column(db.String)
    high_school = db.Column(db.String)
    high_school_location = db.Column(db.String)
    years_played =db.Column(db.String)

    def __init__(self, data):

        '''
        
        Data is expected to be a dictionary that has keys equal to:
            id 
            name 
            games_played
            rushing_attempts
            rushing_yards
            rushing_tds
            rushing_over_20
            rushing_over_40
            fumbles

        '''

        self.id = data['id']
        self.name = data['name']
        self.games_played = data['games_played']
        self.rushing_attempts = data['rushing_attempts']
        self.rushing_yards = data['rushing_yards']
        self.rushing_tds = data['rushing_tds']
        self.rushing_over_20 = data['rushing_over_20']
        self.rushing_over_40 = data['rushing_over_40']
        self.fumbles = data['fumbles']
        self.birth_place = data['birth_place']
        self.birth_date = data['birth_date']
        self.college = data['college']
        self.experience = data['experience']
        self.height = data['height']
        self.weight = data['weight']
        self.high_school = data['high_school']
        self.high_school_location = data['high_school_location']
        self.years_played = data['years_played']


    def __repr__(self):
        return f'<id {self.id}, name {self.name}>'