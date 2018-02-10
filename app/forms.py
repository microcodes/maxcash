from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignUpForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	phone = StringField('Phone Number', validators=[DataRequired(), Length(min=0, max=11)])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Password (repeat)', validators=[DataRequired(), EqualTo('password')])
	terms = BooleanField('Terms & Conditions', validators=[DataRequired()])
	sign_up = SubmitField('Sign Up')


class SignInForm(FlaskForm):
	phone = StringField('Phone Number', validators=[DataRequired(), Length(min=0, max=11)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	sign_in = SubmitField('Sign In')


"""
class EmailForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])


class AccountForm(FlaskForm):
	bank_name = SelectField('Bank Name', validators=[DataRequired()])
	acc_no = StringField('Account Number', validators=[DataRequired(), Length(min=0, max=10)])
	acc_name = StringField('Account Name', validators=[DataRequired()])
	save = SubmitField('Save')
"""	