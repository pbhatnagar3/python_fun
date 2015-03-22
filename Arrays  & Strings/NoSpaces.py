# replacing all the spaces with %20
import unittest

def replace_spaces_C(input_string):
	# since strings are immutable, we will just convert them to list and assume that everything is well
	output = []
	for i in input_string[::-1]:
		if i == ' ':
			output.append("%20")
		else:
			output.append(i)

	return "".join(output[::-1])

def replace_spaces_python(input_string):
	return input_string.replace(" ", "%20")

class TestNoSpaces(unittest.TestCase):
	TEST_DATA = [("Pujun Bhatnagar", "Pujun%20Bhatnagar"), ("Mr. & Mrs. Smith", "Mr.%20&%20Mrs.%20Smith")]

	def test_blank_spaces(self):
		for input_string, expected_output in self.TEST_DATA:
			self.assertEqual(replace_spaces_python(input_string), expected_output)
			self.assertEqual(replace_spaces_C(input_string), expected_output)
if __name__ == '__main__':
	unittest.main()