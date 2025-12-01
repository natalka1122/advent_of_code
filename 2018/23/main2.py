import re

FILENAME = "demo2.txt"  # expected 36
FILENAME = "input.txt"


def main() -> None:
    nanobots = []
    strongest = None
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", line)
            if line_match is None:
                raise NotImplementedError
            nanobots.append(
                (
                    int(line_match.group(1)),
                    int(line_match.group(2)),
                    int(line_match.group(3)),
                    int(line_match.group(4)),
                )
            )
            if strongest is None or strongest[3] < nanobots[-1][3]:
                strongest = nanobots[-1]
    if strongest is None:
        raise NotImplementedError
    print(f"strongest = {strongest}")
    result = 0
    for z, y, x, _ in nanobots:
        if abs(z - strongest[0]) + abs(y - strongest[1]) + abs(x - strongest[2]) <= strongest[3]:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
