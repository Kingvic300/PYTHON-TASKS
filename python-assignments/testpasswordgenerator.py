import unittest
import passwordgenerator

class TestPasswordGenerator(unittest.TestCase):
	def test_that_generates_password_function_exists(self):
		passwordgenerator.generates_password()

	def test_that_generates_password_function_returns_uppercase(self):
		self.assertTrue(any(c for c in passwordgenerator.generates_password() if c.isupper()))
	def test_that_generates_password_function_returns_uppercase(self):
		self.assertFalse(any(c for c in passwordgenerator.generates_password() if c.islower()))