
import unittest
import investment

class Testinvestmentplan(unittest.TestCase):
	def test_that_get_investment_exists(self):
		investment.get_investment(1,1,1)
	
	def test_for_small_and_large_number(self):
		self.assertEqual(investment.get_investment(1000, 7, 10))
		self.assertEqual(investment.get_investment(2500, 55.5, 8))

	def test_for_string_input(self):
		self.assertRaises(ValueError,investment,"String")	
	
	def test_to_check_possible_edge_cases(self):
		self.assertEqual(investment.get_investment(0, 5, 10),0)
		self.assertEqual(investment.get_investment(1000, 0, 10),1000)
		self.assertEqual(investment.get_investment(1000, 5, 0),1000)
		
	def test_for_negative_values(self):
		self.assertRaises(ValueError, investment, (-1000, 5, 10))
		self.assertRaises(ValueError, investment, (1000, -5, 10))
		self.assertRaises(ValueError, investment, (1000, 5, -10))

		