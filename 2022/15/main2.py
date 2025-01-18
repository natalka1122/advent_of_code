import re

FILENAME, MAX_COORD = "demo.txt", 20  # expected 56000011
FILENAME, MAX_COORD = "input.txt", 4000000


def main() -> None:
    lines = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            lines.append(tuple(map(int, line_match.groups())))
    for y in range(MAX_COORD + 1):
        cuts: list[tuple[int, int]] = []
        for sx, sy, bx, by in lines:
            dist = abs(sx - bx) + abs(sy - by)
            if dist >= abs(sy - y):
                c1 = max(0, sx - dist + abs(sy - y))
                c2 = min(MAX_COORD, sx + dist - abs(sy - y))
                if c1 > c2:
                    continue
                if len(cuts) == 0:
                    cuts.append((c1, c2))
                else:
                    cuts.append((c1, c2))
                    has_changed = True
                    while has_changed:
                        has_changed = False
                        for index1 in range(len(cuts)):
                            for index2 in range(len(cuts)):
                                if index1 >= index2:
                                    continue
                                if cuts[index1][1] + 1 < cuts[index2][0]:
                                    continue
                                if cuts[index2][1] + 1 < cuts[index1][0]:
                                    continue
                                cuts[index1] = min(
                                    cuts[index1][0], cuts[index2][0]
                                ), max(cuts[index1][1], cuts[index2][1])
                                cuts.pop(index2)
                                has_changed = True
                                break
                            if has_changed:
                                break
        if len(cuts) == 0 or len(cuts) > 2:
            raise NotImplementedError
        if len(cuts) == 2:
            break
    if len(cuts) != 2:
        raise NotImplementedError
    print(y + 4000000 * (cuts[0][1] + 1))


if __name__ == "__main__":
    main()
