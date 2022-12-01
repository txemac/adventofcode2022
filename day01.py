file = open("day01_input.txt", "r")
lines = file.read().splitlines()

elves = []
current = 0
for line in lines:
    if line != "":
        current += int(line)
    else:
        elves.append(current)
        current = 0

print(max(elves))

print(sum(sorted(elves, reverse=True)[:3]))
