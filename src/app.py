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
    app.run(debug=True)
