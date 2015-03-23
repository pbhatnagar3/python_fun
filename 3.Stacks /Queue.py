from SimpleLinkedList import LinkedList
from SimpleLinkedList import Node

class My_Queue():
	
	def __init__(self):	
		self.backing_data_structure = LinkedList()

	def add_list(self, data):
		for i in data:
			if self.backing_data_structure.head == None:
				self.backing_data_structure.head = Node(i)
				self.backing_data_structure.tail = self.backing_data_structure.head

			else:
				self.backing_data_structure.tail.next = Node(i)
				self.backing_data_structure.tail = self.backing_data_structure.tail.next

	def add(self, i):
		if self.backing_data_structure.head == None:
			self.backing_data_structure.head = Node(i)
			self.backing_data_structure.tail = self.backing_data_structure.head

		else:
			self.backing_data_structure.tail.next = Node(i)
			self.backing_data_structure.tail = self.backing_data_structure.tail.next
	
	def remove(self):
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

	def __repr__(self):
		output = []
		temp = self.backing_data_structure.head
		while(temp != None):
			output.append(str(temp.data))
			temp = temp.next

		return "~/>".join(output)

my_queue = My_Queue()
my_queue.add_list([1,2,3,4,5])
print my_queue
my_queue.add(6)
print "updated queue is ", my_queue
for i in range(7):
	print 'removing element ', my_queue.remove()
