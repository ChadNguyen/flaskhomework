from flask import render_template
from app import app

@app.route('/')
def index():
    cdn={
        'instructors':('lucas','dylan'),
        'students':['blane','ashmika','abe','zi','connor','martin','noah','erm']
    }
    return render_template('index.jinja', cdn=cdn, title='Home')

@app.route('/login')
def login():
    return render_template('login.jinja')

@app.route('/register')
def register():
    return render_template('register.jinja')


@app.route('/about')
def about():
    return render_template('about.jinja')


@app.route('/blog')
def blog():
    return render_template('blog.jinja')