import unittest
import palindromeprime

class testPalindromeprime(unittest.TestCase):
	def test_that_the_prime_function_exist(self):
		palindromeprime.prime(345)
	
	def test_that_the_prime_number_function_determines_a_prime_number(self):
		self.assertIs(palindromeprime.prime(7), True)
		self.assertIs(palindromeprime.prime(4), False)
	
	def test_that_the_palindrome_function_exist(self):
		palindromeprime.palindrome(134)
	
	def test_is_a_palindrome(self):
		self.assertIs(palindromeprime.palindrome(33), True)
		self.assertIs(palindromeprime.palindrome(86), False)

	def test_for_negative_val(self):
		self.assertRaises(ValueError, palindromeprime.palindrome_prime, -1)

	def test_for_string(self):
		self.assertRaises(TypeError, palindromeprime.palindrome_prime, "error")

	def test_that_palindrome_prime_function_exist(self):
		palindromeprime.palindrome_prime(121)
	
	def test_if_number_is_a_palindrome(self):
		self.assertIs(palindromeprime.palindrome_prime(11),True)

	def test_for_negative_values(self):
		self.assertRaises(ValueError, palindromeprime.palindrome_prime, -6)

	def test_for_string(self):
		self.assertRaises(TypeError, palindromeprime.palindrome_prime, "error")