from typing import Literal


def score(
        elf: Literal['A', 'B', 'C'],
        me: Literal['X', 'Y', 'Z'],
) -> int:
    result = 0

    # selected
    if me == "X":
        result += 1
    elif me == "Y":
        result += 2
    elif me == "Z":
        result += 3

    # draw
    if (elf == "A" and me == "X") or \
            (elf == "B" and me == "Y") or \
            (elf == "C" and me == "Z"):
        result += 3

    # win
    if (elf == "A" and me == "Y") or \
            (elf == "B" and me == "Z") or \
            (elf == "C" and me == "X"):
        result += 6

    return result


assert score(elf="A", me="Y") == 8
assert score(elf="B", me="X") == 1
assert score(elf="C", me="Z") == 6

file = open("day02_input.txt", "r")
lines = file.read().splitlines()

total = 0
for line in lines:
    elf, me = line.split(" ")
    total += score(elf=elf, me=me)

print(total)
