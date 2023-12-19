my_nums = []
winning_nums = []

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        return lines

def extract_nums(line):
    winning, mine = line.split('|')
    card, win_nums = winning.split(':')
    card = card.replace('Card ', '')
    winning_nums.append(list(map(lambda x: int(x), string_to_array(card + win_nums, " "))))
    my_nums.append(list(map(lambda x: int(x), string_to_array(card + mine, " "))))


def string_to_array(string, delimiter):
    array = string.split(delimiter)
    array = list(filter(lambda a: a != "", array))
    return array


# def main(lines):
#     for line in lines:
#         extract_nums(line)
#     total = 0
    # for i in range(0, len(winning_nums)):
    #     round_score = pow(2, len(set(my_nums[i]) & set(winning_nums[i])) - 1)
    #     if round_score >= 1:
    #         total += round_score
    # print(total)

# PART 2

def main(lines):
    for line in lines:
        extract_nums(line)
    calculate_scores()


def calculate_scores():
    # calculate wins
    win_dict = dict()
    wins = 0
    for i in range(0, len(winning_nums)):
        wins = len(set(winning_nums[i][1:]) & set(my_nums[i][1:]))
        win_dict[winning_nums[i][0]] = [wins]
    #algo
    for card in win_dict:
        wins = win_dict.get(card)
        for win in wins:
            for i in range(0, wins[0]):
                win_dict[card + i + 1].append(win_dict.get(card + i + 1)[0])
    
    total = 0
    for list in win_dict:
        array = win_dict.get(list)
        for num in array:
            total += 1
    print(total)


if __name__ == "__main__":
    lines = load_file('4.txt')
    main(lines)