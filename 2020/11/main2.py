FILENAME = "demo.txt"  # expected 26
FILENAME = "input.txt"

EMPTY = "."
CHAIR = "L"


def f(
    the_map: dict[tuple[int, int], bool], height: int, width: int
) -> tuple[bool, int, dict[tuple[int, int], bool]]:
    result = dict()
    has_changed = False
    current_sum = 0
    for y0, x0 in the_map:
        calc_nei = 0
        for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            y = y0 + dy
            x = x0 + dx
            while (y, x) not in the_map and 0 <= y < height and 0 <= x < width:
                y = y + dy
                x = x + dx
            if (y, x) in the_map and the_map[y, x]:
                calc_nei += 1
        if not the_map[y0, x0] and calc_nei == 0:
            result[y0, x0] = True
            has_changed = True
        elif the_map[y0, x0] and calc_nei >= 5:
            result[y0, x0] = False
            has_changed = True
        else:
            result[y0, x0] = the_map[y0, x0]
        if result[y0, x0]:
            current_sum += 1
    return has_changed, current_sum, result


def main() -> None:
    the_map = dict()
    with open(FILENAME, "r") as file:
        y = 0
        for line in file:
            width = len(line)
            for x, symbol in enumerate(line.strip()):
                if symbol == CHAIR:
                    the_map[y, x] = False
            y += 1
    height = y
    has_changed = True
    while has_changed:
        has_changed, current_sum, the_map = f(the_map, height, width)
        # for y in range(height):
        #     for x in range(width):
        #         if (y,x) in the_map:
        #             if the_map[y,x]:
        #                 print("#",end="")
        #             else:
        #                 print("L",end="")
        #         else:
        #             print(".",end="")
        #     print()
        # print()
    print(current_sum)


if __name__ == "__main__":
    main()
