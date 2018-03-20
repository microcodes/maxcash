from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
from .util import todays_date


class User(UserMixin ,db.Model):
	__tablename__ = 'user'
	id         = db.Column(db.Integer, primary_key=True)
	seller_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
	email      = db.Column(db.String, nullable=False, index=True, unique=True)
	phone      = db.Column(db.String, nullable=False, index=True, unique=True)
	password   = db.Column(db.String, nullable=False)
	bank_name  = db.Column(db.String, nullable=False)
	acc_no     = db.Column(db.String, nullable=False, index=True, unique=True)
	acc_name   = db.Column(db.String, nullable=False)
	terms      = db.Column(db.Boolean, default=True)
	reg_date   = db.Column(db.String, default=todays_date)
	role       = db.Column(db.Enum('crtr', 'intx', 'intxx', name='who_enum'), 
		                   nullable=False, default='intxx')
	stock      = db.Column(db.Integer, default=0)
	status     = db.Column(db.Enum('ready', 'queued', 'buyer', 'stockholder', 'seller', 'selling', 'frozen', 
		                   name='status_enum'), nullable=False, default='ready')
	order_date = db.Column(db.String)
	notice     = db.Column(db.String)
	round      = db.Column(db.Integer, default=0)
	buyers     = db.relationship('User')

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))