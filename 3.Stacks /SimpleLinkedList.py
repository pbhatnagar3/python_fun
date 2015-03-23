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

	



import unittest
