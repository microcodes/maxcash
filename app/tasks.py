from . import celery, db
from .models import User
from .util import todays_date, date_diff


@celery.task
def buying(id):
	buyer = User.query.get(id)
	if buyer.stock == 0 and buyer.status == 'ready':
		buyer.status = 'queued'
		db.session.commit()


@celery.task
def selling(id):
	seller = User.query.get(id)
	if seller.stock == 2000 and seller.status == 'seller':
		buyers = User.query.filter_by(status='queued').limit(2).all()
		for u in buyers:
			u.seller_id  = seller.id
			u.status     = 'buyer'
			u.pair_date  = todays_date
			u.notice     = '<p><strong>Account Name  : </strong>' + seller.acc_name  + '</p> \
			                <p><strong>Account Number: </strong>' + seller.acc_no    + '</p> \
			                <p><strong>Bank Name     : </strong>' + seller.bank_name + '</p> \
			                <p><strong>Phone Number  : </strong>' + seller.phone     + '</p>'               
		db.session.commit()


@celery.task
def crtr_selling(id):
	seller = User.query.get(id)
	buyers = User.query.filter_by(status='queued').limit(2).all()
	for u in buyers:
		u.seller_id  = seller.id
		u.status     = 'buyer'
		u.pair_date  = todays_date
		u.notice     = '<p><strong>Account Name  : </strong>' + seller.acc_name  + '</p> \
		                <p><strong>Account Number: </strong>' + seller.acc_no    + '</p> \
		                <p><strong>Bank Name     : </strong>' + seller.bank_name + '</p> \
		                <p><strong>Phone Number  : </strong>' + seller.phone     + '</p>'               
	db.session.commit()


@celery.task
def intx_selling(id):
	seller = User.query.get(id)
	buyers = User.query.filter_by(status='queued').limit(2).all()
	for u in buyers:
		u.seller_id  = seller.id
		u.status     = 'buyer'
		u.pair_date  = todays_date
		u.notice     = '<p><strong>Account Name  : </strong>' + seller.acc_name  + '</p> \
		                <p><strong>Account Number: </strong>' + seller.acc_no    + '</p> \
		                <p><strong>Bank Name     : </strong>' + seller.bank_name + '</p> \
		                <p><strong>Phone Number  : </strong>' + seller.phone     + '</p>'               
	db.session.commit()			               


@celery.task
def confirming(id, sid):
	seller = User.query.get(sid)
	for x in seller.buyers:
		if x.id == id:
			crtr = User.query.filter_by(role='crtr').first()
			intx = User.query.filter_by(role='intx').all()
			x.stock     = 1000
			x.status    = 'stockholder'
			x.notice    = ''
			x.seller_id = 0
			x.earn_date = todays_date
			seller.stock -= 1000
			if len(seller.buyers) == 0:
				seller.status = 'ready'
				seller.round  += 1
			crtr.stock  += 100
			for i in intx:
				i.stock = 20
	db.session.commit()			


@celery.task
def cancelling(id):
	buyer = User.query.get(id)
	if buyer.stock == 0 and buyer.status == 'queued':
		buyer.status = 'ready'
		db.session.commit()


@celery.task
def profit():
	"""
	stockholders = User.query.filter_by(status='stockholder').all()
	for x in stockholders:
		if x.stock != 2000:
			if date_diff(x.earn_date, todays_date) >= 12:
				x.stock += 500
		#elif x.stock == 2000:
		x.status = 'seller'
	db.session.commit()
	"""
	return 'I am Profitting'		


@celery.task
def re_sell():
	"""
	buyers = User.query.filter_by(status='buyer').all()
	for x in buyer:
		if date_diff(x.pair_date, todays_date) >= 12:
			seller_id = x.seller_id
			x.seller_id = 0
			x.status = 'frozen'
			x.pair_date = ''
			x.notice = ''
			seller = User.query.get(seller_id)
			buyer = User.query.filter_by(status='queued').limit(1).all()
			buyer.seller_id = seller.id
			buyer.status = 'buyer'
			buyer.pair_date = todays_date
			buyer.notice = '<p><strong>Account Name  : </strong>' + seller.acc_name  + '</p> \
			                <p><strong>Account Number: </strong>' + seller.acc_no    + '</p> \
			                <p><strong>Bank Name     : </strong>' + seller.bank_name + '</p> \
			                <p><strong>Phone Number  : </strong>' + seller.phone     + '</p>'
	db.session.commit()
	"""
	return 'I am re-selling'