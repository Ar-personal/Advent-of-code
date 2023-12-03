import itertools

with open('../input files/2015/2015.13.txt') as file:
    inputs = file.read().rstrip().split('\n')

people = []
relations = {}

def parse_input(input):
    args = input[0:-1].split()
    n = int(args[3])
    if args[2] == 'lose':
        n *= -1
    subject = args[0]
    if subject not in people:
        people.append(subject)
    neighbor = args[-1]
    relations[(subject, neighbor)] = n

for input in inputs:
    parse_input(input)

for person in people:
    relations[(person, 'me')] = 0
    relations[('me', person)] = 0
people.append('me')


def calculate_total(order):
    length = len(order)
    happiness = 0
    for n in range(length):
        p1 = order[n]
        p2 = order[(n + 1) % length]
        happiness += relations[(p1, p2)]
        happiness += relations[(p2, p1)]
    return happiness

# Since the table is circular, I can keep the first person in the same spot
# and only permute the order of people who come after.
first_person = people.pop(0)
orders = itertools.permutations(people)
max_happiness = 0
for order in orders:
    max_happiness = max(max_happiness, calculate_total([first_person] + list(order)))

print(max_happiness)