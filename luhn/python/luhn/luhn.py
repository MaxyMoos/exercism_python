class Luhn:

	def __init__(self, number):
		self.inputNum = number
		self.inputNumStr = str(self.inputNum)
	
	def addends(self):
		addends = ''
		for i in range( 1, len(self.inputNumStr) + 1 ):
			if ( i % 2 == 0 ):
				# We need to double value and take off 9 if needed
				newNum = int( self.inputNumStr[-i] ) * 2
				if (newNum >= 10) : newNum -= 9
				addends = str(newNum) + addends #We append to the beginning of the string, not the end
			else:
				addends = self.inputNumStr[-i] + addends
		return [int(i) for i in addends]
	
	def checksum(self):
		return sum ( self.addends() ) % 10
	
	def is_valid(self):
		return self.checksum() == 0
	
	@staticmethod
	def create(number):
		# Clearly suboptimal as we try each possibility from 0 onwards
		# Still, a maximum of 10 iterations isn't THAT bad
		luhn = 0
		result = str(number) + str(luhn)
		while ( not Luhn(result).is_valid() ):
			luhn += 1
			result = str(number) + str(luhn)
		return int(result)