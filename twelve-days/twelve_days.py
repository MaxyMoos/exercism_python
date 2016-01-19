nth = { 1:['first','a Partridge in a Pear Tree.'], 2:['second', 'two Turtle Doves'] , 3:['third', 'three French Hens'], 
	4:['fourth', 'four Calling Birds'], 5:['fifth', 'five Gold Rings'], 6:['sixth', 'six Geese-a-Laying'],
	7:['seventh', 'seven Swans-a-Swimming'], 8:['eighth', 'eight Maids-a-Milking'], 9:['ninth', 'nine Ladies Dancing'], 
	10:['tenth', 'ten Lords-a-Leaping'], 11:['eleventh', 'eleven Pipers Piping'], 12:['twelfth', 'twelve Drummers Drumming'] }

def verse(index):
	separator = ", "

	result = "On the " + nth[index][0] + " day of Christmas my true love gave to me"

	if index == 1:
		result += ", " +  nth[1][1]
	else:
		for i in reversed(range(1, index + 1)):
			if i == 1: separator = ", and "
			result += separator + nth[i][1]
	return result + "\n"

def sing():
	result = ""
	for i in range(1, 13):
		result += verse(i) + "\n"
	return result

def verses(minInd, maxInd):
	result = ""
	for i in range(minInd , maxInd + 1):
		result += verse(i) + "\n"
	return result