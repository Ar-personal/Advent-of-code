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


def main(lines):
    sum = 0
    for line in lines:
       sum += int(sum_line(line))
    print(sum)
    

if __name__ == "__main__":
    lines = load_file('1.txt')
    main(lines)