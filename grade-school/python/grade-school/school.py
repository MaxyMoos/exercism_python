class School:
	db = {}
	
	def add(self, studentName, grade):
		if grade not in self.db.keys(): self.db[grade] = set()
		self.db[grade].add(studentName)

	def grade(self, grade):
		if grade in self.db.keys(): return self.db[grade]
		else:
			return set()
			
	def sort(self):
		result = []
		for grade in sorted( self.db.keys() ):
			result += [ (grade, tuple( sorted( self.db[grade] ) ) ) ]
		return result
		
	def __init__(self, schoolName):
		self.name = schoolName
		self.db = {}