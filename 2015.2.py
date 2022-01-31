
def main():
    paperNeeded = 0
    with open("input files/2015.2.txt") as file:
        while line := file.readline():
            dims = parseBoxDims(line)
            paperNeeded += boxWrappingCalculator(dims[0], dims[1], dims[2])
    print(paperNeeded)


def parseBoxDims(string):
    s = string.split("x")
    for i in range(len(s)):
        s[i] = int(s[i])
    return s


def boxWrappingCalculator(length, width, height):
    lw = 2 * length * width
    wh = 2 * width * height
    hl = 2 * height * length
    extra = smallestBoxDimension(lw, wh, hl)
    return lw + wh + hl + extra


def smallestBoxDimension(x, y, z):
    if x <= y and x <= z:
        smallest = x
    elif y <= z:
        smallest = y
    else:
        smallest = z
    return smallest / 2

if __name__ == "__main__":
    main()
