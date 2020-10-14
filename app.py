# flask
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# os
import os

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

    # get top 10 passers
    passers = session.query(Passing).order_by(Passing.passing_yards.desc())[0:10]

    # get top 10 rushers
    rushers = session.query(Rushing).order_by(Rushing.rushing_yards.desc())[0:10]

    return render_template('index.html', passers=passers, rushers=rushers)

# passing yards per year data
@app.route('/passing-yards-tds')
def passing_yards_tds():

    '''Returns JSON data of passing yards and touchdowns.'''

    # import pandas
    import pandas as pd

    # group by 
    passing_yards = pd.read_sql_table('passing', engine)[['name', 'passing_yards', 'passing_tds']]

    return passing_yards.to_json()

# passing yards per year data
@app.route('/rushing-yards-tds')
def rushing_yards_tds():

    '''Returns JSON data of passing yards and touchdowns.'''

    # import pandas
    import pandas as pd

    # group by 
    rushing_yards = pd.read_sql_table('rushing', engine)[['name', 'rushing_yards', 'rushing_tds']]

    return rushing_yards.to_json()

def insert_data():

    '''Runs the data_handler functions to insert data.'''

    import sys
    sys.path.append("..")
    import data_handler
    data_handler.insert_all()

# run app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) # this sets the port to 5000 locally, and ${PORT} environment variable on Heroku
    app.run(host='0.0.0.0', port=port)
