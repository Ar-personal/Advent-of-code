with open("../input files/2016/2016.3.txt") as file:
    count = 0
    for line in file:
        m = 0
        line = line.strip().split()
        line = list(map(int, line))
        m = max(line)
        line.remove(m)
        if line[0] + line[1] > m:
            count += 1
    print(count)