import operator
import collections
lineDict = {3: [], 4: [], 5: []}
wireDict = {}
max = 65536

orderedDict = {}
translate = {'NOT': operator.__not__,
             'OR': operator.__or__,
             'LSHIFT': operator.__lshift__,
             'RSHIFT': operator.__rshift__,
             'AND': operator.__and__}


# c b b RSHIFT 3 -> e 209 f 52 v 837 d418
def main():
    with open("input files/2015.7.txt") as file:
        for line in file:
            line = line.strip('\n')
            line = line.split()
            lineLength = len(line)
            lineDict[lineLength].append(line)
    while checkInt(wireDict.get('a')) is False:
            for line in lineDict.get(3):
                if checkInt(line[0]):
                    if line[2] not in wireDict:
                        wireDict[line[2]] = int(line[0])
                elif line[0] in wireDict and line[2] not in wireDict:
                    wireDict[line[2]] = wireDict[line[0]]
            for line in lineDict.get(4):
                if line[1] in wireDict:
                    # making it so target variable is set only once
                    if line[3] not in wireDict:
                        wireDict[line[3]] = ~wireDict[line[1]]
                        if wireDict[line[3]] < 0:
                            wireDict[line[3]] = wireDict[line[3]] + max
            for line in lineDict.get(5):
                # making it so target variable is set only once
                if line[4] not in wireDict:
                    func = translate[line[1]]
                    try:
                            if checkInt(line[0]) and line[2] in wireDict:
                                wireDict[line[4]] = func(int(line[0]), wireDict[line[2]])
                            elif checkInt(line[2]) and line[0] in wireDict:
                                wireDict[line[4]] = func(wireDict[line[0]], int(line[2]))
                            elif line[0] in wireDict and line [2] in wireDict:
                                wireDict[line[4]] = func(wireDict[line[0]], wireDict[line[2]])
                    except KeyError:
                        pass
    print(wireDict.get('a'))
    b = wireDict.get('a')
    wireDict.clear()
    wireDict['b'] = b
    main()


def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


# parse input text
# unique char identifiers = new wire
# each wire initialized with value 0
# loop through text and handle commands


if __name__ == "__main__":
    main()
