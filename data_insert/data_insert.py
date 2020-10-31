import app
import pandas as pd
import sys
sys.path.insert(1, 'models')

# import models
from passing import Passing, db
from rushing import Rushing

# database insert function
def insert_passing(data):

    '''Takes data formatted according to passing model and pushes to database.'''

    passing_obj = Passing(data)
    app.session.add(passing_obj)
    app.session.commit()

def insert_rushing(data):

    '''Takes data formatted according to rushing model and pushes to database.'''

    rushing_obj = Rushing(data)
    app.session.add(rushing_obj)
    app.session.commit()

def insert_all_passing():

    '''Inserts processed passing data into postgreSQL database.'''

    # delete the table if it exists
    if app.engine.dialect.has_table(app.engine, 'passing'):

        app.session.query(Passing).delete()
        app.session.commit()

    passing = pd.read_csv('processed_data/passing.csv')

    # loop through each row and insert
    for index, row in passing.iterrows():
        
        # empty dictionary
        data = {}

        # get data
        data['id'] = row['Player Id']
        data['name'] = row['Name']
        data['games_played'] = row['Games Played']
        data['passing_attempts'] = row['Passes Attempted']
        data['passing_completions'] = row['Passes Completed']
        data['passing_yards'] = row['Passing Yards']
        data['passing_tds'] = row['TD Passes']
        data['ints'] = row['Ints']
        data['passing_over_20'] = row['Passes Longer than 20 Yards']
        data['passing_over_40'] = row['Passes Longer than 40 Yards']
        data['sacks'] = row['Sacks']
        data['sack_yards'] = row['Sacked Yards Lost']
        data['birth_place'] = row['Birth Place']
        data['birth_date'] = row['Birthday']
        data['college'] = row['College']
        data['experience'] = row['Experience']
        data['height'] = row['Height (inches)']
        data['weight'] = row['Weight (lbs)']
        data['high_school'] = row['High School']
        data['high_school_location'] = row['High School Location']
        data['years_played'] = row['Years Played']

        # insert record
        insert_passing(data)

def insert_all_rushing():

    '''Inserts processed rushing data into postgreSQL database.'''

    # delete the table if it exists
    if app.engine.dialect.has_table(app.engine, 'rushing'):
        app.session.query(Rushing).delete()
        app.session.commit()

    rushing = pd.read_csv('processed_data/rushing.csv')

    # loopf through each row and insert
    for index, row in rushing.iterrows():
        
        # empty dictionary
        data = {}

        # get data
        data['id'] = row['Player Id']
        data['name'] = row['Name']
        data['games_played'] = row['Games Played']
        data['rushing_attempts'] = row['Rushing Attempts']
        data['rushing_yards'] = row['Rushing Yards']
        data['rushing_tds'] = row['Rushing TDs']
        data['rushing_over_20'] = row['Rushing More Than 20 Yards']
        data['rushing_over_40'] = row['Rushing More Than 40 Yards']
        data['fumbles'] = row['Fumbles']
        data['birth_place'] = row['Birth Place']
        data['birth_date'] = row['Birthday']
        data['college'] = row['College']
        data['experience'] = row['Experience']
        data['height'] = row['Height (inches)']
        data['weight'] = row['Weight (lbs)']
        data['high_school'] = row['High School']
        data['high_school_location'] = row['High School Location']
        data['years_played'] = row['Years Played']

        # insert record
        insert_rushing(data)

def insert_all():

    '''Wrapper for all insertion functions available in this file.'''

    insert_all_passing()
    insert_all_rushing()