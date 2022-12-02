from typing import Literal


# def score(
#         elf: Literal['A', 'B', 'C'],
#         me: Literal['X', 'Y', 'Z'],
# ) -> int:
#     result = 0
#
#     # selected
#     if me == "X":
#         result += 1
#     elif me == "Y":
#         result += 2
#     elif me == "Z":
#         result += 3
#
#     # draw
#     if (elf == "A" and me == "X") or \
#             (elf == "B" and me == "Y") or \
#             (elf == "C" and me == "Z"):
#         result += 3
#
#     # win
#     if (elf == "A" and me == "Y") or \
#             (elf == "B" and me == "Z") or \
#             (elf == "C" and me == "X"):
#         result += 6
#
#     return result
#
#
# assert score(elf="A", me="Y") == 8
# assert score(elf="B", me="X") == 1
# assert score(elf="C", me="Z") == 6

def score(
        elf: Literal['A', 'B', 'C'],
        round_end: Literal['X', 'Y', 'Z'],
) -> int:
    result = 0

    # lose
    if round_end == "X":
        if elf == "A":
            result += 3
        elif elf == "B":
            result += 1
        elif elf == "C":
            result += 2

    # draw
    elif round_end == "Y":
        result += 3
        if elf == "A":
            result += 1
        elif elf == "B":
            result += 2
        elif elf == "C":
            result += 3

    # win
    elif round_end == "Z":
        result += 6
        if elf == "A":
            result += 2
        elif elf == "B":
            result += 3
        elif elf == "C":
            result += 1

    return result


assert score(elf="A", round_end="Y") == 4
assert score(elf="B", round_end="X") == 1
assert score(elf="C", round_end="Z") == 7

file = open("day02_input.txt", "r")
lines = file.read().splitlines()

total = 0
for line in lines:
    column_1, column_2 = line.split(" ")
    total += score(elf=column_1, round_end=column_2)

print(total)
