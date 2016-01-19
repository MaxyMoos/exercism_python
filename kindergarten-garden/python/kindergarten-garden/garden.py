class Garden:
	firstRow = ''
	secondRow = ''
	results = {}
	
	plantsArray = {
				'G':'Grass',
				'C':'Clover',
				'R':'Radishes',
				'V':'Violets'
			}
	
	def analyze(self):
		i = 0
		while ( i < len(self.firstRow) / 2 ):
			tmp = [ self.plantsArray[self.firstRow[i*2]], self.plantsArray[self.firstRow[i*2+1]], self.plantsArray[self.secondRow[i*2]], self.plantsArray[self.secondRow[i*2+1]] ]
			self.results[ self.students[i] ] = tmp
			i += 1
	
	def __init__( self, rows, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'] ):
		lines = str.split(rows)
		self.firstRow = lines[0]
		self.secondRow = lines[1]
		self.students = sorted(students)
		self.analyze()
	
	def plants(self, student):
		return self.results[student]