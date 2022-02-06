import numpy as np

lights = np.zeros((1000, 1000), dtype=np.int32)


def main():
    with open("input files/2015.6.txt") as file:
        for line in file:
            line = line.replace(',', ' ')
            line = line.split()
            if line[0] == "toggle":
                start = (int(line[1]), int(line[2]))
                end = (int(line[4]), int(line[5]))
                toggleLight(line[0], start, end)
            else:
                start = (int(line[2]), int(line[3]))
                end = (int(line[5]), int(line[6]))
                toggleLight(line[1], start, end)
    c = 0
    for row in range(1000):
        for col in range(1000):
            if lights[row][col] == 1:
                c += 1
    print("lights on: ", c)


def toggleLight(command, start, end):
    for yCol in range(start[1], end[1] + 1):
        for xCol in range(start[0], end[0] + 1):
            if command == "toggle":
                toggle(xCol, yCol)
            elif command == "on":
                lightOn(xCol, yCol)
            else:
                lightOff(xCol, yCol)


def lightOn(x, y):
    lights[y][x] = 1


def lightOff(x, y):
    lights[y][x] = 0


def toggle(x, y):
    if lights[y][x] == 1:
        lights[y][x] = 0
    else:
        lights[y][x] = 1


if __name__ == "__main__":
    main()
