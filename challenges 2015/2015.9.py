import sys
from itertools import permutations


def main():
    paths = []
    routeList = []
    destinations = set()
    distances = dict()
    with open("../input files/2015/2015.9.txt") as file:
        for line in file:
            (source, _, dest, _, distance) = line.split()
            destinations.add(source)
            destinations.add(dest)
            distances.setdefault(source, dict())[dest] = int(distance)
            distances.setdefault(dest, dict())[source] = int(distance)
        shortest = sys.maxsize
        longest = 0
        for items in permutations(destinations):
            dist = sum(map(lambda x, y: distances[x][y], items[1:], items[:-1]))
            shortest = min(shortest, dist)
            longest = max(longest, dist)
        print(shortest)
        print(longest)


if __name__ == "__main__":
    main()
