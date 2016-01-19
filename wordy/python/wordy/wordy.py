def calculate(inputStr):
	splitted = inputStr.split()
	splitted = splitted[0:-1] + list(splitted[-1].split("?")[0:])

	checkInput(splitted)
	onlyOrders = splitted[2:-1]
	count = 1
	while len(onlyOrders) > 1:
		result = 0

		firstNumber = int(onlyOrders[0])
		operation = onlyOrders[1]
		lastIndex = 2

		if operation == "plus":
			if onlyOrders[2] == '-':
				secondNumber = - int(onlyOrders[3])
				lastIndex = 3
			else:
				secondNumber = int(onlyOrders[2])
				lastIndex = 2
			result = firstNumber + secondNumber
		elif operation == "minus":
			if onlyOrders[2] == '-':
				secondNumber = - int(onlyOrders[3])
				lastIndex = 3
			else:
				secondNumber = int(onlyOrders[2])
				lastIndex = 2
			result = firstNumber - secondNumber
		elif operation == "multiplied":
			if onlyOrders[3] == '-':
				secondNumber = - int(onlyOrders[4])
				lastIndex = 4
			else:
				secondNumber = int(onlyOrders[3])
				lastIndex = 3
			result = firstNumber * secondNumber
		elif operation == "divided":
			if onlyOrders[3] == '-':
				secondNumber = - int(onlyOrders[4])
				lastIndex = 4
			else:
				secondNumber = int(onlyOrders[3])
				lastIndex = 3
			result = firstNumber / secondNumber
		else:
			raise ValueError("Operation not recognized")
		onlyOrders = [result] + onlyOrders[lastIndex+1:]
	return int(onlyOrders[0])


def checkInput(splitted):
	if splitted[0:2] != ["What", "is"]:
		raise ValueError("Expecting \"What is\" at the beginning of input")