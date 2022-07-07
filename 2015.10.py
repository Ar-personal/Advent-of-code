from itertools import groupby
from pip._vendor.msgpack.fallback import xrange


def look_and_say(input_string, num_iterations):
    for i in xrange(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    return input_string

def main():
    print(len(look_and_say('1321131112', 50)))


if __name__ == "__main__":
    main()