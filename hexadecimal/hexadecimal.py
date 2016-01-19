refTable = 	{
			'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,
			'7':7, '8':8, '9':9,
			'a':10,	'b':11,	'c':12,	'd':13,	'e':14,	'f':15
		}

def hexa(inputStr):
	result = 0

	for pos, char in enumerate(reversed(inputStr.lower())):
		if char in refTable.keys(): result += refTable[char] * (16 ** pos)
		else: raise ValueError("Invalid hexadecimal character found")

	return result