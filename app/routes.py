from flask import render_template, flash, redirect
from app import app
from app.forms import SignUpForm, LoginForm, CarForm

@app.route('/')
def index():
    return render_template('index.jinja', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def show_login_form():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash(f'{login_form.username} successfully signed in!')
        return redirect('/')
    return render_template('login.jinja', login_form=login_form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        flash(f'Request to signup {signup_form.username.data} successful')
        return redirect('/')
    return render_template('signup.jinja', form=signup_form)

@app.route('/carform', methods=['GET', 'POST'])
def show_car_form():
    car_form = CarForm()
    return render_template('car.jinja', car_form=car_form)

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/blog')
def blog():
    return render_template('blog.jinja')


