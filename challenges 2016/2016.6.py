from collections import Counter

with open('../input files/2016/2016.6.txt') as f:
    s = f.read().strip()
# Part 1
print(''.join(Counter(x).most_common()[0][0] for x in zip(*s.split('\n'))))
# Part 2
print(''.join(Counter(x).most_common()[-1][0] for x in zip(*s.split('\n'))))