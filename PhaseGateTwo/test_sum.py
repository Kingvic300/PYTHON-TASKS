import unittest
import sum

class testSum(unittest.TestCase):
	def test_that_sum_function_exist(self):
		sum.sum('23','22')
	def test_that_the_sum_function_determines_the_sum(self):
		self.assertEqual(sum.sum('23','22'),'45')
	def test_for_negative_values(self):
		self.assertEqual(sum.sum('-23','-22'),'-45') 	
	def test_for_strings(self):
		self.assertRaises(TypeError,sum.sum,"error")