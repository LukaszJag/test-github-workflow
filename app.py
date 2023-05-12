from flask import Flask
app = Flask(__name__)

"""
Flask application instance.
"""

@app.route('/')
def index():
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
