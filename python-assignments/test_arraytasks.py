import unittest
import arraytasks


class testArraytask(unittest.TestCase):
	def test_that_the_prime_function_exist(self):
		arraytasks.ascending([5,4,3,2,1])

	def test_that_ascending_function_gives_a_descending_number(self):
		self.assertEqual(arraytasks.ascending([2,1,7,5,3]),[1,2,3,5,7])
		self.assertEqual(arraytasks.ascending([5,2,4,5,2]),[2,2,4,5,5])
