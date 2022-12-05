import string

# input = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")

file = open("day03_input.txt", "r")
input = file.read().splitlines()
file.close()

score = string.ascii_lowercase + string.ascii_uppercase
#
# result = 0
# for line in input:
#     index = len(line) // 2
#     item_shared = list(set(line[:index]) & set(line[index:]))[0]
#     result += score.index(item_shared) + 1
#
# print(result)

result = 0
lines = iter(input)
for line1 in lines:
    line2 = next(lines)
    line3 = next(lines)
    item_shared = list(set(line1) & set(line2) & set(line3))[0]
    result += score.index(item_shared) + 1

print(result)
