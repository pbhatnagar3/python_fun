class Node:
	data = None
	next = None

	def __init__(self, data, next):
		self.data = data
		self.next = next

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	head = None
	tail = None	
	size = 0

	def __init__(self, data=None):
		if data == None:
			self.head = None
			self.tail = None
			self.size = 0
			return

		for i in data:
			self.append_to_end(i)

	def append_to_end(self, data):
		self.size += 1
		if self.head == None:
			self.head = Node(data)
			self.size = 1
			self.tail = self.head
			return
		temp = self.head
		while(temp.next != None):
			temp = temp.next
		temp.next = Node(data)
		self.tail = temp.next

	def delete(self, data):
		print "here is the data ", data
		temp = self.head
		if temp.data == data:
			self.head = self.head.next
			return
		while(temp!= None and temp.data != data):
			parent = temp
			temp = temp.next
		if temp!= None:
			parent.next = temp.next
			return
		else:
			print 'not found in list'


	def __repr__(self):
		output = []
		temp = self.head
		while(temp != None):
			output.append(str(temp.data))
			temp = temp.next
		return " --> ".join(output)

	
	def add_linked_list(self, other_list):
		output_list = LinkedList()
		ripple = 0
		temp1 = self.head
		temp2 = other_list.head
		while(temp1 != None or temp2 != None or ripple != 0):
			if temp1.data != None and temp2.data != None:
				cumulative_sum = (temp1.data + temp2.data + ripple)
			elif temp1.data == None and temp2.data != None:
				cumulative_sum = temp2.data + ripple

			elif temp1.data != None and temp2.data == None:
				cumulative_sum = temp1.data + ripple

			else:
			 	cumulative_sum = ripple
			output_list.append_to_end( cumulative_sum % 10)
			ripple = ( cumulative_sum/ 10)			
			temp1 = temp1.next
			temp2 = temp2.next

		return output_list

import unittest


class test_add_linked_lists(unittest.TestCase):
	l1 = LinkedList([3,2,1])
	l2 = LinkedList([0,0,1])
	intended_suml1l2  = LinkedList([3,2,2])
	TEST_CASES = [(l1, l2, intended_suml1l2)]


	def test_add_linked_lists(self):
		for l1, l2, intended_output in self.TEST_CASES:
			print l1.add_linked_list(l2)


if __name__ == "__main__":
	unittest.main()