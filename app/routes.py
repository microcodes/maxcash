from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.models import User
from app.forms import SignUpForm, SignInForm
from flask_login import login_user

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
			        terms=form.terms.data
			        )
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you sign up successfull!')
		return redirect(url_for('index'))
	return render_template('sign_up.html', title='Sign Up', form=form)


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
	form = SignInForm()
	if form.validate_on_submit():
		user = User.query.filter(User.phone==form.phone.data). \
		                  filter(User.password==form.password.data).first()
		if user is None:
			flash('Invalid phone number or password')
			return redirect(url_for('sign_in'))
		login_user(user, remember=form.remember.data)
		flash('Signed in successfully.')
		return redirect(url_for('dashboard'))
	return render_template('sign_in.html', title='Sign In', form=form)