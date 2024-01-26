"""
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return str(random.random())
# random.random()으로 하면 문자열이 아니라서 에러. return값에 문자열 넣어줘야함
app.run(debug=True)
"""