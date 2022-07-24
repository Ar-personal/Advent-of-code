def main():
    print(sum(len(s[:-1]) - len(eval(s)) for s in open("input files/2015.8.txt")))
    print(sum(2 + s.count('\\') + s.count('"') for s in open("input files/2015.8.txt")))


if __name__ == "__main__":
    main()
