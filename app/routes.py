from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Car
from app.forms import SignUpForm, LoginForm, CarForm
from app import db, app, login_manager

@app.route('/')
@login_required
def index():
    cars = Car.query.filter_by(user_id=current_user.id).all()
    return render_template('index.jinja', title='Home', cars=cars)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        flash('Logged in successfully.')
        return redirect(url_for('index'))
    return render_template('login.jinja', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        flash(f'{login_form.username} successfully signed in!')
        return redirect('/login')
    return render_template('signin.jinja', login_form=login_form)

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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))








