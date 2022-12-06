# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
# input = "nppdvjthqldpwncqszvftbrmjlhg"
# input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
# input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

file = open("day06_input.txt", "r")
input = file.readline()
file.close()

for i in range(len(input) - 13):
    if len(set(input[i:i + 14])) == 14:
        print(i + 14)
        break
