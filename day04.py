# input = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8""".split("\n")

file = open("day04_input.txt", "r")
input = file.read().splitlines()
file.close()

# count = 0
# for line in input:
#     elf1_start, elf1_end, elf2_start, elf2_end = [int(x) for elfs in line.split(",") for x in elfs.split("-")]
#     elf1 = list(range(elf1_start, elf1_end + 1))
#     elf2 = list(range(elf2_start, elf2_end + 1))
#     count += 1 if set(elf1).issubset(elf2) or set(elf2).issubset(elf1) else 0
#
# print(count)


count = 0
for line in input:
    elf1_start, elf1_end, elf2_start, elf2_end = [int(x) for elfs in line.split(",") for x in elfs.split("-")]
    elf1 = list(range(elf1_start, elf1_end + 1))
    elf2 = list(range(elf2_start, elf2_end + 1))
    count += 1 if set(elf1) & set(elf2) else 0

print(count)
