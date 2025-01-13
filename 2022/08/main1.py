from __future__ import annotations

FILENAME = "demo.txt"  # expected 21
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
            is_visible = True
            for y in range(y0):
                if the_map[y][x0] >= the_map[y0][x0]:
                    is_visible = False
                    break
            if is_visible:
                result += 1
                continue
            is_visible = True
            for y in range(y0 + 1, len(the_map)):
                if the_map[y][x0] >= the_map[y0][x0]:
                    is_visible = False
                    break
            if is_visible:
                result += 1
                continue
            is_visible = True
            for x in range(x0):
                if the_map[y0][x] >= the_map[y0][x0]:
                    is_visible = False
                    break
            if is_visible:
                result += 1
                continue
            is_visible = True
            for x in range(x0 + 1, len(the_map[0])):
                if the_map[y0][x] >= the_map[y0][x0]:
                    is_visible = False
                    break
            if is_visible:
                result += 1
    print(result)


if __name__ == "__main__":
    main()
