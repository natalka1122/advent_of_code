FILENAME = "demo.txt"  # expected 8
FILENAME = "input.txt"


def main() -> None:
    the_map: list[list[int]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(list(map(int, line.strip())))
    print(the_map)
    result = 0
    for y0 in range(len(the_map)):
        for x0 in range(len(the_map[0])):
            a = 0
            for y in range(y0 - 1, -1, -1):
                if the_map[y][x0] < the_map[y0][x0]:
                    a += 1
                else:
                    a += 1
                    break
            b = 0
            for y in range(y0 + 1, len(the_map)):
                if the_map[y][x0] < the_map[y0][x0]:
                    b += 1
                else:
                    b += 1
                    break
            c = 0
            for x in range(x0 - 1, -1, -1):
                if the_map[y0][x] < the_map[y0][x0]:
                    c += 1
                else:
                    c += 1
                    break
            d = 0
            for x in range(x0 + 1, len(the_map)):
                if the_map[y0][x] < the_map[y0][x0]:
                    d += 1
                else:
                    d += 1
                    break
            result = max(a * b * c * d, result)
    print(result)


if __name__ == "__main__":
    main()
