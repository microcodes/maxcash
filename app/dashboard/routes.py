from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from . import dash
from .. import db, celery
from ..models import User


@celery.task()
def crtr_sell():
	crtr = User.query.filter_by(who='crtr').first()
	if crtr.stock == 2000:
		buyers = User.query.filter_by(status='queued').limit(2).all()
		for u in buyers:
			u.seller_id = crtr.id
			u.status    = 'buyer'
			u.notice    = '<p>Hello! We got you a seller and you are required to make payment \
			               of N1000 within 12 hours into the following bank account information \
			               in order to buy the stock from this seller:</p> \
			               <p>Account Name  : ' + crtr.acc_name + '</p> \
			               <p>Account Number: ' + crtr.acc_no + '</p> \
			               <p>Bank Name     : ' + crtr.bank_name + '</p> \
			               <p>Phone Number  : ' + crtr.phone + '</p> \
			               <p>Before making the payment contact him/her to let them know that you are \
			               about to make the payment so that they will confirm the payment and release \
			               the stock for you.</p>'
		db.session.commit()
		

@celery.task()
def profit():
	stockholders = User.query.filter_by(status='stockholder').all()
	for u in stockholder:
		if u.stock == 1000:
			u.status = 100
		elif u.stock == 2000:
			u.status = 'seller'
	db.session.commit()	

		
crtr_sell.delay()
profit.delay()			


@dash.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard/dashboard.html', title='Dashboard')


@dash.route('/buy/<int:id>')
@login_required
def buy(id):
	user = User.query.get(id)
	if user.stock == 0 and user.status == 'ready':
		user.status = 'queued'
		db.session.commit()
		flash('You have successfull place a buy order.', 'success')
		return redirect(url_for('dash.dashboard'))
	flash('Sorry! You can not place a buy order at your current status.', 'danger')
	return redirect(url_for('dash.dashboard'))	


@dash.route('/sell/<int:id>')
@login_required
def sell(id):
	seller = User.query.get(id)
	if seller.stock == 2000 and seller.status == 'seller':
		buyers = User.query.filter_by(status='queued').limit(2).all()
		for u in buyers:
			u.seller_id = seller.id
			u.status    = 'buyer'
			u.notice    = '<p>Hello! We got you a seller and you are required to make payment \
			               of N1000 within 12 hours into the following bank account information \
			               in order to buy the stock from this seller:</p> \
			               <p>Account Name  : ' + seller.acc_name + '</p> \
			               <p>Account Number: ' + seller.acc_no + '</p> \
			               <p>Bank Name     : ' + seller.bank_name + '</p> \
			               <p>Phone Number  : ' + seller.phone + '</p> \
			               <p>Before making the payment contact him/her to let them know that you are \
			               about to make the payment so that they will confirm the payment and release \
			               the stock for you.</p> '
		db.session.commit()
		return redirect(url_for('dash.dashboard'))	               	
	flash('Sorry! You can not sell stock at your current status.', 'danger')
	return redirect(url_for('dash.dashboard'))		


@dash.route('/confirm/<int:id>/<int:sid>')
@login_required
def confirm(id, sid):
	seller = User.query.get(sid)
	for x in seller.buyers:
		if x.id == id:
			crtr = User.query.filter_by(who='crtr').first()
			intx = User.query.filter_by(who='intx').all()
			x.stock     = 1000
			x.status    = 'stockholder'
			x.notice    = ''
			x.seller_id = 0
			seller.stock -= 1000
			if len(seller.buyers) == 0:
				seller.status = 'ready'
				seller.round  += 1
			crtr.bonus  += 1
			for i in intx:
				i.bonus = 0.5
	db.session.commit()
	return redirect(url_for('dash.dashboard'))


@dash.route('/cancel/<int:id>')
@login_required
def cancel(id):
	buyer = User.query.get(id)
	
	buyer.status = 'ready'
	db.session.commit()
	flash('Your order was canceled successfull.', 'success')
	return redirect(url_for('dashboard'))