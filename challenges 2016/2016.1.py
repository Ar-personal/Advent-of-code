import math

instructions = []
coords_list = []


def appendAndCheck(coord):
    if coord in coords_list:
        print(abs(coord[0]) + abs(coord[1]))
        exit()
    coords_list.append(coord)


def move(angle, amount, position):
    amount = int(amount)
    move_y = 0
    move_x = 0
    for i in range(amount):
        if angle == 90:
            move_x += 1
        if angle == 270:
            move_x -= 1
        if angle == 180:
            move_y -= 1
        if angle == 0:
            move_y += 1
        appendAndCheck((position[0] + move_x, position[1] + move_y))
    return position[0] + move_x, position[1] + move_y


with open("../input files/2016/2016.1.txt") as file:
    coords_list = []
    for line in file:
        line = line.split()
        for i in line:
            i = i.replace(",", "")
            instructions.append(i)
    coords = (0, 0)
    coords_list.append(coords)
    turn = 0
    for i in range(0, len(instructions)):
        inst = instructions[i]
        if inst[0] == "L":
            turn -= 90
        if inst[0] == "R":
            turn += 90
        if turn == 360:
            turn = 0
        if turn < 0:
            turn = 270
        if turn > 360:
            turn = 90
        coords = move(turn, inst[1:], coords)
    print(abs(coords[0]) + abs(coords[1]))