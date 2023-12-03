import hashlib

import numpy


def main():
    combineMD5()


def combineMD5():
    increment = 0
    password = {}
    salt = b"cxdnnyjw"

    while len(password) < 8:
        hash = hashlib.md5(salt + str(increment).encode()).hexdigest()
        if hash.startswith("00000"):
                index = int(hash[5], 16)
                val = hash[6]
                if index in range(8) and index not in password:
                    password[index] = val

                    pass_str = ['_'] * 8
                    for key, val in password.items():
                        pass_str[key] = val
                    print(''.join(pass_str))

        increment += 1


if __name__ == "__main__":
    main()