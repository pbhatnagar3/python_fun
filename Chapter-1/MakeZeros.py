# make all the elements zeros
import unittest

def make_zeros(array_2D):
	# iterate through the loop and mark all the positions with a zero. Both the row and cols
	places_with_zero = []
	for row_number, array_1D in enumerate(array_2D):
		for col_number, element in enumerate(array_1D):
			if element == 0:
				places_with_zero.append((row_number, col_number))

	for current_row_number, current_col_number in places_with_zero:
		array_2D[current_row_number] = [0] * len(array_2D[current_row_number])
		for array_1D in array_2D:
			array_1D[current_col_number] = 0

	return array_2D

def print_as_board(input_array):
	for array_1D in input_array:
		print " ".join(str(x) for x in array_1D)

	print "*"*20


input_array = [[1,2,3,4], [5,0,7,8], [9,10,11, 12]]
print_as_board(input_array)
make_zeros(input_array)
print_as_board(input_array)