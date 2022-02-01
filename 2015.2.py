def main():
    paperNeeded = 0
    ribbonNeeded = 0
    with open("input files/2015.2.txt") as file:
        while line := file.readline():
            dims = parseBoxDims(line)
            paperNeeded += boxWrappingCalculator(dims[0], dims[1], dims[2])
            ribbonNeeded += ribbonCalculator(dims[0], dims[1], dims[2])
    print(paperNeeded, " " , ribbonNeeded)


def parseBoxDims(string):
    s = string.split("x")
    for i in range(len(s)):
        s[i] = int(s[i])
    return s


def boxWrappingCalculator(length, width, height):
    lw = 2 * length * width
    wh = 2 * width * height
    hl = 2 * height * length
    extra = smallestBoxDimension(lw, wh, hl) / 2
    return lw + wh + hl + extra


def smallestBoxDimension(x, y, z):
    if x <= y and x <= z:
        smallest = x
    elif y <= z:
        smallest = y
    else:
        smallest = z
    return smallest


def twoSmallestDimensions(length, width, height):
    paper = 0
    count = 0
    if length <= width or length <= height:
        paper += length + length
        count += 1
    if width < length or width < height:
        paper += width + width
        count += 1
    if height <= length and count < 2 or height <= width and count < 2:
        paper += height + height
    return paper


def ribbonCalculator(l, w, h):
    ribbon = twoSmallestDimensions(l, w, h)
    bow = boxVolume(l, w, h)
    return ribbon + bow


def boxVolume(l, w, h):
    return l * w * h


if __name__ == "__main__":
    main()
