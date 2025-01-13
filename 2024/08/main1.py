from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"
EMPTY = "."


def main():
    the_map: dict[str, list[tuple[int, int]]] = dict()
    y = 0
    width = None
    antennas = set()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if width is None:
                width = len(line)
            for x, value in enumerate(line):
                if value == EMPTY:
                    continue
                antennas.add((y, x))
                if value in the_map:
                    the_map[value].append((y, x))
                else:
                    the_map[value] = [(y, x)]
            y += 1
    height = y
    print(the_map)
    print(height, width)
    activated = set()
    for symbol, cells in the_map.items():
        print(f"cells = {cells}")
        for i in range(len(cells) - 1):
            for j in range(i, len(cells)):
                for y, x in [
                    ((2 * cells[i][0] - cells[j][0]), (2 * cells[i][1] - cells[j][1])),
                    ((2 * cells[j][0] - cells[i][0]), (2 * cells[j][1] - cells[i][1])),
                ]:
                    if 0 <= y < height and 0 <= x < width:
                        if (y, x) not in antennas:
                            activated.add((symbol, y, x))
    print(f"activated = {sorted(activated)}")
    print(len(activated))


if __name__ == "__main__":
    main()
