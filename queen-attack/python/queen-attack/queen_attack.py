def board(whiteQueen, blackQueen):
	checkInput(whiteQueen, blackQueen)
	result = []
	emptyLine = "_" * 8
	for i in range(8):
		curLine = ""
		if whiteQueen[0] == i and blackQueen[0] == i:
			if whiteQueen[1] < blackQueen[1]:
				minQ = whiteQueen, "W"
				maxQ = blackQueen, "B"
			else:
				minQ = blackQueen, "B"
				maxQ = whiteQueen, "W"
			curLine = "_" * minQ[0][1] + minQ[1] + "_" * (maxQ[0][1] - minQ[0][1]) + maxQ[1] + "_" * (8-maxQ[0][1]-1)
		elif whiteQueen[0] == i:
			curLine = "_" * whiteQueen[1] + "W" + "_" * (8-(whiteQueen[1]+1))
		elif blackQueen[0] == i:
			curLine = "_" * blackQueen[1] + "B" + "_" * (8-(blackQueen[1]+1))
		else:
			curLine = emptyLine
		result.append(curLine)
	return result

def can_attack(whiteQueen, blackQueen):
	checkInput(whiteQueen, blackQueen)
	return (blackQueen[0] - whiteQueen[0]) == (blackQueen[1] - whiteQueen[1]) \
		or blackQueen[0] == whiteQueen[0] \
		or blackQueen[1] == whiteQueen[1] \
		or (whiteQueen[0] + whiteQueen[1] == 8 and blackQueen[0] + blackQueen[1] == 8)

def checkInput(whiteQueen, blackQueen):
	if len(whiteQueen) != 2 or len(blackQueen) != 2:
		raise ValueError("Wrong length for parameters")
	if whiteQueen[0] == blackQueen[0] and whiteQueen[1] == blackQueen[1]:
		raise ValueError("The two queens cannot be in the same position")
	if whiteQueen[0] not in range(8) or whiteQueen[1] not in range(8) or blackQueen[0] not in range(8) or blackQueen[1] not in range(8):
		raise ValueError("Wrong position entered")