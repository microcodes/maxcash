from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class SignUpForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	phone = StringField('Phone Number', validators=[DataRequired(), Length(min=11, max=11, 
		 											message='This field must be 11 digits long.')])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Password (repeat)', validators=[DataRequired(), EqualTo('password')])
	bank_name = SelectField('Bank Name', 
		choices=[('--- select ---', '--- select ---'), 
		         ('Access Bank', 'Access Bank'), ('Citibank', 'Citibank'), 
		         ('Diamond Bank', 'Diamond Bank'), ('Ecobank', 'Ecobank'), 
		         ('Fidelity Bank', 'Fidelity Bank'), ('First Bank', 'First Bank'), 
		         ('FCMB', 'FCMB'), ('GT Bank', 'GT Bank'), 
		         ('Heritage Bank', 'Heritage Bank'), ('Keystone Bank', 'Keystone Bank'), 
		         ('Skye Bank', 'Skye Bank'), ('Stanbic IBTC', 'Stanbic IBTC'), 
		         ('Standard Chartered Bank', 'Standard Chartered Bank'), ('Sterling Bank', 'Sterling Bank'), 
		         ('Union Bank', 'Union Bank'), ('UBA', 'UBA'), 
		         ('Unity Bank', 'Unity Bank'), ('Wema Bank', 'Wema Bank'), ('Zenith Bank', 'Zenith Bank')
		        ])
	acc_no = StringField('Account Number', validators=[DataRequired(), Length(min=10, max=10, 
		                                               message='This field must be 11 digits long.')])
	acc_name = StringField('Account Name', validators=[DataRequired()])
	sign_up = SubmitField('Sign up')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('This email address is already in use.')

	def validate_phone(self, phone):
		user = User.query.filter_by(phone=phone.data).first()
		if user is not None:
			raise ValidationError('This phone number is already in use.')

	def validate_bank_name(self, bank_name):
		if bank_name.data == '--- select ---':
			raise ValidationError('Select a proper bank name.')

	def validate_acc_no(self, acc_no):
		user = User.query.filter_by(acc_no=acc_no.data).first()
		if user is not None:
			raise ValidationError('This account number is already in use.')

	def validate_acc_name(self, acc_name):
		user = User.query.filter_by(acc_name=acc_name.data).first()
		if user is not None:
			raise ValidationError('This account name is already in use.')		


class SignInForm(FlaskForm):
	phone = StringField('Phone Number', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	sign_in = SubmitField('Sign in')

	def validate_phone(self, phone):
		user = User.query.filter_by(phone=phone.data).first()
		if user is None:
			raise ValidationError('Invalid phone number')

	def validate_password(self, password):
		user = User.query.filter_by(password=password.data).first()
		if user is None:
			raise ValidationError('Invalid password')		


"""
class EmailForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])


class AccountForm(FlaskForm):
	bank_name = SelectField('Bank Name', validators=[DataRequired()])
	acc_no = StringField('Account Number', validators=[DataRequired(), Length(min=0, max=10)])
	acc_name = StringField('Account Name', validators=[DataRequired()])
	save = SubmitField('Save')
"""	