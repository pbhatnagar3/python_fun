def reverse_string(input_string):
    input_string_list = list(input_string)
    for i in xrange(len(input_string)/2):
        temp = input_string[i]
        input_string_list[i] = input_string[len(input_string) -i - 1]
        input_string_list[len(input_string) -i -1 ] = temp

    return "".join(input_string_list)

import unittest

class Test_reverse_string(unittest.TestCase):

	TEST_CASES = [('Pujun', 'nujuP'), ('', '')]

	def test_reverse_string(self):
		for input_string, expected_output in self.TEST_CASES:
			# print self.TEST_CASES
			self.assertEqual(reverse_string(input_string), expected_output)

if __name__ == '__main__':
	unittest.main()