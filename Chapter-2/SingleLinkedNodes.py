class LinkedNodes:
	next = None
	data = ''

	def __init__(self, data):
		self.data = data

	def set_next(self, set_to_next):
		self.next = set_to_next

	def get_data(self):
		return self.data

	def __repr__(self):
		if self.next != None:
			return " the present node %s and its next's data is %s" % \
			(str(self.data), str(self.next.data))
		else:
			return " the present node value is %s and there is no next" % (str(self.data))


if __name__ == '__main__':
	harry = SingleLinkedNodes('Harry')
	print harry
	# Lily = DoublyLinkedNodes('Lily', None, harry)
	# James = DoublyLinkedNodes('James', None, harry)
	# print Lily
	# print James
