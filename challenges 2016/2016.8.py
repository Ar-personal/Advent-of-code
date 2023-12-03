import numpy as np

screen = np.zeros((6, 50))


def rect(value):
    value = value.strip().split("x")
    value = (int(value[1]), int(value[0]))
    sub = np.where(0, np.arange(value[0] * value[1]).reshape(value), 1)
    screen[0:value[0], 0:value[1]] = sub


def rotate(axis, index, value):
    index = int(index[2:])
    if axis == "row":
        arr = screen[index, :]
        arr = np.roll(arr, value, axis=0)
        screen[index] = arr
    if axis == "column":
        arr = screen[:, index]
        arr = np.roll(arr, value, axis=0)
        screen[:, index] = arr


def display(s):
    print('\n'.join(''.join('X' if p else ' ' for p in row) for row in s))


with open("../input files/2016/2016.8.txt") as file:
    for line in file:
        line = line.split()
        if line[0] == "rect":
            rect(line[1])
        if line[0] == "rotate":
            rotate(line[1], line[2], int(line[4]))

    print(np.count_nonzero(screen))
    display(screen)
    #AFBUPZBJPS