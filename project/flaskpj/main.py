from flaskpj import app
from flask import render_template
from markupsafe import escape

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

