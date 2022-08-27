# import Flask
from flask import Flask

# This __name__ variable denotes the name of the current function
# Variables with underscores before and after them are called magic methods
app = Flask(__name__)

# CREATE FLASK ROUTES
# / denotes that we want to put our data at the root of our routes
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/creator')
def by_mike():
    return 'This was created by Mike'