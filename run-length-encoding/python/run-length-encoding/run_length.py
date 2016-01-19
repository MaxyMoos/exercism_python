import string


def encode(inputStr):
	if len(inputStr) == 0:
		raise ValueError("Cannot encode empty string")

	lastChar = inputStr[0]
	counter = 1
	result = ''

	for char in inputStr[1:]:
		if lastChar != char:
			if counter > 1:
				result += str(counter)
			result += lastChar
			# Reset counter & lastChar
			counter = 1
			lastChar = char
		else:
			counter += 1
	# Final letter
	if counter > 1:
		result += str(counter)
	result += inputStr[-1]
	return result


def decode(inputStr):
	result = ''
	occurences = ''

	for char in inputStr:
		if char in string.digits:
			occurences += char
		else:
			if occurences == '':
				occurences = '1'
			result += int(occurences) * char
			occurences = ''
	return result