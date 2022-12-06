# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
# input = "nppdvjthqldpwncqszvftbrmjlhg"
# input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
# input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

file = open("day06_input.txt", "r")
input = file.readline()
file.close()

for i in range(len(input) - 3):
    if len(set(input[i:i + 4])) == 4:
        print(i + 4)
        break
