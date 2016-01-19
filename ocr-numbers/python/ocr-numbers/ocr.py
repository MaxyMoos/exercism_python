ZERO_OCR = 	[" _ ",
		 	 "| |",
		 	 "|_|",
		 	 "   "]

ONE_OCR	=	["   ",
		 	 "  |",
		 	 "  |",
		 	 "   "]

TWO_OCR =	[" _ ",
		 	 " _|",
		 	 "|_ ",
		 	 "   "]

THREE_OCR =	[" _ ",
		 	 " _|",
		 	 " _|",
		 	 "   "]

FOUR_OCR =	["   ",
		 	 "|_|",
		 	 "  |",
		 	 "   "]

FIVE_OCR = 	[" _ ",
		 	 "|_ ",
		 	 " _|",
		 	 "   "]

SIX_OCR =	[" _ ",
		 	 "|_ ",
		 	 "|_|",
		 	 "   "]

SEVEN_OCR =	[" _ ",
		 	 "  |",
		 	 "  |",
		 	 "   "]

EIGHT_OCR = 	[" _ ",
				 "|_|",
				 "|_|",
		 		 "   "]

NINE_OCR =	[" _ ",
			 "|_|",
		 	 " _|",
		 	 "   "]

NUMBERS = [ZERO_OCR, ONE_OCR, TWO_OCR, THREE_OCR, FOUR_OCR, FIVE_OCR, SIX_OCR, SEVEN_OCR, EIGHT_OCR, NINE_OCR]
GARBLE = [	" _ ",
			"  |",
			" _|",
			"   "]

def checkInput(candidate):
	for item in candidate:
		if len(item) % 3 != 0:
			raise ValueError("Length of input is not a multiple of three")
	if len(candidate) == 4:
		refLen = len(candidate[0])
		for item in candidate[1:]:
			if len(item) != refLen:
				return False
	else:
		raise ValueError("4 rows expected")


def grid(digits):
	result = ["", "", "", ""]
	for char in digits:
		newresult = []
		if int(char) in range(10):
			result = [a + b for a,b in zip(result, NUMBERS[int(char)])]
		else:
			result = [a + b for a,b in zip(result, GARBLE)]
	return result


def number(candidate):
	if checkInput(candidate) == False:
		return '?'

	digits = [ [item[i:i+3] for item in candidate] for i in range(0, len(candidate[0]), 3) ]

	result = ""
	for item in digits:
		match = [index for index, value in enumerate(NUMBERS) if item == value]
		if len(match) != 0:
			result += str(match[0])
		else:
			result += '?'
	return result