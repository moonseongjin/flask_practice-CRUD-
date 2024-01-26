"""
from flask import Flask

app = Flask(__name__)

# 데이터 베이스에 저장함 주로
topics = [
    {'id':1, 'title':'html', 'body': 'html is ...'},
    {'id':2, 'title':'css', 'body': 'css is ...'},
    {'id':3, 'title':'javascript', 'body': 'javascript is ...'}
]


@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="read/{topic["id"]}/">{topic["title"]}</li>'
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            hello, web
        </body>
    </html>
    '''

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