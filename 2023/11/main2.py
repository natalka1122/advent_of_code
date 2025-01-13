from __future__ import annotations

# FILENAME = "demo.txt"
# FILENAME = "demo1.txt"
FILENAME = "input.txt"
# YEARS = 1
# YEARS = 10 - 1
# YEARS = 100 - 1
YEARS = 1000000 - 1


def main():
    height = 0
    width = None
    old_starmap = set()
    all_y = {-1: 0}
    all_x = {-1: 0}
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if height == 0:
                width = len(line)
            for x in range(len(line)):
                if line[x] == "#":
                    all_y[height] = None
                    all_x[x] = None
                    old_starmap.add((height, x))
            height += 1
    if not width:
        raise NotImplementedError
    prev_y = -1
    delta = 0
    for y in sorted(all_y.keys()):
        if y == -1:
            continue
        if y - prev_y > 1:
            delta += y - prev_y - 1
        print(f"y = {y} delta = {delta}")
        all_y[y] = y + delta * YEARS
        prev_y = y
    print(f"all_y = {all_y}")

    prev_x = -1
    delta = 0
    for x in sorted(all_x.keys()):
        if x == -1:
            continue
        if x - prev_x > 1:
            delta += x - prev_x - 1
        print(f"x = {x} delta = {delta}")
        all_x[x] = x + delta * YEARS
        prev_x = x
    print(f"all_x = {all_x}")
    starmap = list()
    while old_starmap:
        y, x = old_starmap.pop()
        starmap.append((all_y[y], all_x[x]))
    print(starmap)
    result = 0
    for i in range(len(starmap) - 1):
        for j in range(i + 1, len(starmap)):
            result += abs(starmap[i][0] - starmap[j][0]) + abs(
                starmap[i][1] - starmap[j][1]
            )
    print(result)


if __name__ == "__main__":
    main()
