# FILENAME = "demo1.txt"
FILENAME = "input.txt"

XMAS = "XMAS"


def count_xmas(shirt, y0, x0):
    result = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            found_flag = True
            for index, letter in enumerate(XMAS):
                if index == 0:
                    continue
                y = y0 + index * dy
                x = x0 + index * dx
                if 0 <= y < len(shirt) and 0 <= x < len(shirt[y]):
                    if letter == shirt[y][x]:
                        continue
                found_flag = False
                break
            if found_flag:
                result += 1

    return result


def main():
    shirt = []
    with open(FILENAME, "r") as file:
        for line in file:
            shirt.append(line)
    result = 0
    for y in range(len(shirt)):
        for x in range(len(shirt[y])):
            if shirt[y][x] == XMAS[0]:
                result += count_xmas(shirt, y, x)
    print(result)


if __name__ == "__main__":
    main()
