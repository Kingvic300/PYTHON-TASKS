import unittest
import divide

class TestDivide(unittest.TestCase):
	def test_that_square_function_exist(self):
		divide.square(10)
	def test_that_square_function_determines_the_result(self):
		self.assertEqual(divide.square(10),3.1622776601683795)
		self.assertEqual(divide.square(23),4.6)
	def test_for_negative_val(self):
		self.assertRaises(ValueError,divide.square, -1)
	def test_for_string(self):
		self.assertRaises(TypeError,divide.square,"error")