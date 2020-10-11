from flask import Flask, jsonify

app = Flask(__name__)

# home route
@app.route("/")
def welcome():
    """List available api routes."""
    return (
        f'Welcome!!!'
    )

# run app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) # this sets the port to 5000 locally, and ${PORT} environment variable on Heroku
    app.run(host='0.0.0.0', port=port)
