NUMBERS = ["", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

TENS    = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

HUNDRED = "hundred "

THOUSAND = "thousand "

MILLION = "million "

BILLION = "billion "

ORDERED_SUFFIXES    =   ["", THOUSAND, MILLION, BILLION]

def buildSpecialOnes(tens, units):
    totalNum = tens * 10 + units
    if totalNum < 20:
        return NUMBERS[totalNum]
    else:
        if units != 0:
            return "-".join([TENS[tens], NUMBERS[units]])
        else:
            return TENS[tens]

def say(number):
    from itertools import zip_longest

    number = int(number)  # Handle the '1eX' input cases

    if number < 0 or number > 999999999999:
        raise AttributeError("Number out of accepted range")
    if number == 0:
        return "zero"

    result = []
    strNum = str(number)
    # Divide inputString in groups of three digits, starting with the LSValue
    while len(strNum) % 3 != 0:
        strNum = '0' + strNum
    groupedNum = map(''.join, zip_longest(*[iter(strNum)]*3, fillvalue=''))
    groupedNum = [int(item) for item in groupedNum][::-1]
    
    for index, group in enumerate(groupedNum):
        tmp = ''
        if group > 0:
            hundreds    = int(group / 100)
            tens        = int((group - hundreds * 100) / 10)
            units       = int(group - hundreds * 100 - tens * 10)
            if hundreds > 0:
                tmp = " ".join([NUMBERS[hundreds], "hundred "])
                if tens > 0 or units > 0:
                    tmp += "and "
            if index == 0 and hundreds == 0 and len(groupedNum) > 1:
                tmp += "and "
            tmp += buildSpecialOnes(tens, units)
            if index > 0:
                tmp += " " + ORDERED_SUFFIXES[index]
            result = [tmp] + result

    return "".join(result).strip()