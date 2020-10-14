import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import os

db = SQLAlchemy()

class Passing(db.Model):
    __tablename__ = 'passing'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String) 
    games_played = db.Column(db.Integer)
    passing_attempts = db.Column(db.Integer)
    passing_completions = db.Column(db.Integer)
    passing_yards = db.Column(db.Integer)
    passing_tds = db.Column(db.Integer)
    ints = db.Column(db.Integer)
    passing_over_20 = db.Column(db.Integer)
    passing_over_40 = db.Column(db.Integer)
    sacks = db.Column(db.Integer)
    sack_yards = db.Column(db.Integer)
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
            passing_attempts
            passing_completions
            passing_yards
            passing_tds
            ints
            passing_over_20
            passing_over_40
            sacks
            sack_yards

        '''

        self.id = data['id']
        self.name = data['name']
        self.games_played = data['games_played']
        self.passing_attempts = data['passing_attempts']
        self.passing_completions = data['passing_completions']
        self.passing_yards = data['passing_yards']
        self.passing_tds = data['passing_tds']
        self.ints = data['ints']
        self.passing_over_20 = data['passing_over_20']
        self.passing_over_40 = data['passing_over_40']
        self.sacks = data['sacks']
        self.sack_yards = data['sack_yards']
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