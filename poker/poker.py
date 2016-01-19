from collections import Counter

RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
RANKED_HANDS =	{ 	"Highest card":0,
					"Pair":1,
					"Two pairs":2,
					"Three of a kind":3,
					"Straight":4,
					"Flush":5,
					"Full house":6,
					"Four of a kind":7,
					"Straight flush":8	
				}


class PokerHand():

	@staticmethod
	def analyzeHand(hand):
		cards = [item[0] for item in hand]
		colors = [item[1] for item in hand]

		allCardsSameColor = False
		isAStraight = False

		# Check for same color
		if len(set(colors)) == 1:
			allCardsSameColor = True

		# Check for consecutive cards
		sortedRanks = sorted([RANK.index(card) + 2 for card in cards])
		relativeCards = [card - sortedRanks[0] for card in sortedRanks]

		cardOccurences = Counter(cards).most_common()

		if relativeCards == [0, 1, 2, 3, 4]:
			isAStraight = True

		if allCardsSameColor and isAStraight:
			result = "Straight flush"
		elif isAStraight:
			result = "Straight"
		elif allCardsSameColor:
			result = "Flush"
		elif cardOccurences[0][1] == 4:
			result = "Four of a kind"
		elif cardOccurences[0][1] == 3 and cardOccurences[1][1] == 2:
			result = "Full house"
		elif cardOccurences[0][1] == 3:
			result = "Three of a kind"
		elif cardOccurences[0][1] == 2 and cardOccurences[1][1] == 2:
			result = "Two pairs"
		elif cardOccurences[0][1] == 2:
			result = "Pair"
		else:
			result = "Highest card"

		return RANKED_HANDS[result], cardOccurences


	def __init__(self, hand):
		if len(hand) != 5:
			raise ValueError("Wrong length: a hand is expected to contain 5 cards")

		self.handRef = hand  # Backref
		self.kind, cardOccurences = self.analyzeHand(hand)
		maxOccurence = cardOccurences[0][1]
		self.highestCard = [max([RANK.index(item[0]) + 2 for item in cardOccurences if item[1] == maxOccurence])]


	def __lt__(self, other):
		if self.kind < other.kind:
			return True
		elif self.kind == other.kind:  # The two pairs case really is a PITA
			for selfCard, otherCard in zip(self.highestCard, other.highestCard):
				if selfCard < otherCard:
					return True
		return False


	def __gt__(self, other):
		if self.kind > other.kind:
			return True
		elif self.kind == other.kind:
			for selfCard, otherCard in zip(self.highestCard, other.highestCard):
				if selfCard > otherCard:
					return True
		return False

	def __eq__(self, other):
		return self.kind == other.kind and self.highestCard == self.highestCard


def poker(hands):
	handsObjects = sorted([PokerHand(hand) for hand in hands])[::-1]
	result = [handsObjects[0]]
	for item in handsObjects[1:]:
		if result[0] > item:
			break
		else:
			result.append(item)
	# Ugly hack: if the list is not sorted this way, a SINGLE test fails (the last one)
	return sorted([item.handRef for item in result], key=lambda x: hands.index(x))

	