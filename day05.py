"""
[F]         [L]     [M]
[T]     [H] [V] [G] [V]
[N]     [T] [D] [R] [N]     [D]
[Z]     [B] [C] [P] [B] [R] [Z]
[M]     [J] [N] [M] [F] [M] [V] [H]
[G] [J] [L] [J] [S] [C] [G] [M] [F]
[H] [W] [V] [P] [W] [H] [H] [N] [N]
[J] [V] [G] [B] [F] [G] [D] [H] [G]
 1   2   3   4   5   6   7   8   9
"""

# """
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# """
# input = """move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2""".splitlines()
#
# stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]

file = open("day05_input.txt", "r")
input = [line for line in file.readlines() if line.startswith("move")]
file.close()

stacks = [
    ["J", "H", "G", "M", "Z", "N", "T", "F"],
    ["V", "W", "J"],
    ["G", "V", "L", "J", "B", "T", "H"],
    ["B", "P", "J", "N", "C", "D", "V", "L"],
    ["F", "W", "S", "M", "P", "R", "G"],
    ["G", "H", "C", "F", "B", "N", "V", "M"],
    ["D", "H", "G", "M", "R"],
    ["H", "N", "M", "V", "Z", "D"],
    ["G", "N", "F", "H"]
]

for line in input:
    split_line = line.split()
    num = int(split_line[1])
    # stack_from = int(split_line[3]) - 1
    # stack_to = int(split_line[5]) - 1
    stack_from = stacks[int(split_line[3]) - 1]
    stack_to = stacks[int(split_line[5]) - 1]

    stack_to += stack_from[len(stack_from) - num:]
    for _ in range(num):
        # stacks[stack_to].append(stacks[stack_from].pop())
        stack_from.pop()

print("".join([x.pop() for x in stacks]))
