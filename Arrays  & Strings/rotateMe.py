# we have to rotate the image by 90 degrees
import unittest

def rotate(array, layer, start_index, stop_index):
	temp_list = grab_top_layer(array, layer, start_index, stop_index)
	if start_index == stop_index:
		return
	put_top_layer(array, layer, start_index, stop_index, grab_right_layer(array, layer, start_index, stop_index))
	put_right_layer(array, layer, start_index, stop_index, grab_bottom_layer(array, layer, start_index, stop_index)[::-1])
	put_bottom_layer(array, layer, start_index, stop_index, grab_left_layer(array, layer, start_index, stop_index))
	put_left_layer(array, layer, start_index, stop_index, temp_list[::-1])
	rotate(array, layer + 1, start_index + 1, stop_index - 1)
	

def grab_top_layer(array, layer, start_index, stop_index):
	to_return_list = []
	for i in range(start_index, stop_index):
		to_return_list.append(array[layer][i])

	return to_return_list


def grab_left_layer(array, layer, start_index, stop_index):
	to_return_list = []
	layer_number = 0
	for i in range(len(array)):
		if layer_number in range(start_index, stop_index): 
			to_return_list.append(array[layer_number][layer])
		layer_number += 1

	return to_return_list

def grab_right_layer(array, layer, start_index, stop_index):
	to_return_list = []
	layer_number = 0
	for i in range(len(array)):
		if layer_number in range(start_index, stop_index): 
			to_return_list.append(array[layer_number][len(array) - 1 - layer])
		layer_number += 1

	return to_return_list

def grab_bottom_layer(array, layer, start_index, stop_index):
	to_return_list = []
	for i in range(start_index, stop_index):
		to_return_list.append(array[len(array) - 1 - layer][i])

	return to_return_list


def put_top_layer(array, layer, start_index, stop_index, to_put_list):
	index = 0
	for i in range(start_index, stop_index):
		array[layer][i] = to_put_list[index]
		index += 1


def put_left_layer(array, layer, start_index, stop_index, to_put_list):
	index = 0
	layer_number = 0
	for i in range(len(array)):
		if layer_number in range(start_index, stop_index): 
			array[layer_number][layer] = to_put_list[index]
			index += 1
		layer_number += 1
		

def put_right_layer(array, layer, start_index, stop_index, to_put_list):
	index = 0
	layer_number = 0
	for i in range(len(array)):
		if layer_number in range(start_index, stop_index): 
			array[layer_number][len(array) - 1 - layer] = to_put_list[index]
			index += 1
		layer_number += 1

def put_bottom_layer(array, layer, start_index, stop_index, to_put_list):
	index = 0
	for i in range(start_index, stop_index):
		array[len(array) - 1 - layer][i] = to_put_list[index]
		index += 1


def print_as_array(input_array):
	for i in input_array:
		# print i
		print " ".join(i)
	print "*" * 12

array = [['01','02','03','04'], ['05','06','07','08'], ['09','10','11','12'], ['13', '14', '15','16']]
print_as_array(array)
rotate(array, 0, 0, 4)
print_as_array(array)

class TestRotateMe(unittest.TestCase):
	array = [['01','02','03','04'], ['05','06','07','08'], ['09','10','11','12'], ['13', '14', '15','16']]
	
	def test_grab_top_layer(self):
		test_data = [(0, 0, 4, ['01', '02', '03', '04']), (1, 0, 4, ['05', '06', '07', '08']), (1, 1, 3, [ '06', '07'])]
		for layer_number, start_index, end_index, intended_output in test_data:
			self.assertEqual(grab_top_layer(self.array, layer_number, start_index, end_index), intended_output)

	def test_grab_left_layer(self):
		test_data = [(0, 0, 4, ['01', '05', '09', '13']), (1, 0, 4, ['02', '06', '10', '14']), (1, 1, 3, [ '06', '10'])]
		for layer_number, start_index, end_index, intended_output in test_data:
			self.assertEqual(grab_left_layer(self.array, layer_number, start_index, end_index), intended_output)

	def test_grab_right_layer(self):
		test_data = [(0, 0, 4, ['04', '08', '12', '16']), (1, 0, 4, ['03', '07', '11', '15']), (1, 1, 3, [ '07', '11'])]
		for layer_number, start_index, end_index, intended_output in test_data:
			self.assertEqual(grab_right_layer(self.array, layer_number, start_index, end_index), intended_output)

	def test_grab_bottom_layer(self):
		test_data = [(0, 0, 4, ['13', '14', '15', '16']), (1, 0, 4, ['09', '10', '11', '12']), (1, 1, 3, [ '10', '11'])]
		for layer_number, start_index, end_index, intended_output in test_data:
			self.assertEqual(grab_bottom_layer(self.array, layer_number, start_index, end_index), intended_output)

if __name__ == "__main__":
	unittest.main()