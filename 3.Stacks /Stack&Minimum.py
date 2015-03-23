from SimpleLinkedList import LinkedList
from SimpleLinkedList import Node
from Stack import My_Stack

class My_Stack_with_Mimimum():
	
	def __init__(self):	
		self.backing_data_structure = LinkedList()
		self.minimum_data_structure = My_Stack()

	def add(self, data):
		for i in data:
			if self.backing_data_structure.head == None:
				self.backing_data_structure.head = Node(i)
				self.backing_data_structure.tail = self.backing_data_structure.head
				self.minimum_data_structure.push(i)

			else:
				temp = Node(i)
				temp.next = self.backing_data_structure.head
				self.backing_data_structure.head = temp
				if i <= self.minimum_data_structure.peek_top():
					print "top of min is", self.minimum_data_structure.peek_top(), " and value of i is ", i
					self.minimum_data_structure.push(i)

	def push(self, i):
		if self.backing_data_structure.head == None:
			self.backing_data_structure.head = Node(i)
			self.backing_data_structure.tail = self.backing_data_structure.head
			self.minimum_data_structure.push(i)
		
		else:
			temp = Node(i)
			temp.next = self.backing_data_structure.head
			self.backing_data_structure.head = temp
			if i < self.minimum_data_structure.peek_top:
				self.minimum_data_structure.push(i)

	def minimum(self):
		if self.backing_data_structure.head == None:
			print "Nothing in the stack. Check back later."
			return
		else:
			temp = self.minimum_data_structure.peek_top()
			print "the current minimum value is ", temp
			return temp

	def pop(self):
		if self.backing_data_structure.head == None:
			print "nothing to pop"
			return
		
		elif self.backing_data_structure.head == self.backing_data_structure.tail:
			temp = self.backing_data_structure.head
			self.backing_data_structure.head = None
			self.backing_data_structure.tail = None
			self.minimum_data_structure.head = None
			self.minimum_data_structure.tail = None
			return temp.data

		else:
			temp = self.backing_data_structure.head
			self.backing_data_structure.head = self.backing_data_structure.head.next
			if temp.data == self.minimum_data_structure.peek_top:
				self.minimum_data_structure.head = self.minimum_data_structure.head.next
			return temp.data

	def __repr__(self):
		output = []
		temp = self.backing_data_structure.head
		while(temp != None):
			output.append(str(temp.data))
			temp = temp.next

		return "~/>".join(output)


if __name__ == "__main__":
	my_stack = My_Stack_with_Mimimum()
	my_stack.add([1,2,3,4,5])
	print my_stack
	my_stack.minimum()
	my_stack.push(6)
	for i in range(7):
		print my_stack.pop()
	my_stack.add([-1])
	my_stack.minimum()
