# def charRepeatsWithGap(string, gap):
#     i = 0
#     while i < len(string):
#         if i + (gap + 1) >= len(string):
#             return False
#         char = string[i]
#         nextChar = string[i + (gap + 1)]
#         if nextChar == char:
#             return True
#         i += 1
#     return False
#
#
# def contains3Vowels(string):
#     vowels = "aeiou"
#     vowelCount = 0
#
# def containsLetterPairs(string):
#     substr = ''
#     i = 0
#     while i < len(string) - 1:
#         substr = string[i:i + 2]
#         if string.count(substr) >= 2:
#             return True
#         i += 1
#     return False
#
#
# with open("2015.5.txt") as file:
#     for line in file:
#         line = line.strip("\n")
#         if contains3Vowels(line) and contains2CharInRow(line) and not containsBLString(line, blacklist):
#         # if contains3Vowels(line) and contains2CharInRow(line) and not containsBLString(line, blacklist):
#         if containsLetterPairs(line) and charRepeatsWithGap(line, 1):
#             niceCount += 1
#
# print(niceCount)





