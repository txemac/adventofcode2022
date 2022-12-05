import string

# input = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

file = open("day03_input.txt", "r")
input = file.read().splitlines()
file.close()

score = string.ascii_lowercase + string.ascii_uppercase

result = 0
for line in input:
    index = len(line) // 2
    item_shared = list(set(line[:index]) & set(line[index:]))[0]
    result += score.index(item_shared) + 1

print(result)
