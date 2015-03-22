# make all the characters of the variables unique by removing all the duplicate ones
import unittest

def make_unique_wo_additional_memory(input_string):
	make_unique_list = list(input_string[::-1])
	i = 0
	while i < len(make_unique_list):
		if make_unique_list[i] in make_unique_list[i + 1 :]:
			make_unique_list.pop(i)
			i = i - 1
		i += 1
	return "".join(make_unique_list[::-1])

def make_unique_w_additional_memory(input_string):
	# we cannot use a set here since set does not preserve the order of the elements
	record_keeper = set()
	to_output = []
	for i in input_string:
		if i in record_keeper:
			continue
		else:
			to_output.append(i)
			record_keeper.add(i)
	return "".join(to_output)

class TestMakeUnique(unittest.TestCase):
	TEST_DATA = [('', ''), ('i', 'i'), ('Pujun', 'Pujn'), ('aaaaaaa', 'a')]

	def test_test_make_unique(self):
		for to_check, output in self.TEST_DATA:
			self.assertEqual(make_unique_w_additional_memory(to_check), output)

	def test_test_make_unique_wo_additional_structure(self):
		for to_check, output in self.TEST_DATA:
			self.assertEqual(make_unique_wo_additional_memory(to_check), output)

if __name__ == "__main__":
	pass
	unittest.main()
