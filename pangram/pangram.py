import string

alphaSet = set(string.ascii_lowercase)

def is_pangram(inStr):
	curSet = set( inStr.lower() )
	return alphaSet <= curSet