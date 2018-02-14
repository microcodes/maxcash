from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.models import User
from app.forms import SignUpForm, SignInForm
from flask_login import login_user, login_required, logout_user

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	form = SignUpForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					phone=form.phone.data, 
			        password=form.password.data,
			        bank_name=form.bank_name.data, 
			        acc_no=form.acc_no.data, 
			        acc_name=form.acc_name.data 
			        )
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you sign up successfull!')
		return redirect(url_for('sign_in'))
	return render_template('sign_up.html', title='Sign up', form=form)


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
	form = SignInForm()
	if form.validate_on_submit():
		user = User.query.filter(User.phone==form.phone.data). \
		                  filter(User.password==form.password.data).first()
		if user is None:
			flash('Invalid phone number or password')
			return redirect(url_for('sign_in'))
		login_user(user)
		flash('Signed in successfully.')
		return redirect(url_for('dashboard'))
	return render_template('sign_in.html', title='Sign in', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html', title='Dashboard')


@app.route('/sign-out')
@login_required
def sign_out():
	logout_user()
	return redirect(url_for('index'))
