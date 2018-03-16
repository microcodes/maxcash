from flask_login import UserMixin
from . import db, login_manager
from .util import todays_date


class User(UserMixin ,db.Model):
	__tablename__ = 'user'
	id         = db.Column(db.Integer, primary_key=True)
	seller_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
	email      = db.Column(db.String(255), nullable=False, index=True, unique=True)
	phone      = db.Column(db.String(25), nullable=False, index=True, unique=True)
	password   = db.Column(db.String(255), nullable=False)
	bank_name  = db.Column(db.String(255), nullable=False)
	acc_no     = db.Column(db.String(255), nullable=False, index=True, unique=True)
	acc_name   = db.Column(db.String(255), nullable=False)
	terms      = db.Column(db.Boolean, default=True)
	reg_date   = db.Column(db.String(25), default=todays_date)
	role       = db.Column(db.Enum('crtr', 'intx', 'intxx', name='who_enum'), 
		                   nullable=False, default='intxx')
	stock      = db.Column(db.Integer, default=0)
	status     = db.Column(db.Enum('ready', 'queued', 'buyer', 'stockholder', 'seller', 'frozen', 
		                   name='status_enum'), nullable=False, default='ready')
	order_date = db.Column(db.String(255))
	notice     = db.Column(db.String)
	round      = db.Column(db.Integer, default=0)
	buyers     = db.relationship('User')	



@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))