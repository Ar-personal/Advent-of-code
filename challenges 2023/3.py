# directions = [(-1, -1), (0, -1), (1, -1),
#               (-1, 0), (1, 0),
#               (-1, 1), (0, 1), (1, 1)]


# def parse(path):
#     with open(path) as file:
#             lines = file.read().splitlines()
#             return lines


# def main():
#     lines = parse('./inputs/2023/3.txt')
#     position = [0, 0]
#     height = len(lines)
#     coords_list = []
#     num_list = []
#     for row in lines:
#         width = len(row)
#         position[0] = 0
#         for column in row:
#             try:
#                 num_list.append((position.copy(), int(column)))
#             except:
#                 if num_list:
#                     coords_list.append(num_list.copy())
#                     num_list = []
#             position[0] += 1
#         position[1] += 1
#     total = 0
#     for pos_list in coords_list:
#         total += calculate(pos_list, lines, width, height)
#     print(total)
 

# def calculate(pos_list, lines, width, height):
#     for pos in pos_list:
#         for direction in directions:
#             coord = pos[0]
#             print(coord)
#             if coord[1] + direction[1] < 0 or coord[1] + direction[1] >= height:
#                 continue
#             if coord[0] + direction[0] < 0 or coord[0] + direction[0] >= width:
#                 continue
#             char = lines[coord[1] + direction[1]][coord[0] + direction[0]]
#             if not (char).isalnum() and char is not '.':
#                 # valid num,ber add all values up
#                 number = ''
#                 for value in pos_list:
#                     number += str(value[1])
#                 return int(number)
#     return 0


# if __name__ == "__main__":
#     main()

# Part 2


directions = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1)]


def parse(path):
    with open(path) as file:
            lines = file.read().splitlines()
            return lines


def main():
    lines = parse('./inputs/2023/3.txt')
    position = [0, 0]
    height = len(lines)
    coords_list = []
    num_list = []
    for row in lines:
        width = len(row)
        position[0] = 0
        for column in row:
            try:
                num_list.append((position.copy(), int(column)))
            except:
                if num_list:
                    coords_list.append(num_list.copy())
                    num_list = []
            position[0] += 1
        position[1] += 1
    total = 0
    for pos_list in coords_list:
        total += calculate(pos_list, lines, width, height)
    print(total)
 

def calculate(pos_list, lines, width, height):
    star_count = 0
    for pos in pos_list:
        for direction in directions:
            coord = pos[0]
            print(coord)
            if coord[1] + direction[1] < 0 or coord[1] + direction[1] >= height:
                continue
            if coord[0] + direction[0] < 0 or coord[0] + direction[0] >= width:
                continue
            char = lines[coord[1] + direction[1]][coord[0] + direction[0]]
            if char is '*':
                star_count += 1
                # valid num,ber add all values up
                if star_count == 2:
                    
                number = ''
                for value in pos_list:
                    number += str(value[1])
                return int(number)
    return 0


if __name__ == "__main__":
    main()