def checkBoard(inputBoard):
	# Check all lines for equal length
	if len(inputBoard) > 0:
		refLength = len(inputBoard[0])
	for line in inputBoard[1:]:
		if len(line) != refLength:
			raise ValueError("All lines are not of the same length")
	
	if inputBoard[0][0] != "+" and inputBoard[0][-1] != "+" and inputBoard[1:-1] != "-" * (refLength - 2):
		raise ValueError("First line is ill-formatted")

	if inputBoard[0] != inputBoard[-1]:
		raise ValueError("First and last line are not the same")
	
	for line in inputBoard[1:-1]:
		if line[0] != "|" or line[-1] != "|":
			raise ValueError("Wrong border characters")
		wrongChar = [i for i in line[1:-1] if i not in [" ", "*"]]
		if len(wrongChar) > 0:
			raise ValueError("Wrong characters in the board: {}".format(wrongChar))
	return True

def board(inputBoard):
	checkBoard(inputBoard)
	result = []
	result.append(inputBoard[0])
	for elem in enumerate(inputBoard):
		curIndex = elem[0]
		if curIndex != 0 and curIndex != len(inputBoard) - 1:
			curLine = elem[1]
			newLine = []
			for lineChr in enumerate(curLine):
				chrIndex = lineChr[0]
				curChr = lineChr[1]
				if curChr == "|" or curChr == "*":
					newLine.append(curChr)
				if curChr == " " :
					neighbors = [inputBoard[curIndex][chrIndex-1]] + [inputBoard[curIndex][chrIndex+1]]
					if curIndex > 1:
						neighbors = list(inputBoard[curIndex-1][chrIndex-1:chrIndex+2]) + neighbors
					if curIndex < len(inputBoard)-2:
						neighbors = neighbors + list(inputBoard[curIndex+1][chrIndex-1:chrIndex+2])
					countStars = neighbors.count("*")
					if countStars > 0:
						newLine.append(str(countStars))
					else:
						newLine.append(curChr)
			newLine = "".join(newLine)	
			result.append(newLine)
	result.append(inputBoard[-1])
	return result