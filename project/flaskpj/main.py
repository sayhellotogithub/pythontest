from flaskpj import app
from flask import render_template
from flask import url_for
from markupsafe import escape
from flask import request
import flaskpj.util.login_util as login_util


@app.route('/')
def index():
    books =[{
        'title':'welcome to our python world',
        'price':3000,
        'arrival_day':'2029-08-12'
    },{
         'title':'welcome to flask world',
        'price':2000,
        'arrival_day':'2030-08-12'
    }]
    return render_template('index.html',books=books)

@app.route("/escape_handler/<name>")
def escape_handler(name):
    return render_template('escape_handler.html',backvalue=f"handle data,{escape(name)}")

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f'Post{post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath{escape(subpath)}'

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method == 'POST':
        if login_util.valid_login(request.form['username'],
                       request.form['password']):
            return login_util.log_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    else:
        return render_template('login.html')




with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    print(url_for('escape_handler',name='John Doe'))