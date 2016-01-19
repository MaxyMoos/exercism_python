NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot():
	def __init__(self, direction=NORTH, xCoord=0, yCoord=0):
		self.bearing = direction
		self.coordinates = xCoord, yCoord

	def turn_right(self):
		self.bearing = (self.bearing + 1) % 4

	def turn_left(self):
		self.bearing = (self.bearing - 1) % 4

	def advance(self):
		advanceVectors = [(0,1), (1,0), (0,-1), (-1,0)]
		self.coordinates = self.coordinates[0] + advanceVectors[self.bearing][0], self.coordinates[1] + advanceVectors[self.bearing][1]

	def simulate(self, inputString):
		for char in inputString:
			if char == "R":
				self.turn_right()
			if char == "L":
				self.turn_left()
			if char == "A":
				self.advance()