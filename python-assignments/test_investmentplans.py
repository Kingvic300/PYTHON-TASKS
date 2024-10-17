
import unittest
import investment

class Testinvestmentplan(unittest.TestCase):
	def test_investment_function_exist(self):
		investment.get_investment(3,12,4)
	def test_that_investment_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError,investment.get_investment,-3,-4,-9)
	def test_that_investment_function_returns_investment_result(self):
		self.assertEqual(investment.get_investment, (12,5,20))