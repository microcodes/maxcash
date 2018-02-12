from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignUpForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	phone = StringField('Phone Number', validators=[DataRequired(), Length(min=0, max=11)])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Password (repeat)', validators=[DataRequired(), EqualTo('password')])
	bank_name = SelectField('Bank Name', 
		choices=[('1', 'Access Bank'), ('2', 'Citibank'), ('3', 'Diamond Bank'), ('4', 'Ecobank'), 
		         ('5', 'Fidelity Bank'), ('6', 'First Bank'), ('7', 'FCMB'), ('8', 'GT Bank'), 
		         ('9', 'Heritage Bank'), ('10', 'Keystone Bank'), ('11', 'Skye Bank'), ('12', 'Stanbic IBTC'), 
		         ('13', 'Standard Chartered Bank'), ('14', 'Sterling Bank'), ('15', 'Union Bank'), ('16', 'UBA'), 
		         ('17', 'Unity Bank'), ('18', 'Wema Bank'), ('19', 'Zenith Bank')
		        ], validators=[DataRequired()])
	acc_no = StringField('Account Number', validators=[DataRequired(), Length(min=0, max=10)])
	acc_name = StringField('Account Name', validators=[DataRequired()])
	sign_up = SubmitField('Sign Up')


class SignInForm(FlaskForm):
	phone = StringField('Phone Number', validators=[DataRequired(), Length(min=0, max=11)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me on this device')
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