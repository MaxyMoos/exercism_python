class Triangle():
	def __init__(self, first, second, third):
		if first <= 0 or second <= 0 or third <= 0:
			raise TriangleError("Incorrect initialization values")
		if first + second <= third or first + third <= second or second + third <= first:
			raise TriangleError("Violating triangle inequality")
		self.sides = first, second, third

	def kind(self):
		kinds = ["", "equilateral", "isosceles", "scalene"]
		return kinds[ len(set(self.sides)) ]

class TriangleError(Exception):
	pass