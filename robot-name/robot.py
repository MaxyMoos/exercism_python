import random
import string

givenNames = []

class Robot():
	
	def build_random_name(self):
		rand = random.randint(0,25)
		tmp = string.ascii_uppercase[rand]
		rand = random.randint(0,25)
		tmp += string.ascii_uppercase[rand]
		rand = random.randint(100,999)
		tmp += str(rand)
		return tmp

	def generateAndAssignName(self):
		global givenNames
		tmp = self.build_random_name()
		while tmp in givenNames:
			tmp = self.build_random_name()
		self.name = tmp
		givenNames += [self.name]

	def __init__(self):
		self.generateAndAssignName()

	def name(self):
		return self.name

	def reset(self):
		self.generateAndAssignName()