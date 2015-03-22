# check if the two strings are anagrams or not
import unittest
def check_anagrams(input_string1, input_string2):
	
	first_set = set(input_string1)
	second_set = set(input_string2)

	if (first_set.issubset(second_set) and second_set.issubset(first_set)):
		return True
	else:
		return False

class TestAnagrams(unittest.TestCase):
	TEST_CASES = [("Harry", "", False), ("Pujun",  "junPu", True), ("", "", True)]

	def test_anagrams(self):
		for input_string1, input_string2, output in self.TEST_CASES:
			self.assertEqual(check_anagrams(input_string2, input_string1), output)

if __name__ == "__main__":
	unittest.main()
