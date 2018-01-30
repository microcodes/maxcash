from app import app, r
from flask import render_template
from app.forms import SignUpForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/sign-up')
def sign_up():
	form = SignUpForm()
	return render_template('sign_up.html', form=form)