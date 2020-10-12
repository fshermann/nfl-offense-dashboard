import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import os
import app

db = SQLAlchemy()

class Rushing(db.Model):
    __tablename__ = 'rushing'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer) 
    games_played = db.Column(db.Integer)
    rushing_attempts = db.Column(db.Integer)
    rushing_yards = db.Column(db.Integer)
    rushing_tds = db.Column(db.Integer)
    rushing_over_20 = db.Column(db.Integer)
    rushing_over_40 = db.Column(db.Integer)
    fumbles = db.Column(db.Integer)

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

        self.name = data['name']
        self.games_played = data['games_played']
        self.rushing_attempts = data['rushing_attempts']
        self.rushing_yards = data['rushing_yards']
        self.rushing_tds = data['rushing_tds']
        self.rushing_over_20 = data['rushing_over_20']
        self.rushing_over_40 = data['rushing_over_40']
        self.fumbles = data['fumbles']

    def __repr__(self):
        return f'<id {self.id}, name {self.name}>'