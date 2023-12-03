import re


def tls(x):
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))


with open("../input files/2016/2016.7.txt") as file:
    lines = [re.split(r'\[([^\]]+)\]', line) for line in file]
    parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
    print('Answer #1:', sum(tls(sn) and not (tls(hn)) for sn, hn in parts))
    print('Answer #2:',
          sum(any(a == c and a != b and b + a + b in hn for a, b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts))