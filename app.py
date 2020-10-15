# flask
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json

# os
import os

# import pandas
import pandas as pd

# initialize app
app = Flask(__name__, template_folder=os.path.abspath('static/templates')) # reference a different path for templates
CORS(app)
# setup database and sqlalchemy dependencies
from sql_setup import setup_dependencies
engine, session, Passing, Rushing = setup_dependencies(app)

# home route
@app.route('/')
def welcome():
    '''Main Dashboard Route.'''

    # get default data
    data = session.query(Passing).order_by(Passing.passing_yards.desc())

    # default dropdowns
    options = populate_dropdown('passing')
    options = options.json
    options = [x.capitalize().replace('_', ' ') for x in options]

    return render_template('index.html', data=data, options=options)

# data return route
@app.route('/<table>/<x>/<y>')
def get_data(table, x, y):

    '''Returns JSON data from user choices.'''

    # group by 
    data = pd.read_sql_table(table, engine)[['name', x, y]]

    return data.to_json()

@app.route('/<table>')
def populate_dropdown(table):

    '''Returns the columns a user can choose from.'''

    exclusions = ['id', 'name', 'birth_place', 'birth_date', 'college', 'experience', 'high_school', 'high_school_location', 'years_played']

    options = [x for x in pd.read_sql_table(table, engine).columns if x not in exclusions]

    return jsonify(options)

@app.route('/table/<table>/<x>/<y>')
def get_table_data(table, x, y):

    '''Returns JSON data from user choices made for bootstrap table.'''

    # group by 
    data = pd.read_sql_table(table, engine)[['name', x, y]]

    table_data = []
    for ind, row in data.iterrows():
        d = {
            'name': row['name'],
            'x': row[x],
            'y': row[y]
        }
        table_data.append(d)

    return jsonify(table_data)

def insert_data():

    '''Runs the data_handler functions to insert data.'''

    import sys
    sys.path.append("..")
    import data_handler
    data_handler.insert_all()

# run app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) # this sets the port to 5000 locally, and ${PORT} environment variable on Heroku
    app.run(host='0.0.0.0', port=port, debug=True)
