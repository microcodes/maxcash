import unittest
from flask_testing import TestCase
from app import create_app




class TestBase(TestCase):
	def create_app(self):
		app = create_app('testing')
		return app

	def setUp(self):
		pass

	def tearDown(self):
		pass


if __name__ == "__main__":
	unittest.main()

