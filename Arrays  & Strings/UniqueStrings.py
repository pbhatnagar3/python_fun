import unittest

def unique_string_tester(to_check):
	return len(set(to_check)) == len(to_check)

class ProgramTester(unittest.TestCase):
	TEST_DATA = [('', True), (' ', True), ('P  ', False), ('P', True)];

	def test_unique_string(self):
		for to_check, answer in self.TEST_DATA:
			self.assertEqual(unique_string_tester(to_check), answer)

if __name__ == '__main__':
	unittest.main()