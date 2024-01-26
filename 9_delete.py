from flask import Flask, request, redirect

app = Flask(__name__)

nextId = 4 
# 데이터 베이스에 저장함 주로
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

# id안쓰는 곳도 있어서 기본값 None준것
def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/" method="POST"><input type="submit" value="delete">delete</form></li>
        '''
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'    
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')
    # contents, content

@app.route('/read/<int:id>/')
def read(id):
    print(type(id))
    # 그냥 @app.route('/read/<id>/')하면 문자열임.
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    print(title, body)
    # title하고 body값 잘 나오는 지 확인
    return template(getContents(), f'<h2>{title}</h2>{body}', id)

@app.route('/create/', methods=['GET', 'POST'])
def create():
    # request시 GET일 경우, post일경우
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST"> 
                <p><input type = "text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        # GET이 기본값(자바 프레임워크 할 때와 같음)
        # GET은 URL 보이고 POST은 안보이고
        # http://127.0.0.1:5000/creat/
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title =request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId,'title': title, 'body':body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)


@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    # request시 GET일 경우, post일경우
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST"> 
                <p><input type = "text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        # GET이 기본값(자바 프레임워크 할 때와 같음)
        # GET은 URL 보이고 POST은 안보이고
        # http://127.0.0.1:5000/creat/
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title =request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)

# 실수로/일부로 GET으로 들어오는 자들도 있어서 POST로 막음
@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for topic in topics:
        if id == topic['id']:
            topics.remove(topic)
            break
    return redirect('/')

app.run(debug=True)