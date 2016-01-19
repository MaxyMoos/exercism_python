OPEN = ( "(", "[", "{" )
CLOSE= ( ")", "]", "}" )


def splitString(inputStr):
	if len(inputStr) == 0:
		return ""
	
	openChar = inputStr[0]
	closeChar = CLOSE[OPEN.index(openChar)]
	if openChar not in OPEN or closeChar not in inputStr:
		raise ValueError
	else:
		count = 1
		for pos, char in enumerate(inputStr[1:]):
			if char == closeChar:
				count -= 1
				if count == 0:
					return [inputStr[1:pos+1], inputStr[pos+2:]]
			elif char == openChar:
				count += 1
	raise ValueError


def check_brackets(inputStr):
	for x in range(3):
		if inputStr.count(OPEN[x]) != inputStr.count(CLOSE[x]):
			return False
	try:
		split = splitString(inputStr)
		split = [res for elem in split for res in splitString(elem) if elem != '']
		while set(split) != set(""):
			split = [res for elem in split for res in splitString(elem) if elem != '']
	except ValueError:
		return False
	return set(split) == set("")