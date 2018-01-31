from app import app, r
from flask import render_template, flash, redirect, url_for, request
from app.forms import SignUpForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	form = SignUpForm()
	if request.method == 'POST':
		flash('Hi ' + str(form.acc_name.data) + ' you are not registered yet \
		because the system is not yet completed. \
		But you can check time to time to see the development is going')
		return redirect(url_for('index'))
	return render_template('sign_up.html', form=form)