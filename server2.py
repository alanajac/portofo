from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index2.html')

@app.route('/<username>/<int:post_id>')
def user(username=None,post_id=None):
    return render_template('index2.html',name=username,post_id=post_id)

@app.route('/about2.html')
def about():
    return render_template('about2.html')

#@app.route('/favicon.ico')
#def fav():
#    return 'These are my thoughts on blogs'

@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs'

@app.route('/blog/2022/dogs')
def dogs():
    return 'au au'