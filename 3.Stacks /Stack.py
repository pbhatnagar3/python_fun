from SimpleLinkedList import LinkedList
from SimpleLinkedList import Node

class My_Stack():
	
	def __init__(self):	
		self.backing_data_structure = LinkedList()
		self.size = 0

	def add(self, data):
		self.size += len(data)
		for i in data:
			if self.backing_data_structure.head == None:
				self.backing_data_structure.head = Node(i)
				self.backing_data_structure.tail = self.backing_data_structure.head

			else:
				temp = Node(i)
				temp.next = self.backing_data_structure.head
				self.backing_data_structure.head = temp

	def push(self, i):
		self.size += 1
		if self.backing_data_structure.head == None:
			self.backing_data_structure.head = Node(i)
			self.backing_data_structure.tail = self.backing_data_structure.head

		else:
			temp = Node(i)
			temp.next = self.backing_data_structure.head
			self.backing_data_structure.head = temp

	def pop(self):
		self.size -= 1
		if self.backing_data_structure.head == None:
			print "nothing to pop"
			return
		
		elif self.backing_data_structure.head == self.backing_data_structure.tail:
			temp = self.backing_data_structure.head
			self.backing_data_structure.head = None
			self.backing_data_structure.tail = None
			return temp.data

		else:
			temp = self.backing_data_structure.head
			self.backing_data_structure.head = self.backing_data_structure.head.next
			return temp.data


	def peek_top(self):
		if self.backing_data_structure.head == None:
			print "nothing in stack"
			return
		
		elif self.backing_data_structure.head == self.backing_data_structure.tail:
			temp = self.backing_data_structure.head
			return temp.data

		else:
			temp = self.backing_data_structure.head
			return temp.data

	def __repr__(self):
		output = []
		temp = self.backing_data_structure.head
		while(temp != None):
			output.append(str(temp.data))
			temp = temp.next

		return "~/>".join(output)

if __name__ == "__main__":
	my_stack = My_Stack()
	my_stack.add([1,2,3,4,5])
	print my_stack
	my_stack.push(6)
	for i in range(7):
		print my_stack.pop()
