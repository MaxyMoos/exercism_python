import string, random

class Cipher:

	def __init__(self, key=''):
		if ( key == '' ):
			self.key = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(100))
		else:
			self.key = key
	
	def encode(self, clearText):
		cipherText = ''
		
		stretchedKey = self.stretch_key( len(clearText) )
		
		for i in range( 0, len(clearText) ):
			curChar = clearText[i].lower()
			if curChar in string.ascii_lowercase:
				tmpIndex = string.ascii_lowercase.index( curChar ) + string.ascii_lowercase.index( stretchedKey[i] )
				if tmpIndex > 25: tmpIndex -=26
				cipherText += string.ascii_lowercase[tmpIndex]
		return cipherText
	
	def decode(self, cipherText):
		clearText = ''
		
		stretchedKey = self.stretch_key( len(cipherText) )
		
		for i in range( 0, len(cipherText) ):
			curChar = cipherText[i]
			tmpIndex = string.ascii_lowercase.index( curChar ) - string.ascii_lowercase.index( stretchedKey[i] )
			if tmpIndex < 0: tmpIndex += 26
			clearText += string.ascii_lowercase[ tmpIndex ]
		return clearText

	def stretch_key(self, length):
		tmpKey = self.key
		while len( tmpKey ) < length:
			tmpKey += 'a'
		return tmpKey
	
class Caesar(Cipher):

	def __init__(self, shiftRank=3):
		self.shiftRank = shiftRank

	def encode(self, clearText):
		cipherText = ''
		for letter in clearText:
			if letter.lower() in string.ascii_lowercase:
				cipherText += string.ascii_lowercase[ (string.ascii_lowercase.index( letter.lower() ) + self.shiftRank ) % len(string.ascii_lowercase) ]
		return cipherText
	
	def decode(self, cipherText):
		self.shiftRank = - self.shiftRank
		result = self.encode(cipherText)
		self.shiftRank = - self.shiftRank
		return result