from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignUpForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	bank_name = StringField('Bank Name', validators=[DataRequired()])
	acc_no = IntegerField('Account Number', validators=[Length(min=0, max=10)])
	acc_name = StringField('Account Name', validators=[DataRequired()])
	phone = IntegerField('Phone Number', validators=[Length(min=0, max=11)])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Password (repeat)', validators=[DataRequired(), EqualTo('password')])
	terms = BooleanField('Terms & Conditions', validators=[DataRequired()])
	submit = SubmitField('Sign Up')