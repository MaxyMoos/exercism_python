def parse_binary(binStr):
	if len([i for i in binStr if i != '0' and i != '1']) > 0:
		raise ValueError("Invalid characters found in string")
	
	# Input sanitizing is done
	result = 0
	for i in range(0, len(binStr)):
		result += int(binStr[i]) * (2 ** (len(binStr) - i - 1))
	return result