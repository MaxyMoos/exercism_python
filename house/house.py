COUPLES = {	0: ("lay in", "house that Jack built."),
			1: ("ate", "malt"),
			2: ("killed", "rat"),
			3: ("worried", "cat"),
			4: ("tossed", "dog"),
			5: ("milked", "cow with the crumpled horn"),
			6: ("kissed", "maiden all forlorn"),
			7: ("married", "man all tattered and torn"),
			8: ("woke", "priest all shaven and shorn"),
			9: ("kept", "rooster that crowed in the morn"),
			10:("belonged to", "farmer sowing his corn"),
			11:("", "horse and the hound and the horn")
		}

def verse(rank):
	firstLine = "This is the " + COUPLES[rank][1]
	body = "".join(["that " + COUPLES[i][0] + " the " + COUPLES[i][1] + "\n" for i in range(rank)[::-1]])
	body = body.strip()  # Remove the trailing newline at the end
	if rank == 0:
		return firstLine
	else:
		return "\n".join([firstLine, body])

def rhyme():
	return "\n\n".join([verse(i) for i in range(12)])