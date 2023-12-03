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
    gear_list = []
    num_list = []
    for row in lines:
        width = len(row)
        position[0] = 0
        for column in row:
            if column == '*':
                gear_list.append(position.copy())
            try:
                num_list.append((position.copy(), int(column)))
            except:
                if num_list:
                    coords_list.append(num_list.copy())
                    num_list = []
            position[0] += 1
        position[1] += 1
    print(calculate(coords_list, lines, width, height, gear_list))

def calculate(coords_list, lines, width, height, gear_list):
    total = 0
    for gear_pos in gear_list:
        adj_numbers = []
        for direction in directions:
            if gear_pos[1] + direction[1] < 0 or gear_pos[1] + direction[1] >= height:
                    continue
            if gear_pos[0] + direction[0] < 0 or gear_pos[0] + direction[0] >= width:
                continue
            char = lines[gear_pos[1] + direction[1]][gear_pos[0] + direction[0]]
            try:
                int(char)
                # get number from list
                number_position = [gear_pos[0] + direction[0], gear_pos[1] + direction[1]]
                # if this pos is already part of number that has been added to adj numbers then skip
                if prevent_dupe(number_position, adj_numbers):
                    continue
                adj_numbers.append(find_nums(coords_list, number_position))
            except:
                continue
        if len(adj_numbers) == 2:
            vals = []
            for value in adj_numbers:
                s = ''
                for data in value:
                    s += str(data[1])
                vals.append(int(s))
            ratio = vals[0] * vals[1]
            total += ratio
    return total

def find_nums(coords_list, number_position):
    for number_list in coords_list:
        for coord in number_list:
            if number_position == coord[0]:
                return number_list
            
def prevent_dupe(number_position, adj_numbers):
    for list in adj_numbers:
        for entry in list:
            for coord in entry:
                if coord == number_position:
                    return True
    return False
                

if __name__ == "__main__":
    main()