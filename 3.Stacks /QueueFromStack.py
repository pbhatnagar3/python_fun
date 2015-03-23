from Stack import My_Stack

class Queues_from_Stacks():

	def __init__(self):
		self.new_elements_stack = My_Stack()
		self.old_elements_stack = My_Stack()
		self.size = 0
	def add(self, data):
		for i in data:
			self.new_elements_stack.push(i)
		self.size = self.new_elements_stack.size + self.old_elements_stack.size
		return

	def remove(self):
		if self.old_elements_stack.size == 0:
			while(self.new_elements_stack.size != 0):
				self.old_elements_stack.push(self.new_elements_stack.pop())
			
		self.size = self.new_elements_stack.size + self.old_elements_stack.size - 1
		return self.old_elements_stack.pop()

	def __repr__(self):
		print self.old_elements_stack,'~/>', self.new_elements_stack
		return ''

if __name__ == '__main__':
	my_awesome_queue = Queues_from_Stacks()
	my_awesome_queue.add([1,2,3])
	print my_awesome_queue.remove() , 'removed from the queue'
	my_awesome_queue.add([10,20,30])
	print my_awesome_queue.remove(), 'removed from the queue'

	print my_awesome_queue

