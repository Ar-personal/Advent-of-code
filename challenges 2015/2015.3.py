housesDict = {}


def main():
    locationSanta = (0, 0)
    locationRoboSanta = (0, 0)
    housesDict[locationSanta] = 0
    deliverPresent(locationSanta)
    deliverPresent(locationRoboSanta)
    index = 0
    with open("../input files/2015/2015.3.txt") as file:
        for line in file:
            for ch in line:
                if (index % 2) == 0:
                    locationSanta = moveInDirection(locationSanta, ch)
                    checkLocation(locationSanta)
                    deliverPresent(locationSanta)
                else:
                    locationRoboSanta = moveInDirection(locationRoboSanta, ch)
                    checkLocation(locationRoboSanta)
                    deliverPresent(locationRoboSanta)
                index += 1
    print(countPresents(housesDict, 1))


def checkLocation(location):
    if location not in housesDict:
        housesDict[location] = 0


def deliverPresent(location):
    housesDict[location] += 1


def moveInDirection(location, direction):
    locationList = list(location)
    if direction == '>':
        locationList[0] += 1
        newLocation = tuple(locationList)
    if direction == '<':
        locationList[0] -= 1
        newLocation = tuple(locationList)
    if direction == '^':
        locationList[1] += 1
        newLocation = tuple(locationList)
    if direction == 'v':
        locationList[1] -= 1
        newLocation = tuple(locationList)

    return newLocation


def countPresents(dict, min):
    housesWithPresents = 0
    for key in dict:
        if dict[key] >= min:
            housesWithPresents += 1
    return housesWithPresents


if __name__ == "__main__":
    main()
