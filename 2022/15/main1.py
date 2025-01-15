import re

FILENAME, TARGET = "demo.txt", 10  # expected 26
FILENAME, TARGET = "input.txt", 2000000


def main() -> None:
    result = set()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            sx, sy, bx, by = map(int, line_match.groups())
            dist = abs(sx - bx) + abs(sy - by)
            if dist >= abs(sy - TARGET):
                print(sx, sy, bx, by)
            for x in range(sx - dist + abs(sy - TARGET), sx + dist - abs(sy - TARGET)):
                result.add(x)
    print(len(result))


if __name__ == "__main__":
    main()
