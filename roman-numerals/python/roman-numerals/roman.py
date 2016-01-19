def numeral(arabic):
	romanStr = ""
	strArabic = str(arabic)
	for i in range(1, len(strArabic) + 1):
		if strArabic[-i] == '0': continue
		if i == 1:
			romanStr = units(strArabic[-i]) + romanStr
		elif i == 2:
			romanStr = decimals(strArabic[-i]) + romanStr
		elif i == 3:
			romanStr = centuries(strArabic[-i]) + romanStr
		elif i == 4:
			romanStr = milleniums(strArabic[-i]) + romanStr
	return romanStr

def units(number):
	refDict = 	{
					'1':'I',
					'2':'II',
					'3':'III',
					'4':'IV',
					'5':'V',
					'6':'VI',
					'7':'VII',
					'8':'VIII',
					'9':'IX'
				}
	return refDict[number]
	
def decimals(number):
	refDict =	{
					'1':'X',
					'2':'XX',
					'3':'XXX',
					'4':'XL',
					'5':'L',
					'6':'LX',
					'7':'LXX',
					'8':'LXXX',
					'9':'XC'
				}
	return refDict[number]

def centuries(number):
	refDict =	{
					'1':'C',
					'2':'CC',
					'3':'CCC',
					'4':'CD',
					'5':'D',
					'6':'DC',
					'7':'DCC',
					'8':'DCCC',
					'9':'CM'
				}
	return refDict[number]

def milleniums(number):
	refDict =	{
					'1':'M',
					'2':'MM',
					'3':'MMM'
				}
	return refDict[number]