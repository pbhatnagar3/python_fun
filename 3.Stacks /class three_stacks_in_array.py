import copy

class Array_Stack():
	
	def __repr__(self):
		return "->".join([str(i) for i in self.backing_array])

	def __init__(self, size):
		if size < 10:
			print "the array might not be large enough. Try again"
			return
		self.backing_array = [None] * size
		self.boundaries = [size/3 * i for i in range(1,4)]
		self.boundaries[2] += 1
		self.starting_positions = [size/3 * i for i in range(3)]
		self.current_positions = copy.deepcopy(self.starting_positions)
		print "boundaries", self.boundaries
		print self.starting_positions

	def push(self, data, index):
		index -= 1
		current_position = self.current_positions[index] 
		if current_position == self.boundaries[index]:
			print "stack full. Remove some elements and try again"
			return
		else:
			self.backing_array[current_position] = data
			self.current_positions[index] += 1
			return



	def pop(self, index):
		index -= 1
		current_position = self.current_positions[index] 
		if current_position == self.starting_positions[index]:
			print "stack empty"
			return
		else:
			temp = self.backing_array[current_position - 1]
			self.backing_array[current_position - 1] = None
			self.current_positions[index] -= 1
			return temp

three_stacks_in_array = Array_Stack(10)
print three_stacks_in_array

three_stacks_in_array.push(3, 3)
print three_stacks_in_array

three_stacks_in_array.push(4, 3)
print three_stacks_in_array

three_stacks_in_array.push(5, 3)
print three_stacks_in_array

three_stacks_in_array.push(6, 3)
print three_stacks_in_array

three_stacks_in_array.push(7, 3)
print three_stacks_in_array

print 'being poped', three_stacks_in_array.pop(3)
print three_stacks_in_array

print 'being poped', three_stacks_in_array.pop(3)
print three_stacks_in_array

print 'being poped', three_stacks_in_array.pop(3)
print three_stacks_in_array

print 'being poped', three_stacks_in_array.pop(3)
print three_stacks_in_array


print 'being poped', three_stacks_in_array.pop(3)
print three_stacks_in_array
