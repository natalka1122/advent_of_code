# FILENAME = "demo2.txt"
FILENAME = "input.txt"

MAS = ["MMSS", "MSMS", "SMSM", "SSMM"]
A = "A"
MS = "MS"


def count_xmas(shirt, y0, x0):
    result = 0
    found_flag = True
    ms_line = ""
    for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        y = y0 + dy
        x = x0 + dx
        if 0 <= y < len(shirt) and 0 <= x < len(shirt[y]):
            if shirt[y][x] in MS:
                ms_line += shirt[y][x]
                continue
        found_flag = False
        break
    if found_flag and ms_line in MAS:
        return 1
    return 0


def main():
    shirt = []
    with open(FILENAME, "r") as file:
        for line in file:
            shirt.append(line)
    result = 0
    for y in range(len(shirt)):
        for x in range(len(shirt[y])):
            if shirt[y][x] == A:
                result += count_xmas(shirt, y, x)
    print(result)


if __name__ == "__main__":
    main()
