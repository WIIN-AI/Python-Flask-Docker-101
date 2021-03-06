from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is check ....'


@app.route('/hello')
def hello_world():
    return "hello world - Sample"


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return '--> Revision Number %f' % revNo


# app.add_url_rule("/", 'hello', hello_world)
if __name__ == '__main__':
    # app.run()
    app.run(debug=True) #,host='0.0.0.0'


