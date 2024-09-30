import unittest
import even
class Testeven(unittest.TestCase):
	def test_even_function_exist(self):
		even.even(1)
	def test_even_for_negative_values(self):
		even.even(-1)
		 
	