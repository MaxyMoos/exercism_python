# First, naive implementation
# Refactoring left for v2

def verse(rank):
	if rank > 2:
		verseStr = str(rank) + " bottles of beer on the wall, " + str(rank) + " bottles of beer.\nTake one down and pass it around, " + str(rank - 1) + " bottles of beer on the wall.\n"
	elif rank == 2:
		verseStr = str(rank) + " bottles of beer on the wall, " + str(rank) + " bottles of beer.\nTake one down and pass it around, " + str(rank - 1) + " bottle of beer on the wall.\n"
	elif rank == 1:
		verseStr = str(rank) + " bottle of beer on the wall, " + str(rank) + " bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n"
	else:
		verseStr = "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
	return verseStr

def song(rank, lowerlimit=0):
	verseStr = ''
	while rank >= lowerlimit:
		verseStr += verse(rank) + "\n"
		rank -= 1
	return verseStr