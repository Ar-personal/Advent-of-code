# Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
# Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
# Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
# Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
from collections import defaultdict, namedtuple

cookies = []
Specs = namedtuple('Specs', 'capacity, durability, flavour, texture, calories')
with open("../input files/2015.15.txt") as f:
    for line in f:
        line = line.replace(",", "").strip()
        name, capacity, durability, flavour, texture, calories = line.split()[0], int(line.split()[2]), int(
            line.split()[4]), int(line.split()[6]), int(line.split()[8]), int(line.split()[10])
        cookies.append(([capacity, durability, flavour, texture, calories]))


def find_max_score():
    score = 0
    max = 0
    for i in range(0, 100):
        for j in range(0, 100):
            for k in range(0, 100 - i - j):
                h = 100 - i - j - k
                a = cookies[0][0] * i + cookies[1][0] * j + cookies[2][0] * k + cookies[3][0] * h
                b = cookies[0][1] * i + cookies[1][1] * j + cookies[2][1] * k + cookies[3][1] * h
                c = cookies[0][2] * i + cookies[1][2] * j + cookies[2][2] * k + cookies[3][2] * h
                d = cookies[0][3] * i + cookies[1][3] * j + cookies[2][3] * k + cookies[3][3] * h
                e = cookies[0][4] * i + cookies[1][4] * j + cookies[2][4] * k + cookies[3][4] * h
                if not e == 500:
                    continue
                if a <= 0 or b <= 0 or c <= 0 or d <= 0:
                    continue
                score = a * b * c * d
                if score > max:
                    max = score
    print(max)


if __name__ == "__main__":
    find_max_score()
