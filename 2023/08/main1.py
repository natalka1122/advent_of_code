import re

# FILENAME = "demo1_1.txt"
# FILENAME = "demo1_2.txt"
FILENAME = "input.txt"
START = "AAA"
FINISH = "ZZZ"
INDEX = "LR"


def main():
    result = 0
    the_map = dict()
    with open(FILENAME, "r") as file:
        instruction = file.readline().strip()
        print(instruction)
        file.readline()
        for line in file:
            key, left, right = re.match(
                r"(\w{3})\s=\s\((\w{3}),\s(\w{3})\)", line
            ).groups()
            the_map[key] = {"L": left, "R": right}
    print(the_map)
    step = 0
    position = START
    while position != FINISH:
        position = the_map[position][instruction[step % len(instruction)]]
        step += 1
        print(step, position)
    print(step)


if __name__ == "__main__":
    main()
