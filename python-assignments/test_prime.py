import unittest
import get_prime

class Testrime(unittest.TestCase):
	def test_that_prime_function_exist(self):
		prime.get_prime(3)
	def test_that_prime_function_returns_prime_result(self):
		self.assertEqual(prime.get_prime(10), 1000)
		self.assertEqual(prime.get_prime(7), 343)
		self.assertEqual(prime.get_prime(2), 8)
	def test_that_prime_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError,prime.get_prime, -3)

