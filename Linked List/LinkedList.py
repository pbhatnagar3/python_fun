import SingleLinkedNodes as sl
import DoublyLinkedNodes as dl
import unittest

class LinkedList(object):

	head = ""
	tail = ""
	curr_type = None 

	def __init__(self, linked_list_type, data):	

		if linked_list_type == "single":
			self.curr_type = sl
		else:
			self.curr_type = dl

		self.head = self.curr_type.LinkedNodes(data)
		self.tail = self.head
		# self.head.data = data

	def add(self, data):
		self.tail.next = self.curr_type.LinkedNodes(data)
		self.tail = self.tail.next

	def __repr__(self):
		result = []
		list_iter = self.head
		if list_iter == None:
			print "Nothing there"
			return ""
		while list_iter.next != None:
			result.append(list_iter.data)
		return "->".join(result)


my_list = LinkedList('single', 'Family')
my_list.add("Billy")
my_list.add("Joel")
print my_list
