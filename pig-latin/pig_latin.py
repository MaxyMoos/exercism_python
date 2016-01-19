import string

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxz'

def translate(inputStr):
	result = ''

	for word in inputStr.split():
		if word[0] in vowels:
			result += word + 'ay'
		else:
			result += translate(word[1:] + word[0]) + ' '
	return result.strip()