refVal = {1:'wink', 2:'double blink', 4:'close your eyes', 8:'jump', 16:'reverse'}

def handshake(num):
	if str(num) == num:
		tmp = "0b" + num
		num = int(tmp, 2)

	if num not in range(0, 17):
		num = num % 16
	result = []

	for key,val in sorted(refVal.items()):
		if num & key == key:
			result += [val]
	if result[-1] == 'reverse':
		result = result[-2::-1]
	return result

def code(inArray):
	code = 0
	for key,val in refVal.items():
		if val in inArray:
			code += key
	return bin(code)[2:]
	
# code(['wink', 'double blink'])