from itertools import combinations


def count(asciiDiagram=""):
    count = 0
    apex = []
    foundRectangles = []

    for i in range(len(asciiDiagram)):
        for j in range(len(asciiDiagram[i])):
            curElem = asciiDiagram[i][j]
            if curElem == "+":
                apex.append((i, j))

    diagList = combinations(apex, 2)

    for coord1, coord2 in combinations(apex, 2):
        isARectangle = True

        # If elements are on the same line/column
        if coord1[0] == coord2[0] or coord1[1] == coord2[1]:
            continue
        # Find other summits of the rectangle and check that they are '+' too
        otherApexes = [(coord1[0], coord2[1]), (coord2[0], coord1[1])]
        for elem in otherApexes:
            if elem not in apex:
                isARectangle = False
                break

        if not isARectangle:
            continue

        borders = [(i, j) for i in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0]) + 1)
                 for j in range(min(coord1[1], coord2[1]), max(coord1[1], coord2[1]) + 1)
                 if (i in (coord1[0], coord2[0]) or j in (coord1[1], coord2[1]))
                 and (i, j) != coord1 and (i, j) != coord2 and (i,j) not in otherApexes]

        for element in borders:
            if element[0] in (coord1[0], coord2[0]) and not asciiDiagram[element[0]][element[1]] in ("-", "+"):
                isARectangle = False
                break
            if element[1] in (coord1[1], coord2[1]) and not asciiDiagram[element[0]][element[1]] in ("|", "+"):
                isARectangle = False
                break
        if isARectangle:
            newRect = sorted([coord1, coord2] + otherApexes)
            if not newRect in foundRectangles:
                foundRectangles += [sorted([coord1, coord2] + otherApexes)]
                count += 1
    return count