import itertools

class Matrix():
	def __init__(self, inStr):
		self.rows = []
		for line in inStr.split('\n'):
			line = [int(i) for i in line.split(" ") if i.isalnum()]
			self.rows += [line]
		self.columns = [ list(i) for i in itertools.zip_longest(*self.rows, fillvalue=' ') ]