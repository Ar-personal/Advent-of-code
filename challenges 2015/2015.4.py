import codecs
import hashlib


def main():
    combineMD5(b"yzbqklnj")


def combineMD5(input):
    increment = 0
    criteria = '000000'
    hash = hashlib.md5(input + str(increment).encode()).hexdigest()
    while hash[0:6] != criteria:
        increment += 1
        hash = hashlib.md5(input + str(increment).encode()).hexdigest()
    print(increment)
    print(hash)


if __name__ == "__main__":
    main()