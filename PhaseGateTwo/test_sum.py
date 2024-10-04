import unittest
import sum

class testSum(unittest.TestCase):
	def test_that_sum_function_exist(self):
		sum.sum("23","22")
	def test_that_the_sum_function_determines_the_sum(self):
		self.assertIs(sum.sum("23","22"),"45")
		