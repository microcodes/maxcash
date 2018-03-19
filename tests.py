import unittest
from flask import url_for
from flask_testing import TestCase
from app import create_app, db


class TestBase(TestCase):

	def create_app(self):
		return create_app('testing')

	def setUp(self):
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()


class TestAuth(TestBase):
	def test_sign_form_display(self):
		response = self.client.get(url_for('auth.sign_up'))
		self.assertEqual(response.status_code, 200)

	def function():
			pass	


if __name__ == "__main__":
	unittest.main()