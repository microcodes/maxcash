from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.models import User
from app.forms import SignUpForm, SignInForm
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse





@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html', title='Dashboard')


@app.route('/buy/<int:id>')
@login_required
def buy(id):
	user = User.query.get(id)
	if user.stock == 0 and user.status == 'ready':
		user.status = 'queued'
		db.session.commit()
		flash('You have successfull place a buy order.', 'success')
		return redirect(url_for('dashboard'))
	flash('Sorry! You can not place a buy order at this moment.', 'warning')
	return redirect(url_for('dashboard'))	


@app.route('/sell/<int:id>')
@login_required
def sell(id):
	seller = User.query.get(id)
	if seller.stock == 2000 and seller.status == 'seller':
		buyers = User.query.filter_by(status='queued').limit(2).all()
		for u in buyers:
			u.seller_id = seller.id
			u.status    = 'buyer'
			u.notice    = 'Congrats! We got you a seller and you are required to make payment \
			               of N1000 within 6 hours into the following bank account information \
			               in order to buy the stock from this seller: \
			               Account Name  : ' + seller.acc_name + ' \
			               Account Number: ' + seller.acc_no + ' \
			               Bank Name     : ' + seller.bank_name + ' \
			               Phone Number  : ' + seller.phone + ' \
			               Before making the payment contact him/her to let them know that you are \
			               about to make the payment.'
		db.session.commit()
		return redirect(url_for('dashboard'))
	elif seller.who == 'crtr' and seller.stock == 20000:
		buyers = User.query.filter_by(status='queued').limit(20).all()
		for u in buyers:
			u.seller_id = seller.id
			u.status    = 'buyer'
			u.notice    = 'Congrats! We got you a seller and you are required to make payment \
			               of N1000 within 6 hours into the following bank account information \
			               in order to buy the stock from this seller: \
			               Account Name  : ' + seller.acc_name + ' \
			               Account Number: ' + seller.acc_no + ' \
			               Bank Name     : ' + seller.bank_name + ' \
			               Phone Number  : ' + seller.phone + ' \
			               Before making the payment contact him/her to let them know that you are \
			               about to make the payment.'
		db.session.commit()
		return redirect(url_for('dashboard'))	               	
	flash('Sorry! You can not sell stock at this moment.', 'warning')
	return redirect(url_for('dashboard'))		


@app.route('/comfirm/<int:id>/<int:sid>')
@login_required
def comfirm(id, sid):
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
			crtr.bonus  += 1
			for i in intx:
				i.bonus = 0.5
	db.session.commit()
	return redirect(url_for('dashboard'))


@app.route('/cancel/<int:id>')
def cancel(id):
	buyer = User.query.get(id)
	if buyer.status == 'queued':
		buyer.status = 'ready'
		db.session.commit()
		flash('Your order was canceled successfull.', 'success')
		return redirect(url_for('dashboard'))
	flash('Sorry! You can not cancel your order at this moment.', 'warning')
	return redirect(url_for('dashboard'))	