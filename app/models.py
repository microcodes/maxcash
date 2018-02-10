from app import db, login_manager
from flask_login import UserMixin

"""
posts_keywords = db.Table('posts_keywords',
	db.Column('post_id', db.ForeignKey('posts.id'), primary_key=True),
	db.Column('keyword_id', db.ForeignKey('keywords.id'), primary_key=True)
	)


class Address(db.Model):
	__tablename__ = 'addresses'
	id = db.Column(db.Integer, primary_key=True)
	email_address = db.Column(db.String, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	user = db.relationship('User', back_populates='addresses')

	def __repr__(self):
		return "<Address(email_address='%s')>" % self.email_address


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	fullname = db.Column(db.String)
	password = db.Column(db.String)

	addresses = db.relationship('Address', back_populates='user',
		cascade='all, delete, delete-orphan')

	posts = db.relationship('BlogPost', 
		back_populates='author', lazy='dynamic')

	def __repr__(self):
		return "<User(name='%s', fullname'%s', password='%s')>" % (
			   self.name, self.fullname, self.password)


class BlogPost(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	headline = db.Column(db.String(255), nullable=False)
	body = db.Column(db.Text)

	keywords = db.relationship('Keyword', 
		secondary=posts_keywords, back_populates='posts')

	author = db.relationship('User', back_populates='posts')

	def __init__(self, headline, body, author):
		self.author = author
		self.headline = headline
		self.body = body

	def __repr__(self):
		return 'BlogPost(%r, %r, %r)' % (self.headline,
			self.body, self.author)


class Keyword(db.Model):
	__tablename__ = 'keywords'
	id = db.Column(db.Integer, primary_key=True)
	keyword = db.Column(db.String(50), nullable=False, unique=True)

	posts = db.relationship('BlogPost', 
		secondary=posts_keywords, back_populates='keywords')

	def __init__(self, keyword):
		self.keyword = keyword
"""		

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id        = db.Column(db.Integer, primary_key=True)
	email     = db.Column(db.String(255), nullable=False, index=True, unique=True)
	phone     = db.Column(db.String(11), nullable=False, index=True, unique=True)
	password  = db.Column(db.String(255), nullable=False)
	terms     = db.Column(db.Boolean)
	credit    = db.Column(db.String(25))
	status    = db.Column(db.String(25))
	sellerId  = db.Column(db.String(25), index=True, unique=True)

	def __repr__(self):
		return '%s' % self.email

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))