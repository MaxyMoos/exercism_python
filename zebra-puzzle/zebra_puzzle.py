class Nation():
    Englishman = 1
    Spaniard = 2
    Ukrainian = 3
    Norwegian = 4
    Japanese = 5

class Color():
    Red = 1
    Green = 2
    Ivory = 3
    Yellow = 4
    Blue = 5

class Drink():
    Coffee = 1
    Tea = 2
    Milk = 3
    OrangeJ = 4
    Water = 5

class Cigs():
    OldGold = 1
    Kool = 2
    Chesterfield = 3
    LuckyStrike = 4
    Parliament = 5

class HousePos():
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5

class Pet():
    Dog = 1
    Snails = 2
    Fox = 3
    Horse = 4
    Zebra = 5


class House():
    def __init__(self, index=None, color=None, ownerNationality=None, cigs=None, drink=None, animal=None):
        self.index = index
        self.color = color
        self.ownerNat = ownerNationality
        self.cigs = cigs
        self.drink = drink
        self.animal = animal

    def __eq__(self, other):
        return self.index == other.index and self.color == other.color and self.ownerNat == other.ownerNat \
            and self.cigs == other.cigs and self.drink == other.drink and self.animal == other.animal


def house_is_possible(house):
    global GLOBAL_ERRORS_SINGLE
    # 1
    if not house.index in range(1,6):
        return False
    # 2
    if house.ownerNat == Nation.Englishman and house.color != Color.Red or house.color == Color.Red and house.ownerNat != Nation.Englishman:
        return False
    # 3
    if house.ownerNat == Nation.Spaniard and house.animal != Pet.Dog or house.animal == Pet.Dog and house.ownerNat != Nation.Spaniard:
        return False
    # 4
    if house.drink == Drink.Coffee and house.color != Color.Green or house.color == Color.Green and house.drink != Drink.Coffee:
        return False
    # 5
    if house.ownerNat == Nation.Ukrainian and house.drink != Drink.Tea or house.drink == Drink.Tea and house.ownerNat != Nation.Ukrainian:
        return False
    # 6
    if house.color == Color.Green and house.index == HousePos.One:
        return False
    if house.color == Color.Ivory and house.index == HousePos.Five:
        return False
    # 7
    if house.cigs == Cigs.OldGold and house.animal != Pet.Snails or house.animal == Pet.Snails and house.cigs != Cigs.OldGold:
        return False
    # 8
    if house.cigs == Cigs.Kool and house.color != Color.Yellow or house.color == Color.Yellow and house.cigs != Cigs.Kool:
        return False
    # 9
    if house.drink == Drink.Milk and house.index != HousePos.Three or house.index == HousePos.Three and house.drink != Drink.Milk:
        return False
    # 10
    if house.ownerNat == Nation.Norwegian and house.index != HousePos.One or house.index == HousePos.One and house.ownerNat != Nation.Norwegian:
        return False
    # 11
    if house.cigs == Cigs.Chesterfield and house.animal == Pet.Fox:
        return False
    # 12
    if house.cigs == Cigs.Kool and house.animal == Pet.Horse:
        return False
    # 13
    if house.cigs == Cigs.LuckyStrike and house.drink != Drink.OrangeJ or house.drink == Drink.OrangeJ and house.cigs != Cigs.LuckyStrike:
        return False
    # 14
    if house.ownerNat == Nation.Japanese and house.cigs != Cigs.Parliament or house.cigs == Cigs.Parliament and house.ownerNat != Nation.Japanese:
        return False
    # 15
    if house.ownerNat == Nation.Norwegian and house.color == Color.Blue:
        return False
    return True


def houses_are_possible(houses):
    maxL = len(houses)
    for index, house in enumerate(houses):
        # 6
        if house.color == Color.Ivory and index < maxL-1 and houses[index+1].color != Color.Green or house.color == Color.Ivory and index == 5:
            return False
        # 11
        if house.cigs == Cigs.Chesterfield:
            neighbors = []
            if index > 0:
                neighbors.append(houses[index-1])
            if index < maxL-1:
                neighbors.append(houses[index+1])
            if len(neighbors) > 0 and len([item for item in neighbors if item.animal == Pet.Fox]) == 0:
                return False
        # 12
        if house.cigs == Cigs.Kool:
            neighbors = []
            if index > 0:
                neighbors.append(houses[index-1])
            if index < maxL - 1:
                neighbors.append(houses[index+1])
            if len(neighbors) > 0 and len([item for item in neighbors if item.animal == Pet.Horse]) == 0:
                return False
        # 15
        if house.ownerNat == Nation.Norwegian:
            neighbors = []
            if index > 0:
                neighbors.append(houses[index-1])
            if index < maxL - 1:
                neighbors.append(houses[index+1])
            if len(neighbors) > 0 and len([item for item in neighbors if item.color == Color.Blue]) == 0:
                return False
    return True


def solution():
    from random import choice
    from math import pow
    from operator import add

    houses = []
    result = False

    while not result:
        houses = []
        valuePool = [list(range(1,6)), list(range(1,6)), list(range(1,6)), list(range(1,6)), list(range(1,6))]
        counter = 1
        while len(houses) < 5:
            tmpValuePool = [list(item) for item in valuePool]
            randChoice = [choice(item) for item in tmpValuePool]
            args = [len(houses) + 1] + randChoice
            newHouse = House(*args)
            counter += 1
            tmpHouses = houses + [newHouse]
            if house_is_possible(newHouse) and houses_are_possible(tmpHouses):
                counter = 1
                houses = tmpHouses
                for index, item in enumerate(tmpValuePool):
                    item.remove(randChoice[index])
                    valuePool = tmpValuePool
            if len(houses) == 5:
                break
            if counter > int(pow(len(tmpValuePool[0]), 5)) and len(houses) > 0:
                # Consider all possible values to have been tried, we need to go back one step
                counter = 1
                lastHouse = houses[-1]
                buf = [[lastHouse.color], [lastHouse.ownerNat], [lastHouse.cigs], [lastHouse.drink], [lastHouse.animal]]
                valuePool = [item for item in map(add, buf, valuePool)]
                houses.remove(lastHouse)
        result = True

    waterDrinker = [house for house in houses if house.drink == Drink.Water][0]
    zebraOwner = [house for house in houses if house.animal == Pet.Zebra][0]
    Nationalities = {1:"Englishman", 2:"Spaniard", 3:"Ukrainian", 4:"Norwegian", 5:"Japanese"}

    return ("It is the " + Nationalities[waterDrinker.ownerNat] + " who drinks the water.\n"
            "The " + Nationalities[zebraOwner.ownerNat] + " keeps the zebra.")