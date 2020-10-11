from flask import Flask, jsonify, render_template
import os

app = Flask(__name__, template_folder=os.path.abspath('static/templates')) # reference a different path for templates

# home route
@app.route('/')
def welcome():
    '''Home page route.'''

    return render_template('index.html')

# run app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) # this sets the port to 5000 locally, and ${PORT} environment variable on Heroku
    app.run(host='0.0.0.0', port=port)
