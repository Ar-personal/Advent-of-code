import json

def main():
    with open('../input files/2015/2015.12.JSON') as file:
        obj = json.loads(file.read())
        print(sumObject(obj))


def sumObject(obj):
    if type(obj) is int:
        return obj
    if type(obj) is list:
        return sum(map(sumObject, obj))
    if type(obj) is dict:
        vals = obj.values()

        # remove these two lines for part one
        if "red" in vals:
            return 0

        return sum(map(sumObject, vals))

    else:
        return 0

    #             minus = False
    #             if idx == len(line):
    #                 break
    #             if line[idx].isdigit():
    #                 number = line[idx]
    #                 if line[idx -1] == '-':
    #                     minus = True
    #                     number = '-' + number
    #                 inc = 1
    #                 while line[idx + inc].isdigit():
    #                     number += line[idx + inc]
    #                     inc += 1
    #                 total += int(number)
    #                 if minus:
    #                     idx += len(number) -1
    #                 else:
    #                     idx += len(number)
    #                 continue
    #             idx += 1
    # print(total)


if __name__ == "__main__":
    main()