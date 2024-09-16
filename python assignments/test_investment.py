
import unittest
import investment

class TestDivideorsquare(unittest.TestCase):
	def test_that_get_investment_exists(self):
		investment.get_investment(1,1,1)
	
	def test_for_accurate_result_for_small_and_large_number_entries(self):
		self.assertEqual(investment.get_investment(1000, 5, 10),1364.009)
		self.assertEqual(investment.get_investment(2500, 4.5, 8),3580.912)

	def test_to_check_if_error_pops_up_when_input_is_string(self):
		self.assertRaises(ValueError,investment,"String")	
	
	def test_to_check_possible_edge_cases(self):
		self.assertEqual(investment.get_investment(0, 5, 10),0)
		self.assertEqual(investment.get_investment(1000, 0, 10),1000)
		self.assertEqual(investment.get_investment(1000, 5, 0),1000)
		
	def test_if_error_popsup_for_negative_values_input(self):
		self.assertRaises(ValueError, investment, (-1000, 5, 10))
		self.assertRaises(ValueError, investment, (1000, -5, 10))
		self.assertRaises(ValueError, investment, (1000, 5, -10))

		