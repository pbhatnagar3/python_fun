from Stack import My_Stack

class TowersOfHanoi():
	
	def __init__(self, pieces):
		self.towers = [My_Stack(), My_Stack(), My_Stack()]
		self.towers[0].add([i for i in range(1, pieces + 1)][::-1])

	def __repr__(self):
		for i, t in enumerate(self.towers):
			print i, "tower number", t
		return ""

	def solve(self, pieces, source_tower, destination_tower, buffer_tower):
		print 
		print '*' * 5
		print "source tower", source_tower
		print "destination tower", destination_tower
		print "buffer_tower", buffer_tower
		print 
		print '*' * 5

		if pieces < 1:
			return
		if pieces == 1:
			destination_tower.push(source_tower.pop())
			return
		else:
			self.solve(pieces - 1, source_tower, buffer_tower, destination_tower)
			self.solve(1, source_tower, destination_tower, buffer_tower)
			self.solve(pieces - 1, buffer_tower, destination_tower, source_tower)

if __name__ == '__main__':
	interesting_problem = TowersOfHanoi(3)
	print interesting_problem

	interesting_problem.solve(3, interesting_problem.towers[0], interesting_problem.towers[2], interesting_problem.towers[1])
	print interesting_problem
