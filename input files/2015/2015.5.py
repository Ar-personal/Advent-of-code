blacklist = ["ab", "cd", "pq", "xy"]


def main():
    niceCount = 0
    with open("2015.5.txt") as file:
        for line in file:
            line = line.strip("\n")
            # if contains3Vowels(line) and contains2CharInRow(line) and not containsBLString(line, blacklist):
            if containsLetterPairs(line) and charRepeatsWithGap(line, 1):
                niceCount += 1

    print(niceCount)


def containsLetterPairs(string):
    substr = ''
    i = 0
    while i < len(string) -1:
        substr = string[i:i + 2]
        if string.count(substr) >= 2:
            return True
        i += 1
    return False


def charRepeatsWithGap(string, gap):
    i = 0
    while i < len(string):
        if i + (gap + 1) >= len(string):
            return False
        char = string[i]
        nextChar = string[i + (gap + 1)]
        if nextChar == char:
            return True
        i += 1
    return False


def contains3Vowels(string):
    vowels = "aeiou"
    vowelCount = 0
    for v in vowels:
        counter = string.count(v)
        vowelCount += counter
    if vowelCount >= 3:
        return True
    return False


def contains2CharInRow(string):
    prev = ''
    for s in string:
        if s == prev:
            return True
        prev = s
    return False


def containsBLString(inp, li):
    for i in li:
        if i in inp:
            return True
    return False


if __name__ == "__main__":
        main()