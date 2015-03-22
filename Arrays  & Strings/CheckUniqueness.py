def check_uniqueness(input_string):
    #for i in input_string:
    s = set(input_string)
    if len(s) == len(input_string):
        return True
    else:
        return False

import unittest

class Test_check_uniqueness(unittest.TestCase):
	TEST_CASES = [("", True), ("Puj", True), ("Pujun", False)]

	def test_check_uniqueness(self):
		for i, j in self.TEST_CASES:
			# print self.TEST_CASES
			self.assertEqual(check_uniqueness(i), j)


if __name__ == "__main__":
	unittest.main()
