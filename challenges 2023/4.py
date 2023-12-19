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
    extend_rounds(winning_nums.copy(), my_nums, 0)
    print(len(winning_nums))
 
 
def extend_rounds(rounds, my_nums, i):
    wins = len(set(my_nums[i][1:]) & set(rounds[i][1:]))
    for w in range(0, wins):
        round_copy = [winning_nums[(i + 1) + w]]
        rounds[i + w + 1:i + w + 1] = round_copy
        w += 1
 
        # rounds[i + 2:i + 2] = list(round_copies)
        # my_copies = my_nums[i + 1: i + 1 + wins]
        # my_nums[i + 2:i + 2] = list(my_copies)
    if i + 1 > len(rounds):
        return
    extend_rounds(rounds, my_nums, i + 1)
 
 
if __name__ == "__main__":
    lines = load_file('4.txt')
    main(lines)