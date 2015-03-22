class LinkedNodes:
	data = ""
	parent = None
	next = None

	def __init(self, data):
		self.data = data

	def __init__(self, data, parent, next):
		self.data = data
		self.parent = parent
		self.next = next

	def get_data(self):
		return self.data

	def __repr__(self):
		if self.parent == None:
			if self.next == None:
				return "the present node has %s as its data and it has no parent or nextren." % str(self.data)

			else:
				return "the present node contains %s and has no parent. However, its next contains %s" %(str(self.data), str(self.next.data))
		
		if self.next == None:
			return "the present node data is %s and it has no nextren. It's parent has the following data %s" % \
			(str(self.data), str(self.parent.data))
		else: 
			return "the present node data is %s and its nextren data is %s. Finally, its parent contains %s" \
			(str(self.data), str(self.next.data), str(self.parent.data))
