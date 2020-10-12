# flask
from flask import Flask, jsonify, render_template

# os
import os

# initialize app
app = Flask(__name__, template_folder=os.path.abspath('static/templates')) # reference a different path for templates

# setup database and sqlalchemy dependencies
from sql_setup import setup_dependencies
engine, session = setup_dependencies(app)

# home route
@app.route('/')
def welcome():
    '''Home page route.'''

    return render_template('index.html')

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
