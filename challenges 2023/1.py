numdict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        return lines
    

def sum_line(line):
    first = None
    last = None
    for c in line:
        try:
            if first is None:
                first = int(c)
            else:
                last = int(c)
        except:
            continue
    if last is None: last = first
    return str(first) + str(last)


def parse_line(line):
    for i in numdict:
        if i in line:
            start = 0
            while(line.find(i, start)!=-1):
                p = line.find(i, start)
                index = p + len(i)
                start = index
                line = line[:index] + str(numdict.get(i))+i[len(i)-1] + line[index:]
    return line


def main(lines):
    sum = 0
    for line in lines:
       line = parse_line(line)
       sum += int(sum_line(line))
    print(sum)
    

if __name__ == "__main__":
    lines = load_file('1.txt')
    # lines = ["zoneight",
    #         "sevenine",
    #         "abcone2threexyz",
    #         "xtwone3four",
    #         "4nineeightseven2",
    #         "zoneight234",
    #         "sgtwo7"]
    main(lines)


