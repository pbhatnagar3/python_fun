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

	def remove_duplicates(self):
		s = set()
		temp = self.head
		while(temp!= None):
			if temp.data in s:
				#issue a command to delete 
				self.delete(temp.data)
			else:
				s.add(temp.data)
			temp = temp.next


	def __repr__(self):
		output = []
		temp = self.head
		while(temp != None):
			output.append(str(temp.data))
			temp = temp.next
		return " --> ".join(output)

	
	def k_last_element(self, k):
		fast = self.head
		slow  = self.head
		
		while(fast.next != None):
			k -= 1		
			if k <= 0:
				slow = slow.next
			fast = fast.next
		
		return slow.data

	def removeMe(self, currentNode):
			print 'current node being removed is ', currentNode.data
			if currentNode.next == None:
				temp = self.head		
				while(temp.next.next!= None):
					temp = temp.next
				temp.next = None
				return

			else:
				currentNode.data = currentNode.next.data
				currentNode.next = currentNode.next.next
				return


	def partition(self, value):
		updated_list = LinkedList()
		temp = self.head
		while(temp != None):
			next_temp = temp.next
			if temp.data < value:
				if updated_list.head != None:
					bufferd = updated_list.head
					updated_list.head = temp
					updated_list.head.next = bufferd
				else:
					updated_list.head = temp
					updated_list.tail = temp
					temp.next = None		
			else:
				if updated_list.tail != None:
					updated_list.tail.next = temp
					updated_list.tail = temp
					updated_list.tail.next = None
				else:
					updated_list.tail = temp
					updated_list.head = temp
					temp.next = None
			print "contents of updated_list", updated_list
			temp = next_temp

		return updated_list

import unittest
class Test_removeMe(unittest.TestCase):
	test_list = LinkedList(['p0', 'p1', 'p2', 'p3', 'p4'])
	
	p0 = test_list.head
	p3 = test_list.head.next.next.next
	p4 = p3.next
	TEST_CASES = [p3, p0,p4]

	def test_removeMe(self):
		print self.test_list
		for i in self.TEST_CASES:
			print 'to remove is', i.data
			self.test_list.removeMe(i)
			print self.test_list

	def test_partitionMe(self):
		my_list = LinkedList([15, 19, 1, 2, 9, 6, 3])
		print 'mylist is', my_list
		print my_list.partition(5)

if __name__ == '__main__':
	unittest.main()

# my_list = LinkedList("Hard")
# my_list.append_to_end("work")
# my_list.append_to_end("and")
# my_list.append_to_end("Hope")
# my_list.append_to_end("are")
# my_list.append_to_end("important")
# my_list.append_to_end("and")

# print my_list

# my_list.delete("Hard")

# print my_list

# my_list.remove_duplicates()
# print my_list

# print my_list.k_last_element(4)