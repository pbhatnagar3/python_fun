# reverse a string
import unittest

def reverse_string_python(to_reverse):
	return to_reverse[::-1]

def reverse_string_C(to_reverse):
	to_reverse_list = list(to_reverse)
	for i in xrange(len(to_reverse) /2):
		temp = to_reverse_list[i]
		to_reverse_list[i] = to_reverse_list[len(to_reverse) -i - 1]
		to_reverse_list[len(to_reverse) - i - 1] = temp

	return ''.join(to_reverse_list)


class TestReverseString(unittest.TestCase):

	TEST_CASES = [('', ''), ('i', 'i'), ('hi', 'ih'), ('Pujun', 'nujuP')]
	def test_reverse_string_python(self):
		for to_reverse, reversed_string in self.TEST_CASES:
			self.assertEqual(reverse_string_python(to_reverse), reversed_string)

	def test_reverse_string_C(self):
		for to_reverse, reversed_string in self.TEST_CASES:
			self.assertEqual(reverse_string_C(to_reverse), reversed_string)

if __name__ == "__main__":
	unittest.main()
