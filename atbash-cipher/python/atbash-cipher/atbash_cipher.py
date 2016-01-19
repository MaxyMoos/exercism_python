import string

def insert_spaces(inputStr):
	return " ".join( inputStr[i:i+5] for i in range(0, len(inputStr), 5) )	

def remove_spaces(inputStr):
	return inputStr.replace(' ', '')

def encode(clearStr):
	cipherStr = ''
	for char in clearStr.lower():
		if char in string.lowercase:
			cipherStr = cipherStr + string.lowercase[- string.lowercase.index(char) - 1]
		elif char in string.digits:
			cipherStr = cipherStr + char
	return insert_spaces(cipherStr)

def decode(cipherStr):
	clearStr = ''
	for char in cipherStr.lower():
		if char in string.lowercase:
			clearStr = clearStr + string.lowercase[- string.lowercase.index(char) - 1]
		elif char in string.digits:
			clearStr = clearStr + char
	return remove_spaces(clearStr)