blacklist = ["ab", "cd", "pq", "xy"]


def main():
    niceCount = 0
    with open("2015.5.txt") as file:
        for line in file:
            line = line.strip("\n")
            if contains3Vowels(line) and contains2CharInRow(line) and not containsBLString(line, blacklist):
                niceCount += 1
    print(niceCount)


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