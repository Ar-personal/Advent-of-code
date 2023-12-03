# maximums = {"red": 12, "green": 13, "blue": 14}

# def parse(path):
#     with open(path) as file:
#             lines = file.readlines()
#             return lines
    

# def count(line):
#     id, data = line.replace("Game ", "").replace("\n", "").split(" ", 1)
#     rounds = data.split(";")
#     for round in rounds:
#         values = {"blue": 0, "green": 0, "red": 0}
#         count_split = round.split(" ")
#         current_num = None
#         for substring in count_split:
#             if substring == '':
#                 continue
#             try:
#                 current_num = int(substring)
#             except:
#                 if (substring[-1].isalpha()):
#                     values[(substring)] += current_num
#                 else:
#                     values[(substring[:-1])] += current_num
#                 continue
#         for v in values.keys():
#             if values.get(v) > maximums.get(v):
#                 return 0      
#     return int(id[:-1])





# def main():
#     lines = parse('./inputs/2023/2.txt')
#     # lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     #         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     #         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     #         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     #         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
#     total_Score = 0
#     for line in lines:
#         total_Score += count(line)
#     print(total_Score)

# if __name__ == "__main__":
#     main()



#part2

maximums = {"red": 12, "green": 13, "blue": 14}

def parse(path):
    with open(path) as file:
            lines = file.readlines()
            return lines
    

def count(line):
    id, data = line.replace("Game ", "").replace("\n", "").split(" ", 1)
    values = {"red": 0, "green": 0, "blue": 0}
    count_split = data.split(" ")
    current_num = None
    for substring in count_split:
        if substring == '':
            continue
        try:
            current_num = int(substring)
        except:
            if (substring[-1].isalpha()):
                if current_num > values[(substring)]:
                    values[(substring)] = current_num
            else:
                if current_num > values[(substring[:-1])]:
                    values[(substring[:-1])] = current_num
            continue
    power = 1
    for v in values.keys():
        power *= values.get(v)     
    return power


def main():
    lines = parse('./inputs/2023/2.txt')
    # lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
    total_Score = 0
    for line in lines:
        total_Score += count(line)
    print(total_Score)

if __name__ == "__main__":
    main()



