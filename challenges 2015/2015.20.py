import math
target = int(36000000 / 11)

for i in range(1, target):
    presents = 0
    for j in range(1, 51):
        if i % j == 0:
            presents += (j + i/j) * 11
    if math.sqrt(i):
        presents -= 11*math.sqrt(i)
    if presents >= 36000000:
        print(i)
        exit()