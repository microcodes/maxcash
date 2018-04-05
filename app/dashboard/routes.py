from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from . import dash
from .. import db
from ..models import User
from ..tasks import buying, selling, crtr_selling, intx_selling, \
                    confirming, cancelling


@dash.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard/dashboard.html', title='Dashboard')


@dash.route('/crtr-dashboard')
@login_required
def crtr_dashboard():
	if current_user.role != 'crtr':
		abort(403)

	return render_template('dashboard/crtr_dashboard.html', title='Dashboard')


@dash.route('/intx-dashboard')
@login_required
def intx_dashboard():
	if current_user.role != 'intx':
		abort(403)
		
	return render_template('dashboard/intx_dashboard.html', title='Dashboard')


@dash.route('/buy/<int:id>')
@login_required
def buy(id):
	buying.delay(id)
	flash('You have successfully place a buy order.', 'success')
	return redirect(url_for('dash.dashboard'))	


@dash.route('/sell/<int:id>')
@login_required
def sell(id):
	selling.delay(id)	               	
	flash('You have successfully place a sell order.', 'success')
	return redirect(url_for('dash.dashboard'))


@dash.route('/crtr-sell/<int:id>')
@login_required
def crtr_sell(id):
	crtr_selling.delay(id)
	flash('You have successfully place a sell order.', 'success')
	return redirect(url_for('dash.crtr_dashboard'))


@dash.route('/intx-sell/<int:id>')
@login_required
def intx_sell(id):
	intx_selling.delay(id)
	flash('You have successfully place a sell order.', 'success')
	return redirect(url_for('dash.intx_dashboard'))


@dash.route('/confirm/<int:id>/<int:sid>')
@login_required
def confirm(id, sid):
	confirming.delay(id, sid)
	flash('You have successfully confirm this payment.', 'success')
	return redirect(url_for('dash.dashboard'))


@dash.route('/cancel/<int:id>')
@login_required
def cancel(id):
	cancelling.delay(id)
	flash('Your order was canceled successfully.', 'success')
	return redirect(url_for('dash.dashboard'))