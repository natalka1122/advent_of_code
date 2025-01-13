from __future__ import annotations
import re

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def the_hash(line):
    result = 0
    for symbol in line:
        result += ord(symbol)
        result *= 17
        result = result % 256
    return result


def process(line, boxes):
    my_match = re.match(r"^(\w+)(=)?(\d+)?(-?)$", line)
    if my_match is None:
        raise NotImplementedError
    print(my_match.groups())
    box_number = the_hash(my_match.group(1))
    print(f"box_number = {box_number}")
    if my_match.group(2) and my_match.group(3) and not my_match.group(4):
        found_flag = False
        for i in range(len(boxes[box_number])):
            if boxes[box_number][i][0] == my_match.group(1):
                found_flag = True
                boxes[box_number][i] = (boxes[box_number][i][0], int(my_match.group(3)))
                break
        if not found_flag:
            boxes[box_number].append((my_match.group(1), int(my_match.group(3))))
    elif my_match.group(4) and not my_match.group(2) and not my_match.group(3):
        for i in range(len(boxes[box_number])):
            print(boxes[box_number])
            if boxes[box_number][i][0] == my_match.group(1):
                boxes[box_number].pop(i)
                break
    else:
        raise NotImplementedError


def calc(boxes):
    result = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            result+= (i+1)*(j+1)*boxes[i][j][1]
    return result


def main():
    boxes = []
    for _ in range(265):
        boxes.append([])
    with open(FILENAME, "r") as file:
        for line in file.readline().split(","):
            process(line, boxes)
            print(f"boxes[0] = {boxes[0]}")
            print(f"boxes[1] = {boxes[1]}")
            print(f"boxes[3] = {boxes[3]}")
    print(calc(boxes))


if __name__ == "__main__":
    main()
