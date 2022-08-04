instructions = []

def perform_instruction(index):
    a = 1
    b = 0
    c = 0
    while index < len(instructions):
        split = instructions[index].split()
        split[1] = split[1].replace(',', '')
        li = instructions[index]
        li = li.replace(",", "")
        li = li.split()
        register = li[1]
        if li[1] == "a":
            register == "a"
        elif li[1] == "b":
            register == "b"
        command = li[0]

        if command == "hlf":
            if register == "a":
                a = a / 2
                index += 1
            elif register == "b":
                b = b / 2
                index += 1
        if command == "tpl":
            if register == "a":
                a *= 3
                index += 1
            elif register == "b":
                b *= 3
                index += 1
        if command == "inc":
            if register == "a":
                a += 1
                index += 1
            elif register == "b":
                b += 1
                index += 1
        if command == "jmp" or command == "jie" or command == "jio":
            jumper = ""
            if command == "jmp":
                value = li[1]
            else:
                jumper = li[1]
                value = li[2]
            if value[0] == "+":
                value = int(value[1:])
            else:
                value = 0 - int(value[1:])
            if command == "jmp":
                index += value
            elif command == "jio":
                if jumper == "a" and a == 1:
                    index += value
                elif jumper == "b" and b == 1:
                    index += value
                else:
                    index += 1
            elif command == "jie":
                if jumper == "a" and a % 2 == 0:
                    index += value
                elif jumper == "b" and b % 2 == 0:
                    index += value
                else:
                    index += 1
    print(b)


with open("../input files/2015.23.txt") as file:
    for line in file:
        instructions.append(line)
    perform_instruction(0)