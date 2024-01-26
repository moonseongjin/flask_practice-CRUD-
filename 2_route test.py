"""
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/1')
def read():
    return 'read'

@app.route('/read/<id>')
def test(id):
    return 'read ' + id

app.run(debug=True)
"""