from collections import Counter


card_ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        return lines
          

def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def max_kicker(hand1, hand2):
    for i, card in enumerate(hand1):
        if card_ranks.get(card) > card_ranks.get(hand2[i]):
            return True
        elif card_ranks.get(card) == card_ranks.get(hand2[i]):
            continue
        return False
        
        
def calc_score(sorted_list):
    score = 0
    for i in range(0, len(sorted_list)):
        score += int(sorted_list[i][-1]) * (i + 1)
    print(score)


def main():
    lines = load_file('7.txt')
    hands = []

    for line in lines:
        hand, bid = line.split()
        print(line)
        hands.append([hand, score_hand(hand), bid])
    hands = sorted(hands, key=lambda x: x[1])
    for i, hand in enumerate(hands):
        j = i + 1
        if i + 1 >= len(hands): break
        while hands[i][1] == hands[j][1] :
            if max_kicker(hands[i][0], hands[j][0]):
                hands = swap_positions(hands, i, j)
            j+=1
            if j >= len(hands): break
    calc_score(hands)
        

def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def score_hand(hand):
    if hand.count('J') == 5:
        return 25
    if 'J' in hand:
        # find winning hand
        result = Counter(hand.replace('J', ''))
        # two_sum = sum(count == 2 for count in result.values())
        # if two_sum == 2: # two of a kind with jack
        #     result = max(card_ranks.get(list(result.keys())[0]), card_ranks.get(list(result.keys())[1]))
        # else: 
        result = max(result, key=lambda k: result[k])
        x = hand.replace('J', str(result))
        return sum(map(x.count, x))
    else:
        return sum(map(hand.count, hand))


if __name__ == "__main__":
    main()