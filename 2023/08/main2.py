import re
from math import gcd
from functools import reduce

# FILENAME = "demo1_1.txt"
# FILENAME = "demo1_2.txt"
# FILENAME = "demo2.txt"
FILENAME = "input.txt"
START = "A"
FINISH = "Z"
INDEX = "LR"

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

def main():
    the_map = dict()
    with open(FILENAME, "r") as file:
        instructions = file.readline().strip()
        file.readline()
        for line in file:
            key, left, right = re.match(
                r"(\w{3})\s=\s\((\w{3}),\s(\w{3})\)", line
            ).groups()
            the_map[key] = (left, right)
    step = 0
    positions:list[str] =  [item for item in the_map if item.endswith(START)]
    rounds = []
    for _ in range(len(positions)):
        rounds.append(False)
    while not all(rounds):
        instruction_index = INDEX.index(instructions[step%len(instructions)])
        for index in range(len(positions)):
            if not positions[index]:
                continue
            positions[index] = the_map[positions[index]][instruction_index]
            if positions[index].endswith(FINISH):
                if (step+1)%len(instructions) != 0:
                    raise NotImplementedError
                rounds[index] = step+1
                positions[index] = False
        step += 1
    print(rounds)
    print(lcm_of_list(rounds))


if __name__ == "__main__":
    main()
