# def load_file(path):
#     with open(path, 'r', encoding='utf-8') as file:
#         lines = file.read().splitlines()
#         return lines

# def process_data(lines):
#     seeds = lines[0]
#     seed_soil = []
#     soil_fert = []
#     fert_water = []
#     water_light = []
#     light_temp = []
#     temp_humid = []
#     humid_loc = []
#     data=[]
#     data.append(seeds)
#     # seed-to-soil
#     i = 0
#     while True:
#         if lines[i] == '' or i == 0:
#             i += 1
#             continue
#         elif lines[i] == 'seed-to-soil map:':
#             seed_soil, i = extract('soil-to-fertilizer map:', lines, i)
#             data.append(seed_soil)
#         elif lines[i] == 'soil-to-fertilizer map:':
#             soil_fert, i = extract('fertilizer-to-water map:', lines, i)
#             data.append(soil_fert)
#         elif lines[i] == 'fertilizer-to-water map:':
#             fert_water, i = extract('water-to-light map:', lines, i)
#             data.append(fert_water)
#         elif lines[i] == 'water-to-light map:':
#             water_light, i = extract('light-to-temperature map:', lines, i)
#             data.append(water_light)
#         elif lines[i] == 'light-to-temperature map:':
#             light_temp, i = extract('temperature-to-humidity map:', lines, i)
#             data.append(light_temp)
#         elif lines[i] == 'temperature-to-humidity map:':
#             temp_humid, i = extract('humidity-to-location map:', lines, i)
#             data.append(temp_humid)
#         elif lines[i] == 'humidity-to-location map:':
#             humid_loc, i = extract('', lines, i)
#             data.append(humid_loc)
#             break
#         else:
#             i += 1
#     map_data(data)



# def map_data(data):
#     seeds = list(map(lambda x: int(x), string_to_array(data[0], ":")))
#     seed_dict = {}
#     for seed in seeds:
#         seed_dict[seed] = [seed]
#         for data_line in data[1:]:
#             seed_dict[seed].append(calculate_range(seed_dict[seed][-1], data_line))
    
#     low = min(seed_dict[key][-1] for key in seed_dict)
#     print(low)
            

# def calculate_range(value, data_line):
#     result = None
#     for ranges in data_line:
#         num_list = list(map(lambda x: int(x), string_to_array(ranges, None)))
#         dest =  num_list[0]
#         source = num_list[1]
#         range_length = num_list[2]
#         if not source <= value < (source + range_length):
#             continue
#         else:
#             result = dest + (value - source)
#     if result == None:
#         return value
#     else:
#         return result


# def string_to_array(string, delimiter):
#     if delimiter:
#         array = string.split(delimiter)[1].split(" ")
#     else:
#          array = string.split(" ")
#     array = list(filter(lambda a: a != "", array))
#     return array
    

# def extract(exit_str, lines, index):
#     list = []
#     while lines[index + 1] != exit_str:
#         if lines[index + 1] != '':
#             list.append(lines[index + 1])
#         index += 1
#         if index + 1 >= len(lines):
#             return list, index
#     return list, index + 1


# if __name__ == "__main__":
#     lines = load_file('5.txt')
#     process_data(lines)

# {79: [79, 81, 81, 81, 74, 78, 78, 82], 14: [14, 14, 53, 49, 42, 42, 43, 43], 55: [55, 57, 57, 53, 46, 82, 82, 86], 13: [13, 13, 52, 41, 34, 34, 35, 35]}
# P2

import sys


def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        return lines

def process_data(lines):
    seeds = lines[0]
    seed_soil = []
    soil_fert = []
    fert_water = []
    water_light = []
    light_temp = []
    temp_humid = []
    humid_loc = []
    data=[]
    data.append(seeds)
    # seed-to-soil
    i = 0
    while True:
        if lines[i] == '' or i == 0:
            i += 1
            continue
        elif lines[i] == 'seed-to-soil map:':
            seed_soil, i = extract('soil-to-fertilizer map:', lines, i)
            data.append(seed_soil)
        elif lines[i] == 'soil-to-fertilizer map:':
            soil_fert, i = extract('fertilizer-to-water map:', lines, i)
            data.append(soil_fert)
        elif lines[i] == 'fertilizer-to-water map:':
            fert_water, i = extract('water-to-light map:', lines, i)
            data.append(fert_water)
        elif lines[i] == 'water-to-light map:':
            water_light, i = extract('light-to-temperature map:', lines, i)
            data.append(water_light)
        elif lines[i] == 'light-to-temperature map:':
            light_temp, i = extract('temperature-to-humidity map:', lines, i)
            data.append(light_temp)
        elif lines[i] == 'temperature-to-humidity map:':
            temp_humid, i = extract('humidity-to-location map:', lines, i)
            data.append(temp_humid)
        elif lines[i] == 'humidity-to-location map:':
            humid_loc, i = extract('', lines, i)
            data.append(humid_loc)
            break
        else:
            i += 1
    map_data(data)


# if a seed exists in a range oh

def map_data(data):
    # x = get_range_overlaps(data)
    min = 79
    max = 79 + 14
    for i in range(82, 100):
        res = calculate_range(i, data[-1])
        if res is None:
            continue
        for o in reversed(data[:-1]):
            if 'seeds:' in o:
                if min < res <= max:
                    print(res)
                    print(i)
                    sys.exit(0)
                else:
                    break
            res = calculate_range(res, o)
            if res is None:
                break


        
def calculate_range(value, data_line):
    result = None
    for ranges in data_line:
        num_list = list(map(lambda x: int(x), string_to_array(ranges, None)))
        dest =  num_list[1]
        source = num_list[0]
        range_length = num_list[2]
        if not source <= value < (source + range_length):
            continue
        else:
            result = dest + (value - source)
    if result == None:
        return value
    else:
        return result
    

# def get_range_overlaps(data):
#     seeds = list(map(lambda x: int(x), string_to_array(data[0], ":")))
#     ranges = []
#     o = 0
#     for i in range(o, len(seeds)):
#         if i >= len(seeds):
#             break
#         ranges.append({seeds[o]: seeds[o] + seeds[o+1]})
#         o += 2
    
        
def string_to_array(string, delimiter):
    if delimiter:
        array = string.split(delimiter)[1].split(" ")
    else:
         array = string.split(" ")
    array = list(filter(lambda a: a != "", array))
    return array
    

def extract(exit_str, lines, index):
    list = []
    while lines[index + 1] != exit_str:
        if lines[index + 1] != '':
            list.append(lines[index + 1])
        index += 1
        if index + 1 >= len(lines):
            return list, index
    return list, index + 1


if __name__ == "__main__":
    lines = load_file('5.txt')
    process_data(lines)
