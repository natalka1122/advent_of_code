from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def find_vertical(pattern):
    # print(pattern)
    width = len(pattern[0])
    # print(width, list(range(1, width - 1)))
    for x0 in range(1, width):
        is_good_x0 = True
        # print(x0, list(range(1,1+min(x0, width-x0))))
        for dx in range(1, 1 + min(x0, width - x0)):
            # print(f"x0 = {x0} dx = {dx} x0+dx-1 = {x0+dx-1} x0-dx = {x0-dx}")
            for y in range(len(pattern)):
                if pattern[y][x0 + dx - 1] != pattern[y][x0 - dx]:
                    is_good_x0 = False
                    break
            if not is_good_x0:
                break
        if is_good_x0:
            print(f"x0 = {x0} is good")
            return x0
    return 0


def find_horizontal(pattern):
    # print(pattern)
    height = len(pattern)
    # print(height, list(range(1, height - 1)))
    for y0 in range(1, height):
        is_good_y0 = True
        # print(x0, list(range(1,1+min(x0, width-x0))))
        for dy in range(1, 1 + min(y0, height - y0)):
            # print(f"y0 = {y0} dy = {dy} y0+dy-1 = {y0+dy-1} y0-dy = {y0-dy}")
            for x in range(len(pattern[0])):
                if pattern[y0 + dy - 1][x] != pattern[y0 - dy][x]:
                    is_good_y0 = False
                    break
            if not is_good_y0:
                break
        if is_good_y0:
            print(f"y0 = {y0} is good")
            return y0
    raise NotImplementedError


def find_mirror(pattern):
    vertical = find_vertical(pattern)
    if vertical != 0:
        return vertical
    return 100 * find_horizontal(pattern)


def main():
    result = 0
    with open(FILENAME, "r") as file:
        pattern = []
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                result += find_mirror(pattern)
                pattern = []
            else:
                pattern.append(line)
    result += find_mirror(pattern)
    print(result)


if __name__ == "__main__":
    main()
