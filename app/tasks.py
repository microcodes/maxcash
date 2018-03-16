from . import celery, db
from .model import User


@celery.task
def buy(id):
	investor = User.query.get(id)
	if investor.stock == 0 and investor.status == 'ready':
		investor.status = 'queued'
		db.session.commit()


@celery.task
def sell():
	pass


@celery.task
def confirm():
	pass


@celery.task
def cancel():
	pass


def re_sell():
	pass


def crtr_sell():
	pass


def intx_sell():
	pass


@celery.task(name='tasks.print')
def print_hello():
	print('Hello, muslim!')