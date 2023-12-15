import sys


mapping = {}

def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        return lines
          

def main():
    lines = load_file('challenges 2023/8.txt')
    directions = lines[0]
    for i, line in enumerate(lines[2:]):
        mapping[line[:3]] = line[7:10], line[12:15]
    # get wee list of every direction ending in A
    a_list = {k: v for k, v in mapping.items() if k.endswith('A')}  
    # run follow map twice appending the return until both end in z
    i = 0
    location_dict = {}
    location_dict[0] = list(a_list.keys())
    while True:
        for paths in list(location_dict.values()):
            for i, path in enumerate(paths):
                location_dict[i + 1] = follow_map(i, path, directions)
        z_list = {k: v for k, v in mapping.items() if k.endswith('Z')}
        if len(z_list) == len(a_list):
            quit() 
        i+=1
        


def follow_map(i, map, directions):
    o = i % len(directions)
    if directions[o] == 'L':
        map = mapping.get(map)[0]
    elif directions[o] == 'R':
        map = mapping.get(map)[1]
    print(i)
    return map

    

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    main()
