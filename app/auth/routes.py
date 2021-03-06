from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from . import auth
from .forms import SignUpForm, SignInForm
from .. import db, mail
from ..models import User


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	if current_user.is_authenticated:
		return redirect(url_for('dash.dashboard'))

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
		flash('Congratulations, you sign up successfull!', 'success')
		return redirect(url_for('auth.sign_in'))
	return render_template('auth/sign_up.html', title='Sign up', form=form)


@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
	if current_user.is_authenticated:
		return redirect(url_for('dash.dashboard'))

	form = SignInForm()
	if form.validate_on_submit():
		user = User.query.filter(User.phone==form.phone.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password', 'danger')
			return redirect(url_for('auth.sign_in'))

		login_user(user)

		if user.role == 'crtr':
			return redirect(url_for('dash.crtr_dashboard'))

		elif user.role == 'intx':
			return redirect(url_for('dash.intx_dashboard'))


		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('auth.sign_in')
		return redirect(next_page)

	return render_template('auth/sign_in.html', title='Sign in', form=form)


@auth.route('/sign-out')
@login_required
def sign_out():
	logout_user()
	return redirect(url_for('auth.sign_in'))