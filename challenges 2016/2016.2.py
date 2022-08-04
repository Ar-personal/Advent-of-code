keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

keypad = [[-1, -1, 1, -1, -1],
          [-1, 2, 3, 4, -1],
          [5, 6, 7, 8, 9],
          [-1, "A", "B", "C", -1],
          [-1, -1, "D", -1, -1]]

edges = [[0, 0], [0, 1], [0, 3], [0, 4],
         [1, 0], [1, 4],
         [3, 0], [3, 4],
         [4, 0], [4, 1], [4, 3], [4, 4]
        ]

directions = []
code = []
with open("../input files/2016/2016.2.txt") as file:
    for line in file:
        line = line.strip("\n")
        line_list = []
        for char in line:
            line_list.append(char)
        directions.append(line_list)
    position = [0, 2]
    value = keypad[position[1]][position[0]]
    vector = ()
    failedCount = 0
    for direction in directions:
        for i in range(0, len(direction)):
            if direction[i] == "U":
                vector = [0, -1]
            if direction[i] == "R":
                vector = [1, 0]
            if direction[i] == "D":
                vector = [0, 1]
            if direction[i] == "L":
                vector = [-1, 0]
            new_position = [position[0] + vector[0], position[1] + vector[1]]
            if new_position[0] > 4 or new_position[0] < 0 or new_position[1] < 0 or new_position[1] > 4 or new_position in edges:
                if failedCount >= 1 or i == len(direction) -1:
                    code.append(keypad[position[1]][position[0]])
                    continue
            else:
                failedCount = 0
                value = keypad[new_position[1]][new_position[0]]
                position = new_position
                if i == len(direction) - 1:
                    code.append(keypad[new_position[1]][new_position[0]])
                    continue

    print("".join(map(str, code)))