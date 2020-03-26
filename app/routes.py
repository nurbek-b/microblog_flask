from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bakyt'}
    posts = [
        {
        'author': {'username': 'Adilet'},
        'body': 'Corona virus is terrifying every body all ower the world'        
        },
        {
        'author': {'username': 'Madina'},
        'body': 'Beautiful day in Bishkek, Bbut evry body sitting at home all day'
        }
    ]   
    return render_template('index.html', title='Home', user=user, posts=posts)



