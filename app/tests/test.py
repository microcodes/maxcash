import unittest
from app import create_app


app = create_app('testing')

class MaxcashTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		#self.assertEquals(app.debug, False)
		pass

	def tearDown(self):
		pass

	def test_main_page(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertIn(b'MaxCash', response.data)
		self.assertIn(b'Naira trading platform', response.data)
		self.assertIn(b'Sign Up', response.data)
		self.assertIn(b'Sign In', response.data)


if __name__ == "__main__":
	unittest.main()

