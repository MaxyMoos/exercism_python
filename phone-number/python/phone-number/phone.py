class Phone():
	def checkPhoneNumber(self, number):
		digits = [i for i in number if i.isdigit()]
		if len(digits) == 10:
			return "".join(digits)
		elif len(digits) == 11 and digits[0] == "1":
			return "".join(digits[1:])
		else:
			return "0" * 10
	
	def __init__(self, number):
		self.number = self.checkPhoneNumber(number)

	def area_code(self):
		return self.number[0:3]

	def pretty(self):
		return "(" + self.area_code() + ") " + self.number[3:6] + "-" + self.number[6:]