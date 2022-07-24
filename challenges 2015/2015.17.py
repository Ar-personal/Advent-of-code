import itertools

containers = [43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38]
amounts = 0
count = 0
for i in range(len(containers)):
        subtotal = 0
        for combination in itertools.combinations(containers, i):
            if sum(combination) == 150:
                subtotal += 1
                if len(combination) == 4:
                    amounts += 1
        count += subtotal
        print(subtotal)
print(count)
print(amounts)