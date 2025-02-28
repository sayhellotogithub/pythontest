from flaskpj import app
from flask import render_template

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