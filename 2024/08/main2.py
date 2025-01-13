from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"
EMPTY = "."


def main():
    the_map: dict[str, list[tuple[int, int]]] = dict()
    y = 0
    width = None
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if width is None:
                width = len(line)
            for x, value in enumerate(line):
                if value == EMPTY:
                    continue
                if value in the_map:
                    the_map[value].append((y, x))
                else:
                    the_map[value] = [(y, x)]
            y += 1
    height = y
    print(the_map)
    print(height, width)
    activated = set()
    for cells in the_map.values():
        print(f"cells = {cells}")
        for i in range(len(cells) - 1):
            for j in range(i, len(cells)):
                y1 = cells[i][0]
                y2 = cells[j][0]
                x1 = cells[i][1]
                x2 = cells[j][1]
                dy = y1 - y2
                dx = x1 - x2
                for count in range(1, width):
                    y = y1 + count * dy
                    x = x1 + count * dx
                    if 0 <= y < height and 0 <= x < width:
                        activated.add((y, x))
                    else:
                        break
                for count in range(1, width):
                    y = y1 - count * dy
                    x = x1 - count * dx
                    if 0 <= y < height and 0 <= x < width:
                        activated.add((y, x))
                    else:
                        break
    print(f"activated = {sorted(activated)}")
    print(len(activated))


if __name__ == "__main__":
    main()
