import itertools

from numpy import vectorize

weapons = []
armor = []
rings = []

bhp = 104
bdmg = 8
barmr = 1

i = 0
with open("../input files/2015.21.txt") as file:
    for l in file:
        s = l.split()
        s = s[1:]
        s = list(map(int, s))
        if i < 5:
            weapons.append(s)
        elif i < 10:
            armor.append(s)
        elif i >= 10:
                rings.append(s)
        i += 1
    armor.append([0, 0, 0])
    rings.append([0, 0, 0])
    rings.append([0, 0, 0])


def simulate(php, pdmg, parmr):
    b = bhp
    while True:
        b -= max(1, pdmg - barmr)
        if b <= 0:
            return True
        php -= max(1, bdmg - parmr)
        if php <= 0:
            return False


m = 1e100
for w in weapons:
    for a in armor:
        for r, combo in itertools.combinations(rings, 2):
            health = 100
            cost = w[0] + a[0] + r[0] + combo[0]
            pdmg = w[1] + a[1] + r[1] + combo[1]
            parmor = w[2] + a[2] + r[2] + combo[2]
            if simulate(health, pdmg, parmor):
                m = min(m, cost)

ma = 0
for w in weapons:
    for a in armor:
        for r, combo in itertools.combinations(rings, 2):
            health = 100
            cost = w[0] + a[0] + r[0] + combo[0]
            pdmg = w[1] + a[1] + r[1] + combo[1]
            parmor = w[2] + a[2] + r[2] + combo[2]
            if not simulate(health, pdmg, parmor):
                ma = max(ma, cost)

print(m)
print(ma)