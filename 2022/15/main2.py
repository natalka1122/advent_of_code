import re

FILENAME, MAX_COORD = "demo.txt", 20  # expected 56000011
FILENAME, MAX_COORD = "input.txt", 4000000


def main() -> None:
    result = set()
    for x in range(MAX_COORD):
        if x % 10 == 0 :
            print(x)
        for y in range(MAX_COORD):
            pass
    # with open(FILENAME, "r") as file:
    #     for line in file:
    #         line_match = re.match(
    #             r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
    #             line.strip(),
    #         )
    #         if line_match is None:
    #             raise NotImplementedError
    #         sx, sy, bx, by = map(int, line_match.groups())
    #         dist = abs(sx - bx) + abs(sy - by)
    #         if dist >= abs(sy - TARGET):
    #             print(sx, sy, bx, by)
    #         for x in range(sx - dist + abs(sy - TARGET), sx + dist - abs(sy - TARGET)):
    #             result.add(x)
    print(result)


if __name__ == "__main__":
    main()
